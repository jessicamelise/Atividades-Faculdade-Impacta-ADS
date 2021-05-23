from unittest.mock import Mock

import pytest

from meu_banco import Banco, Cliente, Conta


# ------------------------------ #
# -- Testes da classe Cliente -- #
# ------------------------------ #
def test_cria_cliente():
    try:
        c = Cliente('nome', '(11) 999-999-999', 'email@mail.com')
    except Exception:
        raise AssertionError('Erro ao criar o cliente')
    else:
        assert hasattr(c, 'nome'), 'não criou o atributo público nome'
        assert hasattr(c, 'telefone'), 'não criou o atributo público telefone'
        assert hasattr(c, 'email'), 'não criou o atributo público email'


@pytest.mark.parametrize('telefone', [5.2, -3, 999, [], {}])
def test_cria_cliente_telefone_type_error(telefone):
    try:
        Cliente('nome', telefone, 'email@mail.com')
    except TypeError:
        pass
    except Exception:
        raise AssertionError(
            'Erro diferente de TypeError para telefone que não é string')
    else:
        raise AssertionError('Criou cliente com telefone inválido')


@pytest.mark.parametrize(
    'telefone',
    ['11_999', '999*123', '999@abc.com', '11.99.123']
)
def test_cria_cliente_telefone_value_error(telefone):
    try:
        Cliente('nome', telefone, 'email@mail.com')
    except ValueError:
        pass
    except Exception:
        raise AssertionError(
            'Erro diferente de ValueError para telefone com caracteres inválidos')
    else:
        raise AssertionError('Criou cliente com telefone inválido')


@pytest.mark.parametrize('email', [5.2, -3, [], {}])
def test_cria_cliente_email_type_error(email):
    try:
        Cliente('nome', '11 9999-9999', email)
    except TypeError:
        pass
    except Exception:
        raise AssertionError(
            'Erro diferente de TypeError para email que não é string')
    else:
        raise AssertionError('Criou cliente com email inválido')


@pytest.mark.parametrize(
    'email',
    ['não é email', 'também.não.é.com.br', 'outro-que-não-é']
)
def test_cria_cliente_email_value_error(email):
    try:
        Cliente('nome', '11 9999-9999', email)
    except ValueError:
        pass
    except Exception:
        raise AssertionError(
            'Erro diferente de ValueError para email inválido')
    else:
        raise AssertionError('Criou cliente com email inválido')


def test_cliente_nome():
    c = Cliente('nome', '11 9999-9999', 'email@mail.com')
    assert c.nome == 'nome', 'Atributo nome com valor incorreto'
    try:
        c.nome = 'novo nome'
    except Exception:
        pass
    finally:
        assert c.nome == 'nome', 'O atributo nome não pode ser alterado'


def test_cliente_telefone():
    c = Cliente('nome', '11 9999-9999', 'email@mail.com')
    assert c.telefone == '11 9999-9999', 'Atributo telefone com valor incorreto'
    c.telefone = '11 888-777-000'
    assert c.telefone == '11 888-777-000', 'Não atualizou o valor de telefone'


@pytest.mark.parametrize(
    'telefone',
    [5.2, -3, 999, [], {}, '11_999', '999*123', '999@abc.com', '11.99.123']
)
def test_cliente_atualiza_telefone_com_erro(telefone):
    c = Cliente('nome', '11 9999-9999', 'email@mail.com')
    try:
        c.telefone = telefone
    except (TypeError, ValueError):
        pass
    except Exception:
        raise AssertionError('Erro diferente de TypeError/ValueError para telefone inválido')
    finally:
        assert c.telefone == '11 9999-9999', 'telefone não poderia ser alterado'


def test_cliente_email():
    c = Cliente('nome', '11 9999-9999', 'email@mail.com')
    assert c.email == 'email@mail.com', 'Atributo email com valor incorreto'
    c.email = 'outro@mail.com'
    assert c.email == 'outro@mail.com', 'Não atualizou o valor de email'


@pytest.mark.parametrize(
    'email',
    [5.2, -3, 999, [], {}, 'não é email', 'também.não.é.com.br', 'outro-que-não-é']
)
def test_cliente_atualiza_email_com_erro(email):
    c = Cliente('nome', '11 9999-9999', 'email@mail.com')
    try:
        c.email = email
    except (TypeError, ValueError):
        pass
    except Exception:
        raise AssertionError('Erro diferente de TypeError/ValueError para email inválido')
    finally:
        assert c.email == 'email@mail.com', 'email não poderia ser alterado'


