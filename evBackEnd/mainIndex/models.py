from pyexpat import model
from django.db import models
from django.forms import BooleanField

# Create your models here.

class chargerState(models.Model):
    charger_state       = models.BooleanField(default=0)
    charger_mode        = models.IntegerField(default=1)
    ev_connect_state    = models.BooleanField(default=0)
    update_time         = models.TimeField(null=True)
    update_date         = models.DateField(null=True)

class pConsumptionData(models.Model):
    update_time         = models.TimeField(null=False)
    update_data         = models.DateField(null=False)
    grid_voltage        = models.IntegerField(default=0)
    pow_cnsmp_frm_grid  = models.IntegerField(default=0)
    solar_pv_voltage    = models.IntegerField(default=0)
    pow_cnsmp_frm_pv    = models.IntegerField(default=0)
    ev_batt_voltage     = models.IntegerField(default=0)
    ev_batt_power_cnsmp = models.IntegerField(default=0)
    
   