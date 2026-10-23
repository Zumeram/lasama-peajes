from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_choferes, name='lista_choferes'),  # Choferes móvil
    path('finanzas/', views.dashboard_finanzas, name='dashboard_finanzas'),  # Finanzas PC
    path('iniciar/', views.iniciar_viaje, name='iniciar_viaje'),
    path('viaje/<str:codigo>/', views.detalle_viaje, name='detalle_viaje'),
    path('viaje/<str:codigo>/agregar/', views.agregar_peaje, name='agregar_peaje'),
    path('viaje/<str:codigo>/finalizar/', views.finalizar_viaje, name='finalizar_viaje'),
]
