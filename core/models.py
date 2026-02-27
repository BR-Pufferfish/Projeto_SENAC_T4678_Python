from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"


class Pessoa(models.Model):
    cpf_cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    OPCOES_PESSOA = [
        ('Cliente', 'Cliente'),
        ('Colaborador', 'Colaborador')
        ]
    tipo_pessoa = models.CharField(max_length=20, choices=OPCOES_PESSOA, default='Cliente')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.razao_social} - {self.cpf_cnpj}"


class Estoque(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)
    mercadoria = models.CharField(max_length=100)
    data_entrada = models.DateTimeField(auto_now_add=True)
    origem = models.CharField(max_length=100)
    saldo = models.IntegerField()
    status = models.CharField(
    max_length=20,
    choices=[
        ('Disponivel', 'Disponível'),
        ('Despachado', 'Despachado'),
    ],
    default='Disponivel'
)

    def __str__(self):
        return f"{self.mercadoria} - {self.saldo}"


class Movimentacoes(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)
    estoque = models.ForeignKey(Estoque, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()
    dtSaida = models.DateTimeField(auto_now_add=True)
    destino = models.CharField(max_length=100)
    OPCOES_STATUS = [
        ('Transportando', 'Transportando'),
        ('Entregue', 'Entregue')
        ]
    status = models.CharField(max_length=20, choices=OPCOES_STATUS, default='Transportando')

    def __str__(self):
        return f"{self.estoque.mercadoria} - {self.quantidade} - {self.status}"