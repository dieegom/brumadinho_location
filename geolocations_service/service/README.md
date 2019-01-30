# Descrição

Este serviço fornece CRUDs para as geolocalizações

Atualmente conta com dois endpoints:

* `/api/geolocations/` para cadastro e recuperação de posições geográficas contendo latitude e longitude;

* `/api/visited_locations` para cadastro e recuperação de posições geográficas ja visitadas;


# Instalando

Clone o repositório para um dretório da sua preferencia


Instale os requerimentos para o servidor funcionar (preferencialmente em um ambiente virtual)

    pip install -r requirements.txt

## configuração básica:

    cp .env.template .env

Criando a base de dados inicial

    python manage.py migrate

## rodando local:

Rode o servidor

    python manage.py runserver


Acesse o servidor local em `localhost:8000/api/`


## HELP NEEDED

Tem muita coisa rpa ajustar aqui ainda