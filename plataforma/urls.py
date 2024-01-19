from django.urls import path
from plataforma import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('imovel/<str:id>/', views.imovel, name='imovel'),
    path('agendar_visita/', views.agendar_visita, name='agendar_visita'),
    path('agendamentos/', views.agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', views.cancelar_agendamento, name="cancelar_agendamento")
]
