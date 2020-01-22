from django.contrib.auth.models import User
from django.db import models
from django.forms.models import model_to_dict

# Create your models here.

class Commandments(models.Model):
    my_order = models.IntegerField(primary_key=True)
    mitzvah = models.CharField(max_length=256)
    chinuch_order = models.IntegerField()
    book = models.CharField(max_length=20, blank=True, null=True)
    parsha = models.CharField(max_length=20, blank=True, null=True)
    chapter = models.IntegerField(blank=True, null=True)
    verse = models.IntegerField(blank=True, null=True)
    p_n = models.CharField(db_column='p/n', max_length=1)  # Field renamed to remove unsuitable characters.
    man_v = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    live_in_israel = models.CharField(max_length=1)
    kohen = models.CharField(max_length=1)
    not_a_vegetarian = models.CharField(max_length=1)
    judge = models.CharField(max_length=1)
    farmer = models.CharField(max_length=1)
    married = models.CharField(max_length=1)
    children = models.CharField(max_length=1)
    employer = models.CharField(max_length=1)
    lend = models.CharField(max_length=1)
    sorcery = models.CharField(max_length=1)
    social = models.BooleanField(default=False)
    faith = models.BooleanField(default=False)
    ritual = models.BooleanField(default=False)
    monetary = models.BooleanField(default=False)
    speech = models.BooleanField(default=False)
    holidays = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    criminal = models.BooleanField(default=False)
    intimacy = models.BooleanField(default=False)
    idolatry = models.BooleanField(default=False)


    class Meta:
        managed = False
        db_table = 'commandments'
        ordering = ['my_order']

class UserFiltering(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    live_in_israel = models.CharField(verbose_name='Do you live in Israel?', max_length=1)
    kohen = models.CharField(verbose_name='Are you a Kohen?', max_length=1)
    not_a_vegetarian = models.CharField(verbose_name='Do you eat meat?', max_length=1)
    judge = models.CharField(verbose_name='Are you a judge?', max_length=1)
    farmer = models.CharField(verbose_name='Are you a farmer?', max_length=1)
    married = models.CharField(verbose_name='Are you married?', max_length=1)
    children = models.CharField(verbose_name='Do you have children?', max_length=1)
    employer = models.CharField(verbose_name='Do you employ workers?', max_length=1)
    lend = models.CharField(verbose_name='Do you often lend money?', max_length=1)
    sorcery = models.CharField(verbose_name='Do you practice sorcery?', max_length=1)
    gender = models.CharField(max_length=10, default='Both')

    def get_dict(self):
        return model_to_dict(self,exclude=('id','user'))
