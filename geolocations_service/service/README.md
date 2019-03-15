# Português-BR

## Descrição

Este serviço fornece CRUDs para as geolocalizações

Atualmente conta com três endpoints:

* `/api/geolocations/` para cadastro e recuperação de posições geográficas contendo latitude e longitude;

* `/api/visited_locations/` para cadastro e recuperação de posições geográficas ja visitadas;

* `/api/found_people/` para cadastro e recuperação de pessoas localizadas em uma geolocalização;


## Instalando

Clone o repositório para um dretório da sua preferencia

Instale os requerimentos para o servidor funcionar (preferencialmente em um ambiente virtual).


### Desenvolvimento
    pip install -r service.requirements.txt

### Rode as migrations já existentes.
    
    python manage.py migrate


## Rodando:

### Desenvolvimento

    make run

Acesse o servidor local em `localhost:5002/api/`

## Testes

#### Rodar todos os testes
Para rodar os testes de maneira geral basta executar

    make test

#### Rodar testes indiviualmente
Para rodar um testes específico execute o comando `python manage.py test brumadinho.tests.<test_name>` onde `<test_name>` é o nome do arquivo contendo o teste que deseja executar. i.e:

    python manage.py test brumadinho.tests.test_geolocation

## HELP NEEDED

Tem muita coisa que pode ser feita aqui ainda, toda ajuda é necessária.


<hr />

# English

## Description

This service serves CRUD for geoposition data.

For now it only have three endpoints:

* `/api/geolocations/` for creating and retrieving of groposition information (latitude and longitude));

* `/api/visited_locations/` for creating and retrieving already visited geopositions;

* `/api/found_people/` for creating and retrieving found people in a geoposition coordinate;

## Installing

Clone repo to a workspace.

Install requeriments (preferably in a virtual environment)

### Development
    pip install -r service.requirements.txt

### Migrate the database

    python manage.py migrate

## Running:

### Development

    make run_dev

Acess local server at `localhost:5002/api/`

## Tests

#### Run all tests
To run all tests just execute:

    make test

#### Running tests individually
To run an single especific test execute `python manage.py test brumadinho.tests.<test_name>` where `<test_name>` is the filename which is the one you want to execute i.e:

    python manage.py test brumadinho.tests.test_geolocation

## HELP NEEDED

There are a lot of work to do here yet, all help is needed.

<hr />
