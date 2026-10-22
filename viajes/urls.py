from django.urls import path
from . import views
urlpatterns=[path('',views.lista_viajes),path('iniciar/',views.iniciar_viaje),path('viaje/<str:codigo>/',views.detalle_viaje,name='detalle_viaje'),path('viaje/<str:codigo>/agregar/',views.agregar_peaje),path('viaje/<str:codigo>/finalizar/',views.finalizar_viaje)]
