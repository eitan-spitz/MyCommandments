from django.forms import ModelForm, Select, HiddenInput

from account_app.models import UserFiltering

CHOICES = (('Y','Yes'),('N','No'))
OPTIONS = (('Male','Male'),('Female','Female'))

class PersonalCommandmentsForm(ModelForm):
    class Meta:
        model = UserFiltering
        fields = ['user','live_in_israel','kohen','not_a_vegetarian','judge','farmer','married','children','employer','lend','sorcery','gender']
        widgets = {
            'user': HiddenInput(),
            'live_in_israel': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'kohen': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'not_a_vegetarian': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'judge': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'farmer': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'married': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'children': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'employer': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'lend': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'sorcery': Select(choices=CHOICES, attrs={'class': 'form-control w-75', }),
            'gender': Select(choices=OPTIONS, attrs={'class': 'form-control w-75', }),
        }