# ---------------------------- #
# -- Testes da classe Conta -- #
# ---------------------------- #
def test_cria_conta():
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        c2 = Mock(nome='Cliente 2', telefone='11 9999-8888', email='cliente2@mail.com')
        cc = Conta([c1, c2], 1, 0)
    except Exception:
        raise AssertionError('Erro ao criar conta')
    else:
        assert hasattr(cc, 'clientes'), 'Não criou o atributo público clientes'
        assert hasattr(cc, 'numero'), 'Não criou o atributo público numero'
        assert hasattr(cc, 'saldo'), 'Não criou o atributo público saldo'


def test_conta_lista_de_clientes():
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        c2 = Mock(nome='Cliente 2', telefone='11 9999-8888', email='cliente2@mail.com')
        cc = Conta([c1, c2], 1, 0)
    except Exception:
        raise AssertionError('Erro ao criar conta')
    try:
        clientes = cc.clientes
    except Exception:
        raise AssertionError('Erro ao ler clientes')
    else:
        assert len(clientes) == 2, 'Esta conta deveria ter 2 clientes'
        msg = "Modificou os clientes da lista, não são os objetos passados"
        assert clientes[0] is c1 and clientes[1] is c2, msg
        assert clientes[0].nome == 'Cliente 1', 'Nome do cliente incorreto'
        assert clientes[0].telefone == '11 9999-9999', 'Telefone do cliente incorreto'
        assert clientes[0].email == 'cliente1@mail.com', 'Email do cliente incorreto'


@pytest.mark.parametrize('n', [1, 3, 25, 88])
def test_conta_numero(n):
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], n, 0)
    except Exception:
        raise AssertionError('Erro ao criar conta')
    else:
        assert cc.numero == n, 'Conta criada com número incorreto'


@pytest.mark.parametrize('saldo', [100, 300, 25000, 88.50, 0])
def test_conta_saldo_inicial_valido(saldo):
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], 1, saldo)
    except Exception:
        raise AssertionError('Erro ao criar conta')
    else:
        assert cc.saldo == saldo, 'Conta criada com saldo incorreto'


@pytest.mark.parametrize('valor', [100, 300, 25000, 88.50, 0])
def test_conta_deposito(valor):
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], 1, 100)
    except Exception:
        raise AssertionError('Erro ao criar conta')

    try:
        cc.depositar(valor)
    except Exception:
        raise AssertionError('Erro ao fazer depósito')
    else:
        assert cc.saldo == valor + 100, 'Saldo incorreto após depósito'
        msg = 'Depósito não registrado no extrato corretamente'
        assert ('deposito', valor) == cc.tirar_extrato()[-1], msg


@pytest.mark.parametrize('valor', [100, 300, 25000, 88.50, 0])
def test_conta_saque_valido(valor):
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], 1, 1e5)
    except Exception:
        raise AssertionError('Erro ao criar conta')

    try:
        cc.sacar(valor)
    except Exception:
        raise AssertionError('Erro ao fazer saque')
    else:
        assert cc.saldo == 1e5 - valor, 'Saldo incorreto após saque'
        msg = 'Saque não registrado no extrato corretamente'
        assert ('saque', valor) == cc.tirar_extrato()[-1], msg


@pytest.mark.parametrize('valor', [300.01, 25000, 808.50])
def test_conta_saque_invalido(valor):
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], 1, 300)
    except Exception:
        raise AssertionError('Erro ao criar conta')

    try:
        cc.sacar(valor)
    except ValueError:
        msg = 'O saldo não deve ser alterado quando o saque for inválido'
        assert cc.saldo == 300, msg
        msg = 'Um saque inválido não deve ser registrado no extrato'
        assert ('saque', valor) not in cc.tirar_extrato(), msg
    except Exception:
        raise AssertionError('Erro diferente de ValueError para saque inválido')
    else:
        raise AssertionError('Permitiu a realização de um saque inválido')


