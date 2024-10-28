from django.contrib import admin
from equipoBasket.models import Equipo
# Register your models here.
class equipoAdmin(admin.ModelAdmin):
    list_display =['nombreEquipo','ciudad','conferencia','estadio','anioFundacion']
admin.site.register(Equipo,equipoAdmin)