"""Testes planejados para o tratamento de None e a refatoracao do blog.
"""

import pytest
from flask import g
from werkzeug.exceptions import Forbidden, NotFound

from flaskr.blog import get_post


def test_get_post_sem_usuario(app):
    with app.test_request_context('/1/update'):
        g.user = None
        with pytest.raises(Forbidden):
            get_post(1)


def test_get_post_sem_verificacao_de_autoria(app):
    with app.test_request_context('/'):
        g.user = None
        post = get_post(1, check_author=False)
        assert post['id'] == 1


def test_get_post_inexistente(app):
    with app.test_request_context('/9999/update'):
        g.user = None
        with pytest.raises(NotFound):
            get_post(9999)


@pytest.mark.parametrize('path', ['/create', '/1/update'])
def test_titulo_obrigatorio_apos_refatoracao(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': 'Teste'})
    assert response.status_code == 200
    assert b'Title is required.' in response.data