# WIKI
Wiki is project 1 of cs50w, Harvards web design course, using Django.
## introduction:
This project is a simulation of Wikipedia. It has a number of functions as follows.
* Index
* Search
* New Page
* Edit Page
* Random Page

The various pages are set in layout.html, which displays a sidebar with various functions available.

## Index.
The index function render index.html, where there is a sidebar with the other functions listed. The main part of the page displays a list of all the encyclopedia entries which are links to the various entries. the Entry  function is called when one of the titles is clicked. If for some reason the title is not found the error.html page is rendered with a apropriate error message. If the title is found the entry is converted from Markdown and rendered at entry.html.

## Search.
The Search function is implemented with a form written in the layout.html page as html (All the other forms in this app are django forms I used html for this form as an example.) When the submit button is clicked the search function checks the length of the submission, if it is zero the error page is rendered with a suitable message. If a correct entry is made it is compared to the list of titles, if the entry is found it is converted from markdown and rendered to entry.html. If the entry is not found it is checked to see if it is subset of any of the titles, if titles are found that do contain the subset they are listed on possible_entry.html and can be called with a click. If no entry is found error.html displays a suitable message. 

## Create New Page.
When the Create New Page icon is clicked the new_entry function is called. It takes the user to new_entry.html where there is a form with two inputs, title and entry. Because I used django forms to create them they have user side protection that ensures entries are made. When the form is submitted back to the function a further check is made to ensure that a title has been submitted. The function then checks the title against the list of titles to make sure the title does not already exist. if that is the case a warning is displayed and a suggestion the if the user wants to alter the title to use the edit facility. Otherwise the new entry is stored and displayed using HttpResponseRedirect and  reverse.

# Edit
The edit function is not displayed on the home page. On the entry page there a link to the entry function that also sends the entry title to the function. The function sends the EditForm with the existing contents to edit.html where the entry can be edited. When the user is happy with the new contents they can post the form back to the edit function where is is renderd to the entry.html using HttpResponseRedirect and reverse.

# Random 
The random function uses util.list_entries to create a list of all the avaiable titles. Randint from the random module is the used to select one of the titles which is then change from markdown to normal text and rendered  to entry.html.

# Conclusion
That describes all of the features of the wiki app. I found this project to be difficult and it has taken me a long time to compete but I have enjoyed it and learnt a lot.
