from django.db import models

# Create your models here.

class Rol(models.Model):
    id          = models.IntegerField(max_length = 100, verbose_name = "id", primary_key=True)
    nombre      = models.CharField(max_length = 20, verbose_name = "nombre")


    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
    
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id          = models.IntegerField(max_length = 100, verbose_name = "id", primary_key=True)
    nombre      = models.CharField(max_length = 40, verbose_name = "nombre")
    apellido    = models.CharField(max_length = 40, verbose_name = "apellido")
    telefono    = models.CharField(max_length = 40, verbose_name = "telefono")
    correo      = models.CharField(max_length = 40, verbose_name = "correo")
    password    = models.CharField(max_length = 40, verbose_name = "password")
    direccion   = models.CharField(max_length = 60, verbose_name = "direccion")
    id_rol      = models.ForeignKey(Rol, on_delete = models.CASCADE)
    foto        = models.CharField(max_length = 400, verbose_name = "url_foto",blank= True, null= True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.nombre
    

class Servicio(models.Model):
    id          = models.IntegerField(max_length = 100, verbose_name = "id", primary_key=True)
    nombre      = models.CharField(max_length = 80, verbose_name = "nombre")

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.nombre



class Publicacion(models.Model):
    id            = models.IntegerField(max_length = 100, verbose_name = "id", primary_key=True)
    titulo        = models.CharField(max_length = 100, verbose_name = "titulo", null = True)
    fecha_creado  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    usu_id        = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    foto          = models.CharField(max_length = 400, verbose_name = "url_foto",blank= True, null= True)
    descripcion   = models.CharField(max_length = 400, verbose_name = "descripcion")
    fecha_editado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    servicio_id   = models.ForeignKey(Servicio, on_delete= models.CASCADE)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
    
    def __str__(self):
        return self.titulo