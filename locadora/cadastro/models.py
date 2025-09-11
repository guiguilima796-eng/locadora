
from tkinter import CASCADE
from django.db import models

class Locador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField( unique = True)
  
    def _str_(self):
        return self.nome

class Locatario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    
    def _str_(self):
        return self.nome
    
class Imovel (models.Model):
    TIPOS = [
        ('CASA','casa'),
        ('APT','apartamento'),    
        ('SAL','Sala Comercial'),
    ]
    
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE,related_name="imoveis")
    endereco = models.CharField(max_length=250)
    tipo = models.CharField( max_length=10, choices=TIPOS)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def _str_(self):
        return f"{self.tipo} - {self.endereco}"
    
class Contrato (models.Model):
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE, related_name="contratos")
    locatario = models.ForeignKey(Locatario,on_delete=models.CASCADE, related_name="contratos")
    imovel = models.ForeignKey(Imovel,on_delete=models.CASCADE, related_name="contratos")
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def _str_(self):
        return f"Contrato {self.locador} <-> {self.locatario} ({self.imovel})"

class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name="pagamentos")
    data_pagamento = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(
        max_length=20,
        choices=[
            ("PIX", "PIX"),
            ("BOLETO", "Boleto"),
            ("CARTAO", "Cartão"),
            ("TRANSFERENCIA", "Transferência Bancária"),
        ]
    )
    observacao = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Pagamento {self.contrato.id} - {self.valor_pago} em {self.data_pagamento}"