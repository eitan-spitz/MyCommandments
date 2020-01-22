import django_filters
from django import forms
from django.db import models
from django.forms import Select
from django_filters.widgets import BooleanWidget

from account_app.models import Commandments
from commandments_app.forms import PersonalCommandmentsForm


class CommandmentsFilter(django_filters.FilterSet):
    class Meta:
        model = Commandments
        fields = {
            'mitzvah': ['icontains'],
        }


class PersonalFilter(django_filters.FilterSet):

    class Meta:
        model = Commandments
        exclude = ['my_order','mitzvah','chinuch_order','book','parsha','chapter','verse','p_n','man_v','social','faith','ritual','monetary','speech','holidays','food','criminal','intimacy','idolatry']
        form = PersonalCommandmentsForm


CHOICES = (('Unknown','No Filter'),(True,'True'),(False,'False'))

class HopmepageFilter(django_filters.FilterSet):
    social = django_filters.BooleanFilter(field_name='social', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    faith = django_filters.BooleanFilter(field_name='faith', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    ritual = django_filters.BooleanFilter(field_name='ritual', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    monetary = django_filters.BooleanFilter(field_name='monetary', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    speech = django_filters.BooleanFilter(field_name='speech', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    holidays = django_filters.BooleanFilter(field_name='holidays', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    food = django_filters.BooleanFilter(field_name='food', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    criminal = django_filters.BooleanFilter(field_name='criminal', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    intimacy = django_filters.BooleanFilter(field_name='intimacy', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    idolatry = django_filters.BooleanFilter(field_name='idolatry', widget=Select(choices=CHOICES, attrs={'class': 'form-control w-25', }))
    class Meta:
        model = Commandments
        fields = ['social','faith','ritual','monetary','speech','holidays','food','criminal','intimacy','idolatry']

        exclude = ['my_order', 'mitzvah', 'chinuch_order', 'book', 'parsha', 'chapter', 'verse', 'p_n', 'man_v','gender','live_in_israel','kohen','not_a_vegetarian','judge','farmer','married','children','employer','lend','sorcery']
        # widgets = {
        #     'social': BooleanWidget()
        # }

        # filter_overrides = {
        #     models.BooleanField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     },
        # }


NewFilter = django_filters.MultipleChoiceFilter()

class NewFilter(django_filters.FilterSet):

    class Meta:
        model = Commandments
        fields = ['social', 'faith', 'ritual', 'monetary', 'speech', 'holidays', 'food', 'criminal', 'intimacy',
                  'idolatry']

        exclude = ['my_order', 'mitzvah', 'chinuch_order', 'book', 'parsha', 'chapter', 'verse', 'p_n', 'man_v',
                   'gender', 'live_in_israel', 'kohen', 'not_a_vegetarian', 'judge', 'farmer', 'married', 'children',
                   'employer', 'lend', 'sorcery']