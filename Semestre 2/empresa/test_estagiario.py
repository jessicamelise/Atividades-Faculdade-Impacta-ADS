import pytest

from empresa import Estagiario


# --------------------------------- #
# -- Testes da classe Estagiario -- #
# --------------------------------- #
def test_estagiario_01_cria_objeto():
    try:
        est = Estagiario('Fulano', 25, 'fulano@empresa.com', 30)
    except Exception:
        raise AssertionError('Erro ao criar estagiario')
    else:
        assert est.nome == 'Fulano', 'nome incorreto'
        assert est.idade == 25, 'idade incorreta'
        assert est.email == 'fulano@empresa.com', 'email incorreto'
        assert est.carga_horaria == 30, 'carga horária incorreta'


@pytest.mark.parametrize('carga_horaria', [-5, 15, 31, 40])
def test_estagiario_02_cria_objeto_carga_horaria_invalida(carga_horaria):
    try:
        Estagiario('Fulano', 25, 'fulano@empresa.com', carga_horaria)
    except ValueError:
        pass
    except Exception:
        raise AssertionError('Erro diferente de ValueError')
    else:
        raise AssertionError('Estagiario criado com carga horária inválida')


@pytest.mark.parametrize('carga_horaria', [16, 20, 29])
def test_estagiario_03_altera_carga_horaria(carga_horaria):
    try:
        est = Estagiario('Fulano', 25, 'fulano@empresa.com', 30)
    except Exception:
        raise AssertionError('Erro ao criar estagiario')

    try:
        est.carga_horaria = carga_horaria
    except Exception:
        raise AssertionError('Erro ao alterar a carga horária')
    else:
        msg = 'A carga horária não foi alterada para o novo valor'
        assert est.carga_horaria == carga_horaria, msg


@pytest.mark.parametrize('carga_horaria', [-5, 15, 31, 40])
def test_estagiario_04_altera_carga_horaria_invalida(carga_horaria):
    try:
        est = Estagiario('Fulano', 25, 'fulano@empresa.com', 30)
    except Exception:
        raise AssertionError('Erro ao criar estagiario')

    try:
        est.carga_horaria = carga_horaria
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert est.carga_horaria == 30, msg
    except Exception:
        raise AssertionError('Erro diferente de ValueError')
    else:
        raise AssertionError('Não levantou ValueError para carga inválida')


def test_estagiario_05_calcula_salario():
    try:
        est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar estagiario')

    try:
        salario = est.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao calcular salário')
    else:
        msg = 'Salário do estagiario calculado incorretamente'
        assert salario == 1645, msg


def test_estagiario_06_recebe_aumento():
    try:
        est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    except Exception:
        raise AssertionError('Erro ao criar estagiario')

    try:
        est.aumenta_salario()
        salario = est.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao aumentar salário')
    else:
        msg = 'Aumento do salário de estagiario calculado incorretamente'
        assert abs(salario - 1714.75) < 0.01, msg