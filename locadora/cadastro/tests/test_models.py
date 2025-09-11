from datetime import date
import pytest 
from cadastro.models import Locador,Locatario,Imovel,Contrato

@pytest.mark.django_db 
def test_criar_locador():
    novo_locador = Locador.objects.create(nome='Carlos Silva' , email='carlos@example.com')
    assert novo_locador.nome == 'Carlos Silva'
    assert Locador.objects.count() == 1
    
@pytest.mark.django_db  
def test_criar_locatario():
    novo_locatario = Locatario.objects.create(nome='Maria Souza' , telefone='(11)99999-9999')
    assert 'Maria' in novo_locatario.nome
    assert Locatario.objects.count() == 1
    
@pytest.mark.django_db
def test_criacao_imovel():
    locador = Locador.objects.create(nome="Carlos", email="carlos@example.com", telefone="11999999999")
    imovel = Imovel.objects.create(
        locador=locador,
        endereco="Rua das Flores, 123",
        tipo="CASA",
        valor_mensal=2500.00
    )
    assert imovel.locador == locador
    assert Imovel.objects.count() == 1
@pytest.mark.django_db
def test_criacao_contrato():
    locador = Locador.objects.create(nome="Ana", email="ana@example.com", telefone="11911111111")
    locatario = Locatario.objects.create(nome="Pedro", email="pedro@example.com", telefone="11922222222")
    imovel = Imovel.objects.create(
        locador=locador,
        endereco="Av. Paulista, 1000",
        tipo="APT",
        valor_mensal=3500.00
    )
    contrato = Contrato.objects.create(
        locador=locador,
        locatario=locatario,
        imovel=imovel,
        data_inicio=date(2025, 1, 1),
        data_fim=date(2025, 12, 31),
        valor=3500.00
    )
    assert contrato.imovel == imovel
    assert contrato.locatario == locatario
    assert Contrato.objects.count() == 1