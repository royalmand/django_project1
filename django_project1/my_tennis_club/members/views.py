# Django views are Python functions that takes http requests and returns http response, like HTML documents.
# But how can we execute the view? Well, we must call the view via a URL.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

# atau 
def members(request):
    """
    Retrieves a list of all members from the database and renders an HTML template to display the members.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered HTML template with the list of members.
    """
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# Expalantion all_members.html karena kalo run comment jd error 
# {% %} brackets inside the HTML document?
# They are Django Tags, telling Django to perform some programming logic inside these brackets.


# The members view does the following:

# Creates a mymembers object with all the values of the Member model.
# Loads the all_members.html template.
# Creates an object containing the mymembers object.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.

def details(request, id):
    """"
    Retrieves a member object from the database based on the provided ID and renders a details.html template with the member's information.
    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the member to retrieve.
    Returns:
        HttpResponse: The rendered details.html template with the member's information.
    """
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['apple', 'banana', 'orange'],
    }
    return HttpResponse(template.render(context, request))