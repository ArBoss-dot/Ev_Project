from django.db import models
from django.forms import BooleanField

# Create your models here.

class chargerState(models.Model):
    charger_state = models.BooleanField(default=0)
    charger_mode = models.IntegerField(default=1)
    ev_connect_state = models.BooleanField(default=0)
    update_time = models.TimeField(null=True)
    update_date = models.DateField(null=True)