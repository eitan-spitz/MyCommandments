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
    social = models.CharField(max_length=1, blank=True, null=True)
    faith = models.CharField(max_length=1, blank=True, null=True)
    ritual = models.CharField(max_length=1, blank=True, null=True)
    monetary = models.CharField(max_length=1, blank=True, null=True)
    speech = models.CharField(max_length=1, blank=True, null=True)
    holidays = models.CharField(max_length=1, blank=True, null=True)
    food = models.CharField(max_length=1, blank=True, null=True)
    criminal = models.CharField(max_length=1, blank=True, null=True)
    intimacy = models.CharField(max_length=1, blank=True, null=True)
    idolatry = models.CharField(max_length=1, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'commandments'

class UserFiltering(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    def get_dict(self):
        return model_to_dict(self,exclude=('id','user'))
