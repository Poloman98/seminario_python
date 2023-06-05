from django.urls import path
from .views import Rol_APIView, Rol_APIView_List, Rol_APIView_Detail, Usuario_APIView, Usuario_APIView_List, Usuario_APIView_Detail, Servicio_APIView, Servicio_APIView_List, Servicio_APIView_Detail, Publicacion_APIView, Publicacion_APIView_List, Publicacion_APIView_Detail

# urlpatterns = [
#     path('v1/rol/add', Rol_APIView.as_view()),
#     path('v1/rol', Rol_APIView_List.as_view()),
#     path('v1/rol/<int:pk>', Rol_APIView_Detail.as_view()),
        
# ]


urlpatterns = [
    path('rol/', Rol_APIView_List.as_view(), name='rol-list'),
    path('rol/add', Rol_APIView.as_view(), name='rol-add'),
    path('rol/<int:pk>', Rol_APIView_Detail.as_view(), name='rol-detail'),

    path('usuario/', Usuario_APIView_List.as_view(), name='usuario-list'),
    path('usuario/add', Usuario_APIView.as_view(), name='usuario-add'),
    path('usuario/<int:pk>', Usuario_APIView_Detail.as_view(), name='usuario-detail'),

    path('servicio/', Servicio_APIView_List.as_view(), name='servicio-list'),
    path('servicio/add', Servicio_APIView.as_view(), name='servicio-add'),
    path('servicio/<int:pk>', Servicio_APIView_Detail.as_view(), name='servicio-detail'),

    path('publicacion/', Publicacion_APIView_List.as_view(), name='publicacion-list'),
    path('publicacion/add', Publicacion_APIView.as_view(), name='publicacion-add'),
    path('publicacion/<int:pk>', Publicacion_APIView_Detail.as_view(), name='publicacion-detail'),
]