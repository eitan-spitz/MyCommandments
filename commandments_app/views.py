from django.shortcuts import render
from account_app.models import Commandments

# Create your views here.
def index(request):
    return render(request, 'commandments_app/index.html')

def homepage(request):
    commandments = Commandments.objects.all() # need to add here filtering functionality
    return render(request, 'commandments_app/homepage.html', {'commandments': commandments})