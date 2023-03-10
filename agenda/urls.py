from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

#para criação das rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/', views.json_lista_evento),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento), #rota para salvar novo agendamento
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),    #rota para deletar
    path('', RedirectView.as_view(url='/agenda/')),  #forma para direcionar para outra url
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

]
