from django.shortcuts import render
from . import util
import markdown
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse 
from random import randint

class NewPageForm(forms.Form):
   title = forms.CharField(label="Entry Title")
   entry = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':40, 'style':'width:100% max-width:500px; height:250px'}))


class EditRequestForm(forms.Form):
    title = forms.CharField()
    #widget=forms.HiddenInput()

class EditForm(forms.Form):
    entry = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':40, 'style':'width:100% max-width:500px; height:250px'}))

   
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries
    })

def entry(request, title):
    entry_md = util.get_entry(title)    
    if entry_md is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Entry not found."
        })

    entry = markdown.markdown(entry_md)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
        })
    

def search(request):
    if request.method =="POST":
        # Get title and remove whitespace       
        title = request.POST.get("search_title").strip()
        
        # Check that text has been added.
        if len(title) == 0:
            return render(request, "encyclopedia/error.html", {
                "message": "Please enter a search value"
            })

        # Get a list of titles of the entries (names)
        names = util.list_entries() 
        possible_entry = []

        for name in names:
            if title.lower() == name.lower():
                entry_md = util.get_entry(name) 
                entry = markdown.markdown(entry_md)
                          
                return render(request, "encyclopedia/search.html",{
                    "title": title,
                    "entry": entry,
                    "form":EditRequestForm(initial={
                        "title": title
                    })
                    })
                        
        # Check if the title entered is part any of the names listed.       
        if title.lower() != name.lower():           
            for name in names:
                if title.lower() in name.lower():
                    possible_entry.append(name)
            if len(possible_entry) == 0:
                return render(request, "encyclopedia/error.html",{
                    "message": "Sorry there are no close matches."            
                })

            return render(request, "encyclopedia/possible_entry.html",{
                "title": title,
                "possible_entry": possible_entry
            })
        

def new_entry(request):
    if request.method == "POST":
        # Take the submitted data and save it as form
        form = NewPageForm(request.POST)
        # Check if the data is valid (server side)
        if form.is_valid():
            # Isolate title from the cleaned  version of form data and remove white space.
            title = (form.cleaned_data["title"]).strip()
            if len(title) == 0:
                return render(request, "encyclopedia/error.html",{
                    "message": "Please start by entering a title"
                })
            names = util.list_entries()
            for name in names:
                if name.lower() == title.lower():
                    return render(request, "encyclopedia/error.html",{
                        "message": "This entry already exists. If you wish to alter it use Edit."
                    })
                
            # Isolate entry from the cleaned version of form data.
            entry = form.cleaned_data["entry"]
            util.save_entry(title, entry)
            return HttpResponseRedirect(reverse("encyclopedia:entry",args = [title]))
            #entry = markdown.markdown(entry)
            #return render(request, "encyclopedia/entry.html",{
                #"title": title,
                #"entry":entry,
                #"form":NewPageForm(initial={
                    #"entry": entry
                                #})
            
            #})
                       
    else:
        return render(request, "encyclopedia/new_entry.html",{
            "form": NewPageForm()
        })
    
def edit(request, title):
    if request.method == "POST":
        # Take the submitted data and save it as form
        entry = request.POST.get("entry")
        util.save_entry(title, entry)
        return HttpResponseRedirect(
    reverse("encyclopedia:entry", args =[title])
)
    # Render EditForm with the existing entry included
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html",{
            "message": "Edit has failed"
        })    
    return render(request,"encyclopedia/edit.html",{
    "title": title,
    "form":EditForm(initial={
                    "entry":entry
                        }) 
    })
    
def random(request):
    names=[]
    names = util.list_entries()
    name = randint(0, (len(names)-1))
    title = names[name]
    entry_md = util.get_entry(title)
    entry = markdown.markdown(entry_md)
    return render(request, "encyclopedia/entry.html",{
        "title": title,
        "entry": entry

    })

    