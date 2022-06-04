from django.contrib import admin
from mainIndex.models import chargerState
# Register your models here.

class chargerStateAdmin(admin.ModelAdmin):
    list_display:('charger_state','charger_mode','ev_connect_state','update_time','update_date')

admin.site.register(chargerState,chargerStateAdmin)