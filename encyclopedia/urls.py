from django.urls import path

from . import views
app_name = "encyclopedia" 
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/",views.entry,name="entry"),
    path("search", views.search, name= "search"),
    path("wiki/<str:title/new_entry", views.new_entry, name= "new_entry"), 
    path("wiki/<str:title>/edit", views.edit, name= "edit"),
    path("random", views.random, name = "random")

]