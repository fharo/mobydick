from django.contrib import admin

# Register your models here.
from .models import Registro

class AdminRegistro(admin.ModelAdmin):
    list_display = ["correo", "nombres","apellidos","timeslamp"]
    #list_display_links = [""]
    list_filter = ["correo"]
    lus_editable =["nombres","apellidos"]
    search_fileds =["correo","nombres","apellidos"]
    class Meta:
        model = Registro

admin.site.register(Registro, AdminRegistro)