# Flaskr — Projeto de Qualidade de Software

## Sobre o projeto

Flaskr é uma aplicação web de blog baseada no tutorial oficial do Flask.

Permite cadastrar usuários, realizar login e criar, editar e excluir publicações.

Este projeto está sendo utilizado na disciplina de Qualidade de Software para
análise de atributos, métricas, testes e gerenciamento de configuração.

## Tecnologias

- Python
- Flask
- SQLite
- HTML e Jinja
- CSS
- Pytest
- Coverage.py

## Requisitos

- Python 3.9 ou superior.

## Instalação

Crie e ative um ambiente virtual:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -e ".[test]"
```

## Execução

Inicialize o banco:

```powershell
flask --app flaskr init-db
```

Inicie a aplicação:

```powershell
flask --app flaskr run --debug
```

Acesse http://127.0.0.1:5000.

## Cobertura de testes

Para executar os testes com cobertura:

```powershell
coverage run -m pytest
coverage report -m
```

## Para gerar um relatório HTML:

```powershell
coverage html
```

O relatório estará disponível em: htmlcov/index.html

## Estrutura

- flaskr/: código principal.
- tests/: testes automatizados.
- pyproject.toml: configuração e dependências.
- README.md: documentação do projeto.

## Origem

Exemplo oficial do Flask, versão 3.1.3.

https://github.com/pallets/flask/tree/3.1.3/examples/tutorial

## Equipe

- Matheus Ferreira Souza
- Sport Club Corinthians Paulista
