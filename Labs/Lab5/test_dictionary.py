from unittest import TestCase

from Labs.Lab5.dictionary import Dictionary


class TestDictionary(TestCase):
    def test_query_definition(self):
        d = Dictionary()
        d.load_dictionary('data.json')
        output = d.query_definition('acoustics')
        self.assertEqual(output, ["The science of the production, transmission and effects of sound."])

        output = d.query_definition('acoustis')
        self.assertEqual(output, "Match not Found.\nInstead try: ['acoustics', 'acoustic', 'acost']")
