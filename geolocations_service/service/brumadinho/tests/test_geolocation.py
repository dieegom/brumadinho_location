from rest_framework import status
from rest_framework.test import APITestCase
from brumadinho.models import Geolocation
from django.contrib.gis.geos import Point


class GeolocationTests(APITestCase):
    def setUp(self):
        '''
        Define a pré-inicialização dos modelos de teste.
        '''

        latitude = -134.99908
        longitude = 0.98217931

        location = Geolocation.objects.create(
            latitude=latitude,
            longitude=longitude,
            coordinates=Point(longitude, latitude)
        )

    def test_create_a_geolocation(self):
        '''
        Teste que prova a criação de uma geolocalização
        fornecendo latitude e longitude.
        '''

        url = '/api/geolocations/'

        latitude = -100.12345
        longitude = 0.987101

        data = {
            'latitude': latitude,
            'longitude': longitude
        }
        response = self.client.post(url, data, format='json')

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['type'], 'Feature')
        self.assertEqual(response.data['geometry']['type'], 'Point')
        self.assertEqual(
            response.data['geometry']['coordinates'], [longitude, latitude]
        )
        self.assertEqual(
            response.data['properties']['latitude'], latitude
        )
        self.assertEqual(
            response.data['properties']['longitude'], longitude
        )

        # verifica o banco de dados
        created_object = Geolocation.objects.get(
            latitude=latitude,
            longitude=longitude
        )
        self.assertEqual(Geolocation.objects.count(), 2)
        self.assertEqual(created_object.latitude, latitude)
        self.assertEqual(created_object.longitude, longitude)

    def test_create_a_geolocation_without_latitude(self):
        '''
        Verifica que a tentativa de criar uma geolocalização
        sem fornecer um valor de latitude falha, pois este é um
        campo obrigatório.
        '''

        url = '/api/geolocations/'
        expected_error = 'This field is required.'

        longitude = 0.987101

        data = {
            'longitude': longitude
        }
        response = self.client.post(url, data, format='json')
        error = str(response.data['latitude'][0])

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error, expected_error)

        # verifica o banco de dados
        # deve haver somente um objeto, que foi criado durante o setUp
        self.assertEqual(Geolocation.objects.count(), 1)

    def test_create_a_geolocation_without_longitude(self):
        '''
        Verifica que a tentativa de criar uma geolocalização
        sem fornecer um valor de longitude falha, pois este é um
        campo obrigatório.
        '''

        url = '/api/geolocations/'
        expected_error = 'This field is required.'

        latitude = 123.1238129812

        data = {
            'latitude': latitude
        }
        response = self.client.post(url, data, format='json')
        error = str(response.data['longitude'][0])

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error, expected_error)

        # verifica o banco de dados
        # deve haver somente um objeto, que foi criado durante o setUp
        self.assertEqual(Geolocation.objects.count(), 1)

    def test_create_a_geolocation_with_null_latitude(self):
        '''
        Verifica que a tentativa de criar uma geolocalização
        fornecendo null (None) para latitude falha, pois este é um
        campo não nulo.
        '''

        url = '/api/geolocations/'
        expected_error = 'This field may not be null.'

        longitude = 0.987101

        data = {
            'latitude': None,
            'longitude': longitude
        }
        response = self.client.post(url, data, format='json')
        error = str(response.data['latitude'][0])

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error, expected_error)

        # verifica o banco de dados
        # deve haver somente um objeto, que foi criado durante o setUp
        self.assertEqual(Geolocation.objects.count(), 1)

    def test_create_a_geolocation_with_null_longitude(self):
        '''
        Verifica que a tentativa de criar uma geolocalização
        fornecendo null (None) para longitude falha, pois este é um
        campo não nulo.
        '''

        url = '/api/geolocations/'
        expected_error = 'This field may not be null.'

        latitude = 0.987101

        data = {
            'latitude': latitude,
            'longitude': None
        }
        response = self.client.post(url, data, format='json')
        error = str(response.data['longitude'][0])

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error, expected_error)

        # verifica o banco de dados
        # deve haver somente um objeto, que foi criado durante o setUp
        self.assertEqual(Geolocation.objects.count(), 1)

    def test_update_a_geolocation(self):
        '''
        Verifica a tentativa de atualizacão dos dados de uma
        localização ja cadastrada.
        '''

        location = Geolocation.objects.get(
            latitude=-134.99908,
            longitude=0.98217931
        )
        url = '/api/geolocations/{}/'.format(location.id)

        new_lat = 90.99999
        new_long = 09.0909

        data = {
            'latitude': new_lat,
            'longitude': new_long
        }
        response = self.client.put(url, data, format='json')

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Feature')
        self.assertEqual(response.data['geometry']['type'], 'Point')
        self.assertEqual(
            response.data['geometry']['coordinates'], [new_long, new_lat]
        )
        self.assertEqual(
            response.data['properties']['latitude'], new_lat
        )
        self.assertEqual(
            response.data['properties']['longitude'], new_long
        )

        # verifica o banco de dados
        updated_object = Geolocation.objects.get(id=location.id)
        self.assertEqual(Geolocation.objects.count(), 1)
        self.assertEqual(updated_object.latitude, new_lat)
        self.assertEqual(updated_object.longitude, new_long)

    def test_get_geolocation(self):
        '''
        Verifica a consulta à uma localização.
        '''

        location = Geolocation.objects.get(
            latitude = -134.99908,
            longitude = 0.98217931
        )

        url = '/api/geolocations/{}/'.format(location.id)

        response = self.client.get(url, format='json')

        # verifica a resposta da requisição ao serviço
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Feature')
        self.assertEqual(response.data['geometry']['type'], 'Point')
        self.assertEqual(
            response.data['geometry']['coordinates'], [
                location.longitude,
                location.latitude
            ]
        )
        self.assertEqual(
            response.data['properties']['latitude'], location.latitude
        )
        self.assertEqual(
            response.data['properties']['longitude'], location.longitude
        )
