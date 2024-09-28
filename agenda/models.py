from django.db import models

# MODELO EM DJANGO:
# --> qualquer entidade que represente algum objeto, por exemplo, poderia haver uma aplicação com modelo de usuários, que seria para representar um usuário na aplicação

# NESTE CASO (AGENDADOR de AGENDAS):
# --> poderemos ter um modelo Evento para representar um evento


# Create your models here.

class Categoria(models.Model): # models.Model, indica que a classe é um modelo
    nome = models.CharField(max_length=100, unique=True) # --- nome da categoria; parâmetros: (max_length=100, unique=True), unique=True torna o nome da categoria único

    def __str__(self): # --- para mostrar o nome da categoria ao invés de mostrar o id
        return f"{self.nome} ({self.id})"




class Evento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # ---  on_delete=models.SET_NULL, para caso a categoria seja removida, o evento não será removido
    local = models.CharField(max_length=100, blank=True) # --- blank=True, para caso o campo seja deixado em branco
    link = models.CharField(max_length=100, blank=True)

    # adicionando o atributo 'data'
    data = models.DateField(null=True, blank=True)
    
    # adicionando o atributo 'participantes'
    participantes = models.IntegerField(default=0)

    # def __init__(self, nome, categoria, local=None, link=None):
    #     self.nome = nome
    #     self.categoria = categoria
    #     self.local = local
    #     self.link = link

    def __str__(self):
        return f"{self.nome} ({self.id})"