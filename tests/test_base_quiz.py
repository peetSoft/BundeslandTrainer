from unittest import TestCase
from sources.base_quiz import Quiz


class TestQuiz(TestCase):
    def test_get_canonic(self):
        quiz = Quiz({}, None, None, {"Nrw":"Nordrhein-Westfalen"}, None)
        test_data = [
            ('sdfg--  sdfg   cwerg-etrzh', "Sdfg-Sdfg-Cwerg-Etrzh" ),
            ("berlin","Berlin"),
            ("Nrw", "Nordrhein-Westfalen"),
            ("nrw", "Nordrhein-Westfalen")
        ]
        for text, canonic in test_data:
            TestCase.assertEqual(self, quiz.get_canonic(text), canonic)
