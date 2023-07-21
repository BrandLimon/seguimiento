from django.contrib import admin
from GestSeguir.models import Egresado,Empleadore

# Register your models here.
class Egresados2(admin.ModelAdmin):
    list_display = ("nombre", "apepat","apemat","matric","direccion","email","numero", "carrera")
    search_fields = ("nombre", "matric")
    list_filter = ("nombre", "matric", "carrera")
    
class Empleadores2(admin.ModelAdmin):
    list_display = ("nombre", "apepat","apemat","matric","numcedula","direccion","email","numero")
    search_fields = ("nombre", "matric")


admin.site.register(Egresado, Egresados2)
admin.site.register(Empleadore, Empleadores2)

