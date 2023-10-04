from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.template import RequestContext

from .forms import NameForm

# Create your views here

def index(request):

    your_name=''

    submitbutton= request.POST.get("submit")

    # if this is a POST request we need to process the form data
    if request.method == "POST":

     # create a form instance and populate it with data from the request:
        form= NameForm(request.POST or None)

        # check whether it's valid:

        if form.is_valid():

            your_name= form.cleaned_data.get("your_name")

        # if a GET (or any other method) we'll create a blank form
    else:
            form = NameForm()


    context= {'form': form, 'your_name': your_name, 'submitbutton': submitbutton}

    return render(request, 'index.html', context)

'''
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form}, RequestContext(request))
'''
