from django.db import models


edit_date = models.DateTimeField('Edit the date', auto_now=True)


class Usuario(models.Model):

    '''classe para criaçao do modelo do gráfico'''

    permissao = models.CharField(max_length=100)

    class Meta:
        db_table = "cadastro_usuario"
        managed = False


class Person(models.Model):

    '''Ajustar campos. Deixar igual a tabela crm_gvb.cadastro_usuario'''
    '''classe responsavel por listar os dados da tabel'''

    nome = models.CharField(max_length=255, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    nascimento = models.DateField(blank=False)
    login_crm = models.CharField(max_length=255)
    senha_crm = models.CharField(max_length=255)
    id_fast = models.IntegerField()
    permissao = models.CharField(max_length=255, blank=False)
    skill = models.CharField(max_length=255, blank=False)
    empresa = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=255, blank=False)
    telefone1 = models.CharField(max_length=12, blank=False)
    telefone2 = models.CharField(max_length=12, blank=False)


    class Meta:
        db_table = "cadastro_usuario"
        managed = False


class Ponto(models.Model):
    usuario = models.CharField(max_length=255)
    data_horario = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "ponto_eletronico"
        managed = False













