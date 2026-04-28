from django.shortcuts import render
from . import util
import markdown
from django import forms

class NewPageForm(forms.Form):
   Title = forms.CharField(label="Entry Title")
   entry = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':40, 'style':'width:100% max-width:500px; height:250px'}))

   from django import forms


   




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
        "entry": entry
    })

def search(request):
    if request.method =="POST":
        # Get heading and remove whitespace
        heading = (request.POST.get("search_title")).strip()
        # Check that text has been added.
        if len(heading) == 0:
            return render(request, "encyclopedia/error.html", {
                "message": "Please enter a search value"
            })

        # Get a list of titles of the entries (names)
        names = util.list_entries() 
        possible_entry = []

        for name in names:
            if heading.lower() == name.lower():
                entry_md = util.get_entry(name) 
                entry = markdown.markdown(entry_md)            
                return render(request, "encyclopedia/search.html",{
                    "heading":heading,
                    "entry": entry
                    })
            
                pass
        # See if the title entered is part any of the names listed.       
        if heading.lower() != name.lower():           
            for name in names:
                if heading.lower() in name.lower():
                    possible_entry.append(name)
                
            return render(request, "encyclopedia/possible_entry.html",{
                "heading": heading,
                "possible_entry": possible_entry
            })
        

def new_page(request):
    return render(request, "encyclopedia/new_page.html",{
        "form": NewPageForm

})