from django.contrib import admin
from mainIndex.models import chargerState, pConsumptionData
# Register your models here.

class chargerStateAdmin(admin.ModelAdmin):
    list_display:('charger_state','charger_mode','ev_connect_state','update_time','update_date')

admin.site.register(chargerState,chargerStateAdmin)

class powerConsumptionAdmin(admin.ModelAdmin):
    list_display:('update_time','update_data','grid_voltage','pow_cnsmp_frm_grid','solar_pv_voltage','pow_cnsmp_frm_pv','ev_batt_voltage','ev_batt_power_cnsmp')

admin.site.register(pConsumptionData,powerConsumptionAdmin)