Nidus

# Backend

É preferível rodar o Backend através do docker container disponibilizado nesse repositório.

## Com Docker

Para rodar o backend localmente, você precisará ter instalado Docker assim como o Docker Compose.

1. Rode `docker-compose up`
2. Acesse http://0.0.0.0:8080/docs

## Sem Docker

Para rodar o backend localmente sem docker, você precisará do Python 3.9.

1. Instale o poetry:

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
```

2. Instale as dependências:

```sh
poetry install
```

3. Rode o `uvicorn`:

`uvicorn backend.main:app --reload`

4. Acesse http://0.0.0.0:8080/docs

## Resultado

Você deverá ser levado à documentação da API do Nidus e verá uma tela como essa:

<img src="https://github.com/BSI-PCS-2021-1/Nidus/blob/master/.docs/fastapi_landing_page.png" width="300">
