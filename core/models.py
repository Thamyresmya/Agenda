from django.db import models
from django.contrib.auth.models import User

# criando as tabelas da agenda
class Evento(models.Model):
    titulo = models.CharField(max_length=100)   #limite de caracter
    descricao = models.TextField(blank=True, null=True)  #pode ser em branco ou null
    data_evento = models.DateTimeField(verbose_name='Data do Evento')   #para renomear como vai aparecer
    data_criacao = models.DateTimeField(auto_now=True)  #data atual do registro
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  #usar os usuarios do django / caso seja deletado, tds eventos tbm serão


    #mudar o nome da tabela
    class Meta:
        db_table = 'evento'

    #para aparecer o titulo como nome do evento
    def __str__(self):
        return self.titulo

    #formato da data/hora
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

