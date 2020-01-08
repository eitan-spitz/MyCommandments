from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from commandments_app.forms import PersonalCommandmentsForm

from account_app.models import Commandments

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

def homepage(request):
    commandments = Commandments.objects.all() # filter(kohen=user.info.kohen,) need to add here filtering functionality
    return render(request, 'commandments_app/homepage.html', {'commandments': commandments})

def all_commandments(request):
    commandments = Commandments.objects.all() # need to add here filtering functionality
    filter = CommandmentsFilter(request.GET, commandments)
    return render(request, 'commandments_app/all_commandments.html', {'commandments': commandments, 'filter': filter})

class MitzvahPage(DetailView):
    model = Commandments
    template_name = 'commandments_app/commandment_details.html'