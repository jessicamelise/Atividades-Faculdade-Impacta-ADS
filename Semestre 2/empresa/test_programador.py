import pytest

from empresa import Programador


# ---------------------------------- #
# -- Testes da classe Programador -- #
# ---------------------------------- #
def test_programador_01_cria_objeto():
    try:
        prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    except Exception:
        raise AssertionError('Erro ao criar programador')
    else:
        assert prog.nome == 'Fulano', 'nome incorreto'
        assert prog.idade == 25, 'idade incorreta'
        assert prog.email == 'fulano@empresa.com', 'email incorreto'
        assert prog.carga_horaria == 40, 'carga horária incorreta'


@pytest.mark.parametrize('carga_horaria', [-5, 19, 41, 53])
def test_programador_02_cria_objeto_carga_horaria_invalida(carga_horaria):
    try:
        Programador('Fulano', 25, 'fulano@empresa.com', carga_horaria)
    except ValueError:
        pass
    except Exception:
        raise AssertionError('Erro diferente de ValueError')
    else:
        raise AssertionError('Programador criado com carga horária inválida')


@pytest.mark.parametrize('carga_horaria', [20, 31, 39])
def test_programador_03_altera_carga_horaria(carga_horaria):
    try:
        prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    except Exception:
        raise AssertionError('Erro ao criar programador')

    try:
        prog.carga_horaria = carga_horaria
    except Exception:
        raise AssertionError('Erro ao alterar a carga horária')
    else:
        msg = 'A carga horária não foi alterada para o novo valor'
        assert prog.carga_horaria == carga_horaria, msg


@pytest.mark.parametrize('carga_horaria', [-5, 19, 41, 53])
def test_programador_04_altera_carga_horaria_invalida(carga_horaria):
    try:
        prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    except Exception:
        raise AssertionError('Erro ao criar programador')

    try:
        prog.carga_horaria = carga_horaria
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert prog.carga_horaria == 40, msg
    except Exception:
        raise AssertionError('Erro diferente de ValueError')
    else:
        raise AssertionError('Não levantou ValueError para carga inválida')


def test_programador_05_calcula_salario():
    try:
        prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    except Exception:
        raise AssertionError('Erro ao criar programador')

    try:
        salario = prog.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao calcular salário')
    else:
        msg = 'Salário do programador calculado incorretamente'
        assert salario == 6300, msg


def test_programador_06_recebe_aumento():
    try:
        prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    except Exception:
        raise AssertionError('Erro ao criar programador')

    try:
        prog.aumenta_salario()
        salario = prog.calcula_salario()
    except Exception:
        raise AssertionError('Erro ao aumentar salário')
    else:
        msg = 'Aumento do salário de programador calculado incorretamente'
        assert salario == 6615, msg