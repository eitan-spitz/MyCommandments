import django_filters

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
