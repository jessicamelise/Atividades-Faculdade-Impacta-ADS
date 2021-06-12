import pytest

from empresa import Vendedor


# ------------------------------- #
# -- Testes da classe Vendedor -- #
# ------------------------------- #
def test_vendedor_01_cria_objeto():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 45)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')
    else:
        assert vend.nome == 'Fulano', 'nome incorreto'
        assert vend.idade == 25, 'idade incorreta'
        assert vend.email == 'fulano@empresa.com', 'email incorreto'
        assert vend.carga_horaria == 45, 'carga horária incorreta'
        assert vend.visitas == 0, 'visitas devem começar em zero'


@pytest.mark.parametrize('carga_horaria', [-5, 14, 46, 52])
def test_vendedor_02_cria_objeto_carga_horaria_invalida(carga_horaria):
    try:
        Vendedor('Fulano', 25, 'fulano@empresa.com', carga_horaria)
    except ValueError:
        pass
    except Exception:
        raise AssertionError('Erro diferente de ValueError')
    else:
        raise AssertionError('Vendedor criado com carga horária inválida')


@pytest.mark.parametrize('carga_horaria', [15, 29, 44])
def test_vendedor_03_altera_carga_horaria(carga_horaria):
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 45)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.carga_horaria = carga_horaria
    except Exception:
        raise AssertionError('Erro ao alterar a carga horária')
    else:
        msg = 'A carga horária não foi alterada para o novo valor'
        assert vend.carga_horaria == carga_horaria, msg


@pytest.mark.parametrize('carga_horaria', [-5, 14, 46, 52])
def test_vendedor_04_altera_carga_horaria_invalida(carga_horaria):
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 30)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.carga_horaria = carga_horaria
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert vend.carga_horaria == 30, msg
    except Exception:
        raise AssertionError('Erro diferente de ValueError')
    else:
        raise AssertionError('Não levantou ValueError para carga inválida')


def test_vendedor_05_realizar_visitas():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    msg = 'Não atualizou o número de visitas do vendedor corretamente'
    n_visitas = 0
    for n in [3, 9, 5, 2]:
        try:
            vend.realizar_visita(n)
        except Exception:
            raise AssertionError('Erro ao realizar visitas')
        else:
            n_visitas += n
            assert vend.visitas == n_visitas, msg


@pytest.mark.parametrize('n', ['5', 'abc', 5.2, [3], {5}])
def test_vendedor_06_realizar_visitas_erro_de_tipo(n):
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.realizar_visita(n)
    except TypeError:
        pass
    except Exception:
        raise AssertionError('Levantou erro diferente de TypeError')
    else:
        raise AssertionError('Não levantou erro para entrada inválida')


@pytest.mark.parametrize('n', [-10, -1, 11, 23])
def test_vendedor_07_realizar_visitas_erro_de_valor(n):
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.realizar_visita(n)
    except ValueError:
        pass
    except Exception:
        raise AssertionError('Levantou erro diferente de ValueError')
    else:
        raise AssertionError('Não levantou erro para entrada inválida')


def test_vendedor_08_zerar_visitas():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.realizar_visita(5)
        vend.zerar_visitas()
    except Exception:
        raise AssertionError('Erro ao realizar e/ou zerar visitas')
    else:
        msg = 'O número de visitas não foi zerado corretamente'
        assert vend.visitas == 0, msg


def test_vendedor_09_calcula_salario():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        salario = vend.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao calcular salário')
    else:
        msg = 'Salário do vendedor calculado incorretamente'
        assert salario == 3050, msg


def test_vendedor_10_calcula_salario_2():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.realizar_visita(8)
        vend.realizar_visita(6)
        vend.realizar_visita(9)
        salario = vend.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao calcular salário')
    else:
        msg = 'Salário do vendedor calculado incorretamente'
        assert salario == 3740, msg


def test_vendedor_11_recebe_aumento():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.aumenta_salario()
        salario = vend.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao aumentar salário')
    else:
        msg = 'Aumento do salário de vendedor calculado incorretamente'
        assert abs(salario - 3185) < 0.01, msg


def test_vendedor_12_recebe_aumento_2():
    try:
        vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar vendedor')

    try:
        vend.aumenta_salario()
        vend.realizar_visita(6)
        salario = vend.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao aumentar salário')
    else:
        msg = 'Aumento do salário de vendedor calculado incorretamente'
        assert abs(salario - 3365) < 0.01, msg