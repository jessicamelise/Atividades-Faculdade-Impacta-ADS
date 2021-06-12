import pytest
from unittest.mock import Mock, patch

import empresa


# ------------------------------ #
# -- Testes da classe Empresa -- #
# ------------------------------ #
def test_empresa_01_cria_empresa_atributos_publicos():
    try:
        emp = empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', [])
    except Exception:
        raise AssertionError('Erro ao criar empresa')
    else:
        msg = 'Não criou/expôs o atributo público {}'
        for attr in ['nome', 'cnpj', 'area_atuacao', 'equipe']:
            assert hasattr(emp, attr), msg.format(attr)


def test_empresa_02_cria_empresa_metodos_publicos():
    try:
        emp = empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', [])
    except Exception:
        raise AssertionError('Erro ao criar empresa')
    else:
        msg = 'Não criou/expôs o método público {}'
        for attr in [
                'contrata',
                'folha_pagamento',
                'dissidio_anual',
                'listar_visitas',
                'zerar_visitas_vendedores',
                ]:
            assert hasattr(emp, attr), msg.format(attr)


@pytest.mark.parametrize('nome', [123, {}, [], 5.5])
def test_empresa_03_cria_empresa_erro_nome(nome):
    try:
        empresa.Empresa(nome, '28.934.280/0001-24', 'Tecnologia', [])
    except empresa.EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError('Levantou um erro diferente de EmpresaCreationError')
    else:
        raise AssertionError('Criou empresa com valores inválidos')


@pytest.mark.parametrize('cnpj', [123, {}, [], 5.5])
def test_empresa_04_cria_empresa_erro_cnpj(cnpj):
    try:
        empresa.Empresa('ACME', cnpj, 'Tecnologia', [])
    except empresa.EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError('Levantou um erro diferente de EmpresaCreationError')
    else:
        raise AssertionError('Criou empresa com valores inválidos')


@pytest.mark.parametrize('area', [123, {}, [], 5.5])
def test_empresa_05_cria_empresa_erro_area(area):
    try:
        empresa.Empresa('ACME', '28.934.280/0001-24', area, [])
    except empresa.EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError('Levantou um erro diferente de EmpresaCreationError')
    else:
        raise AssertionError('Criou empresa com valores inválidos')


@pytest.mark.parametrize('funcionario', [123, {}, [], 5.5])
def test_empresa_06_cria_empresa_erro_funcionario(funcionario):
    try:
        empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', [funcionario])
    except empresa.EmpresaCreationError:
        pass
    except Exception:
        raise AssertionError('Levantou um erro diferente de EmpresaCreationError')
    else:
        raise AssertionError('Criou empresa com valores inválidos')


def test_empresa_07_equipe_inicial():
    with patch.object(empresa, 'Estagiario', Mock) as estagiario_mock, \
            patch.object(empresa, 'Funcionario', Mock):
        est = estagiario_mock(nome='Pedro', idade=25, email='pedro@empresa.com', carga_horaria=20)
        try:
            emp = empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', [est])
        except (empresa.EmpresaCreationError, TypeError):
            raise AssertionError('Não usou isinstance() para verificar o tipo do Funcionário')
        except Exception:
            raise AssertionError('Erro ao criar empresa com funcionário válido')
        else:
            msg = 'A empresa deve ser criada com a equipe passada'
            assert len(emp.equipe) == 1, msg
            msg = 'O objeto de funcionário recebido em `equipe` não deve ser alterado'
            assert emp.equipe[0] is est, msg


