from django.test import TestCase

class WeatherView(TestCase):
    def test_weather_call(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)