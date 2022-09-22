from django.test import TestCase
from .views import convert_address_to_lat_lon

class TestWeatherView(TestCase):
    def test_weather_call(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class TestLatLonHelper(TestCase):
    def test_lat_lon_failure(self):
        with self.assertRaises(AttributeError):
            _ = convert_address_to_lat_lon('15108 Princewood Lane Land O Lakes Fl 34638')

    def test_lat_lon_success(self):
        lat, lon = convert_address_to_lat_lon('Land O Lakes Fl 34638')
        self.assertTrue(lat is not None)
        self.assertTrue(lon is not None)
