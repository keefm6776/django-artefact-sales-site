from django.test import TestCase
from .models import Artefact

# Create your tests here.

class ArtefactTests(TestCase):
    """ Tests to run against our Artefact Models """

    def test_era_ok(self):
        test_era = Artefact(era='AD')
        self.assertEqual(str(test_era), 'AD')

    def test_name_ok(self):
        test_name = Artefact(name='The Holy Grail')
        self.assertEqual(str(test_name), 'The Holy Grail')

    def test_description_ok(self):
        test_description = Artefact(description='Really Old')
        self.assertEqual(str(test_description), 'Really Old')



