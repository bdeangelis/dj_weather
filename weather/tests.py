import json
from django.test import TestCase
from .forms import is_united_states, GetWeather
from django.forms import ValidationError
from .views import get_forecast, GetWeather
from unittest.mock import patch


class TestWeatherView(TestCase):
    def test_weather_call(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class TestFormHelper(TestCase):
    def test_country_not_us(self):
        """ "
        GIVEN country choice is not United States
        WHEN country validation executes
        THEN ValidationError is raised
        """
        with self.assertRaises(ValidationError):
            _ = is_united_states("other")


class TestForm(TestCase):
    def test_form_passing(self):
        """
        GIVEN all data available in the form
        WHEN validation occurs
        THEN form is valid
        """
        form = GetWeather(
            {
                "address": "15108 Princewood Lane",
                "city": "Land O Lakes",
                "state": "FL",
                "zip": "34638",
                "country": "United States",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_fail_country(self):
        """
        GIVEN all data available in the form but country is not United States
        WHEN validation occurs
        THEN form is not valid
        """
        form = GetWeather(
            {
                "address": "15108 Princewood Lane",
                "city": "Land O Lakes",
                "state": "FL",
                "zip": "34638",
                "country": "other",
            }
        )
        self.assertFalse(form.is_valid())


class TestGetForecast(TestCase):
    @patch("weather.views.requests")
    def test_forecast_returned(self, mock_request):
        """
        GIVEN request is sent to 3rd party
        WHEN date values are inlcuded
        THEN forecast object is returned
        Mock out the actual request, don't call to the third party in test
        """
        mock_request.return_value = json.dumps({"test": "one"})
        _ = get_forecast("123 Main Street", "Tulsa", "OK", "74011", "United States")
        self.assertTrue(mock_request.called_once())


class TestUSForecast(TestCase):
    @patch("weather.views.requests")
    def test_post_get_us_forecast(self, mock_request):
        """
        GIVEN form is submitted with address
        WHEN 3rd party is called
        THEN forecast response is returned
        """
        mock_request.return_value = json.dumps({"test": "one"})
        form_dict = {
            "address": "15108 Princewood Lane",
            "city": "Land O Lakes",
            "state": "FL",
            "zip": "34638",
            "country": "United States",
        }
        response = self.client.post(path="", data=form_dict)
        self.assertTrue(mock_request.called_once())
        self.assertEqual(response.status_code, 200)