def test_empresa_08_contrata():
    with patch.object(empresa, 'Estagiario', Mock) as estagiario_mock, \
            patch.object(empresa, 'Programador', Mock) as programador_mock, \
            patch.object(empresa, 'Vendedor', Mock) as vendedor_mock, \
            patch.object(empresa, 'Funcionario', Mock):
        est = estagiario_mock(nome='Maria', idade=25, email='maria@empresa.com', carga_horaria=20)
        prog = programador_mock(nome='Ana', idade=31, email='ana@empresa.com', carga_horaria=40)
        vend = vendedor_mock(nome='Marcos', idade=28, email='marcos@empresa.com', carga_horaria=35)
        try:
            emp = empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', [])
            emp.contrata(est)
            emp.contrata(prog)
            emp.contrata(vend)
        except TypeError:
            raise AssertionError('Não usou isinstance() para verificar o tipo do Funcionário')
        except Exception:
            raise AssertionError('Erro ao contratar funcionário do tipo correto')
        else:
            msg = 'A equipe não contém o número correto de funcionários contratados'
            assert len(emp.equipe) == 3, msg
            msg = 'O {0} item da equipe não é o {0} funcionário contratado'
            assert emp.equipe[0] is est, msg.format('primeiro')
            assert emp.equipe[1] is prog, msg.format('segundo')
            assert emp.equipe[2] is vend, msg.format('terceiro')


def test_empresa_09_folha_pagamento():
    with patch.object(empresa, 'Estagiario', Mock) as estagiario_mock, \
            patch.object(empresa, 'Programador', Mock) as programador_mock, \
            patch.object(empresa, 'Vendedor', Mock) as vendedor_mock, \
            patch.object(empresa, 'Funcionario', Mock):
        est = estagiario_mock(**{'calcula_salario.return_value': 2500})
        prog = programador_mock(**{'calcula_salario.return_value': 6500})
        vend = vendedor_mock(**{'calcula_salario.return_value': 4800})
        equipe = [est, prog, vend]

        try:
            emp = empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', equipe)
        except Exception:
            raise AssertionError('Erro ao criar empresa')

        try:
            folha_pagamento = emp.folha_pagamento()
        except Exception:
            msg = 'Erro ao calcular a folha de pagamento (use o método calcula_salario de cada funcionário)'
            raise AssertionError(msg)
        else:
            assert folha_pagamento == 13800, 'Cálculo da folha de pagamento incorreto'
            classes = ['Estagiario', 'Programador', 'Vendedor']
            msg1 = 'O método calcula_salario do objeto de {} não foi chamado'
            msg2 = 'O método calcula_salario do objeto de {} foi chamado mais de uma vez'
            msg3 = 'O método calcula_salario deveria ser chamado sem passar nenhum argumento'
            for funcionario, class_ in zip(equipe, classes):
                assert funcionario.calcula_salario.call_count > 0, msg1.format(class_)
                assert funcionario.calcula_salario.call_count < 2, msg2.format(class_)
                assert len(funcionario.calcula_salario.call_args.args) == 0, msg3.format(class_)


def test_empresa_10_dissidio():
    with patch.object(empresa, 'Estagiario', Mock) as estagiario_mock, \
            patch.object(empresa, 'Programador', Mock) as programador_mock, \
            patch.object(empresa, 'Vendedor', Mock) as vendedor_mock, \
            patch.object(empresa, 'Funcionario', Mock):
        est = estagiario_mock()
        prog = programador_mock()
        vend = vendedor_mock()
        equipe = [est, prog, vend]

        try:
            emp = empresa.Empresa('ACME', '28.934.280/0001-24', 'Tecnologia', equipe)
        except Exception:
            raise AssertionError('Erro ao criar empresa')

        try:
            emp.dissidio_anual()
        except Exception:
            raise AssertionError('Erro ao calcular a folha de pagamento')
        else:
            msg1 = 'O método aumenta_salario do objeto de {} não foi chamado'
            msg2 = 'O método aumenta_salario do objeto de {} foi chamado mais de uma vez'
            msg3 = 'O método aumenta_salario deveria ser chamado sem passar nenhum argumento'
            classes = ['Estagiario', 'Programador', 'Vendedor']
            for funcionario, class_ in zip(equipe, classes):
                assert funcionario.aumenta_salario.call_count > 0, msg1.format(class_)
                assert funcionario.aumenta_salario.call_count < 2, msg2.format(class_)
                assert len(funcionario.aumenta_salario.call_args.args) == 0, msg3.format(class_)