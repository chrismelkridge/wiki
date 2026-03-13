from django.shortcuts import render
from . import util
import markdown
from django import forms

class FindEntry(forms.Form):
    form = forms.CharField(label="Find Entry")

from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
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
    })cd