def test_conta_extrato():
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], 1, 100)
    except Exception:
        raise AssertionError('Erro ao criar conta')

    try:
        extrato = cc.tirar_extrato()
    except Exception:
        raise AssertionError('Erro ao tirar o extrato da conta')
    else:
        assert isinstance(extrato, list), 'O extrato deve ser uma lista'
        msg = 'O extrato deve conter apenas uma entrada para esse teste'
        assert len(extrato) == 1, msg
        msg = 'Saldo inicial não registrado no extrato'
        assert ('saldo inicial', 100) == extrato[0], msg


def test_conta_extrato_2():
    try:
        c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
        cc = Conta([c1], 1, 200)
    except Exception:
        raise AssertionError('Erro ao criar conta')

    try:
        cc.sacar(150)
        cc.depositar(250)
        extrato = cc.tirar_extrato()
    except Exception:
        raise AssertionError('Erro ao realizar as operações na conta')
    else:
        msg = 'O extrato deve conter três entradas para esse teste'
        assert len(extrato) == 3, msg
        msg = 'A {} entrada está incorreta'
        assert extrato[0] == ('saldo inicial', 200), msg.format('primeira')
        assert extrato[1] == ('saque', 150), msg.format('segunda')
        assert extrato[2] == ('deposito', 250), msg.format('terceira')


# ---------------------------- #
# -- Testes da classe Banco -- #
# ---------------------------- #
def test_cria_banco():
    try:
        b = Banco('nome')
    except Exception:
        raise AssertionError('Erro ao criar o Banco')
    else:
        assert hasattr(b, 'nome'), 'Não criou o atributo público nome'
        assert hasattr(b, 'contas'), 'Não criou o atributo público contas'
        assert hasattr(b, 'abrir_conta'), 'Não criou o método público abrir_conta'


def test_banco_nome():
    try:
        b = Banco('nome')
    except Exception:
        raise AssertionError('Erro ao criar o Banco')
    else:
        assert b.nome == 'nome', 'Atributo nome com valor incorreto'


def test_banco_comeca_sem_contas():
    try:
        b = Banco('nome')
    except Exception:
        raise AssertionError('Erro ao criar o Banco')
    else:
        assert b.contas == [], ('O banco deve começar sem nenhuma conta (lista vazia)')


def test_banco_abrir_conta():
    try:
        b = Banco('nome')
    except Exception:
        raise AssertionError('Erro ao criar o Banco')

    c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
    c2 = Mock(nome='Cliente 2', telefone='11 9999-8888', email='cliente2@mail.com')
    try:
        b.abrir_conta([c1], 200)
        b.abrir_conta([c2], 300)
    except Exception:
        raise AssertionError('Erro abrir as contas')
    else:
        assert len(b.contas) == 2, 'O banco deveria ter 2 contas'
        msg = 'Os elementos da lista de contas devem ser instâncias da classe Conta'
        for cc in b.contas:
            assert isinstance(cc, Conta), msg


def test_banco_numero_das_contas():
    try:
        b = Banco('nome')
    except Exception:
        raise AssertionError('Erro ao criar o Banco')

    try:
        for n in range(5):
            c1 = Mock(
                nome=f'Cliente {n}',
                telefone='11 9999-'+f'{n}'*4,
                email=f'cliente{n}@mail.com'
            )
            b.abrir_conta([c1], 100)
        ccs = b.contas
    except Exception:
        raise AssertionError('Erro ao abrir as contas')
    else:
        assert len(ccs) == 5, 'O banco deveria ter 5 contas'
        msg = 'Os elementos da lista de contas devem ser instâncias da classe Conta'
        assert all([isinstance(cc, Conta) for cc in ccs]), msg
        ordinais = ['primeira', 'segunda', 'terceira', 'quarta', 'quinta']
        msg = 'A {} conta deve ter o numero {}'
        for i, texto in enumerate(ordinais):
            assert ccs[i].numero == i+1, msg.format(texto, i+1)


@pytest.mark.parametrize('valor', [-100, -0.01, -2500])
def test_banco_abrir_conta_erro(valor):
    try:
        b = Banco('nome')
    except Exception:
        raise AssertionError('Erro ao criar o Banco')

    c1 = Mock(nome='Cliente 1', telefone='11 9999-9999', email='cliente1@mail.com')
    try:
        b.abrir_conta([c1], valor)
    except ValueError:
        pass
    except Exception:
        raise AssertionError('Erro diferente de ValueError para saldo inicial negativo')
    finally:
        assert len(b.contas) == 0, 'Abriu uma conta com saldo inicial negativo'