from django.contrib import admin
from .models import Rol, Usuario, Servicio, Publicacion

# Register your models here.

class Rol_Admin(admin.ModelAdmin):
    # search_fields = ('nombre' )
    list_display = ('id', 'nombre')
    ordering = ('id',)

class Usuario_Admin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido', 'correo', 'id_rol')
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'correo', 'password', 'direccion', 'id_rol', 'foto')
    ordering = ('-id',)

class Servicio_Admin(admin.ModelAdmin):
    search_fields = ('id','nombre')
    list_display = ('id', 'nombre')
    ordering = ('-id',)

class Publicacion_Admin(admin.ModelAdmin):
    readonly_fields = ('fecha_creado', 'fecha_editado')
    search_fields = ('titulo', 'fecha_creado', 'descripcion', 'fecha_editado')
    list_display = ('id', 'titulo', 'fecha_creado', 'usu_id', 'foto', 'descripcion', 'fecha_editado', 'servicio_id')
    ordering = ('-id',)
    

admin.site.register(Rol, Rol_Admin)
admin.site.register(Usuario, Usuario_Admin)
admin.site.register(Servicio, Servicio_Admin)
admin.site.register(Publicacion, Publicacion_Admin)