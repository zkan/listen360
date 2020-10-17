from django.test import TestCase

from ..models import Event


class TestEvent(TestCase):
    def test_model_should_have_defined_fields(self):
        Event.objects.create(name='Airflow for CNX!')

        event = Event.objects.last()

        assert event.name == 'Airflow for CNX!'
