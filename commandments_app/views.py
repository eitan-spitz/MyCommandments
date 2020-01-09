import operator
from functools import reduce

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from commandments_app.forms import PersonalCommandmentsForm

from account_app.models import Commandments, UserFiltering

# Create your views here.
from commandments_app.filters import CommandmentsFilter, PersonalFilter


def index(request):
    return render(request, 'commandments_app/index.html')

class CommandmentsFiltering(CreateView):
    form_class = PersonalCommandmentsForm
    template_name = 'commandments_app/commandments_filtering.html'
    success_url = '/homepage'

    def get_form(self, form_class=None):
        form = super(CommandmentsFiltering, self).get_form(form_class)
        form.fields['user'].initial = self.request.user
        return form


def filter_down(dictionary): # filters out the y answers so the filtering can work properly
    smaller_dict = dict()
    for (key,value) in dictionary.items():
        if value == 'N':
            smaller_dict[key] = 'Y' # for the logic of the db the filter only needs to filter out where the answer in those columns is N
    return smaller_dict


def homepage(request):
    user_info = UserFiltering.objects.filter(user=request.user)[0] # finds the user info and gets the answers from the login form
    filter = filter_down(user_info.get_dict())
    commandments = Commandments.objects.filter(**filter)  # filters the commandments by the answers to form where the answer was no
    return render(request, 'commandments_app/homepage.html', {'commandments': commandments})

def all_commandments(request):
    commandments = Commandments.objects.all()
    filter = CommandmentsFilter(request.GET, commandments)
    return render(request, 'commandments_app/all_commandments.html', {'commandments': commandments, 'filter': filter})

class MitzvahPage(DetailView):
    model = Commandments
    template_name = 'commandments_app/commandment_details.html'