# Plano de melhoria — Parte 2

Baseline: v1.0-parte1

## Problema 1 — Dependências sem versões fixadas

- Evidência: https://sonarcloud.io/project/issues?open=AaHSYVa5pEqpRtwXc5H0&id=Lunare-dot_flaskr-qualidade
- Ação: Definir versões específicas e compatíveis para as dependências apontadas no pyproject.toml e verificar a instalação e execução do projeto.
- Indicador: Quantidade de ocorrências do alerta de dependências sem versões fixadas no SonarCloud.
- Valor inicial: 1 ocorrência.
- Meta: 0 ocorrências.
- Responsável: Matheus.

## Problema 2 — Possível acesso a valor nulo

- Evidência: https://sonarcloud.io/project/issues?open=AaHSYVZipEqpRtwXc5Hy&id=Lunare-dot_flaskr-qualidade
- Ação: Verificar e corrigir o possível acesso a g.user quando seu valor for None, além de adicionar testes automatizados.
- Indicador: Quantidade de ocorrências da regra S2259 no SonarCloud.
- Valor inicial: 1 ocorrência.
- Meta: 0 ocorrências.
- Responsável: Matheus.

## Refatoração planejada

- Arquivo: flaskr/blog.py
- Ação: Extrair a leitura e validação dos dados dos formulários de criação e edição de posts para uma função compartilhada.
- Indicador 1: Número de ocorrências da condição "if not title".
- Indicador 2: Número de leituras diretas de request.form["title"] e request.form["body"].
- Objetivo: Reduzir a repetição sem alterar o comportamento dos formulários.
- Validação: Testes automatizados do blog.

## Problema não priorizado

O alerta de CSRF permanecerá em aberto, pois sua implementação exigiria alterações mais abrangentes nos formulários e testes.
