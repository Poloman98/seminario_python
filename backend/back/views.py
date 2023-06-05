from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RolSerializers, UsuarioSerializers, ServicioSerializers, PublicacionSerializers
from .models import Rol, Usuario, Servicio, Publicacion
from django.http import Http404

#################################################################### Rol
class Rol_APIView_List(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        roles = Rol.objects.all()
        serializer = RolSerializers(roles, many=True)
        return Response(serializer.data)

class Rol_APIView(APIView):

    def post(self, request, format=None):
        serializer = RolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Rol_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Rol.objects.get(pk=pk)
        except Rol.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RolSerializers(role)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RolSerializers(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
################################################################### Usuario
class Usuario_APIView_List(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        usu = Usuario.objects.all()
        serializer = UsuarioSerializers(usu, many=True)
        return Response(serializer.data)

class Usuario_APIView(APIView):

    def post(self, request, format=None):
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Usuario_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsuarioSerializers(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsuarioSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#################################################################### Servicio
class Servicio_APIView_List(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        servicios = Servicio.objects.all()
        serializer = ServicioSerializers(servicios, many=True)
        return Response(serializer.data)

class Servicio_APIView(APIView):

    def post(self, request, format=None):
        serializer = ServicioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Servicio_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        serv = self.get_object(pk)
        serializer = ServicioSerializers(serv)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        serv = self.get_object(pk)
        serializer = ServicioSerializers(serv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        serv = self.get_object(pk)
        serv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#################################################################### Publicacion
class Publicacion_APIView_List(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        publicaciones = Publicacion.objects.all()
        serializer = PublicacionSerializers(publicaciones, many=True)
        return Response(serializer.data)

class Publicacion_APIView(APIView):

    def post(self, request, format=None):
        serializer = PublicacionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Publicacion_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Publicacion.objects.get(pk=pk)
        except Publicacion.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        publi = self.get_object(pk)
        serializer = PublicacionSerializers(publi)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        publi = self.get_object(pk)
        serializer = PublicacionSerializers(publi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        publi = self.get_object(pk)
        publi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)