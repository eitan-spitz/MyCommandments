import django_filters
from django import forms
from django.db import models

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

class HopmepageFilter(django_filters.FilterSet):
    # has_social = django_filters.BooleanFilter(field_name='social', lookup_expr='isnull', exclude=True)
    # has_faith = django_filters.BooleanFilter(field_name='faith', lookup_expr='isnull', exclude=True)
    # has_ritual = django_filters.BooleanFilter(field_name='ritual', lookup_expr='isnull', exclude=True)
    # has_monetary = django_filters.BooleanFilter(field_name='monetary', lookup_expr='isnull', exclude=True)
    # has_speech = django_filters.BooleanFilter(field_name='speech', lookup_expr='isnull', exclude=True)
    # has_holidays = django_filters.BooleanFilter(field_name='holidays', lookup_expr='isnull', exclude=True)
    # has_food = django_filters.BooleanFilter(field_name='food', lookup_expr='isnull', exclude=True)
    # has_criminal = django_filters.BooleanFilter(field_name='criminal', lookup_expr='isnull', exclude=True)
    # has_intimacy = django_filters.BooleanFilter(field_name='intimacy', lookup_expr='isnull', exclude=True)
    # has_idolatry = django_filters.BooleanFilter(field_name='idolatry', lookup_expr='isnull', exclude=True)
    class Meta:
        model = Commandments
        fields = {
            'social': ['isnull'],
            'faith': ['isnull'],
            'ritual': ['isnull'],
            'monetary': ['isnull'],
            'speech': ['isnull'],
            'holidays': ['isnull'],
            'food': ['isnull'],
            'criminal': ['isnull'],
            'intimacy': ['isnull'],
            'idolatry': ['isnull']
        }

        exclude = ['my_order', 'mitzvah', 'chinuch_order', 'book', 'parsha', 'chapter', 'verse', 'p_n', 'man_v','gender','live_in_israel','kohen','not_a_vegetarian','judge','farmer','married','children','employer','lend','sorcery']

        filter_overrides = {
            models.BooleanField: {
                'filter_class': django_filters.BooleanFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxInput,
                },
            },
        }