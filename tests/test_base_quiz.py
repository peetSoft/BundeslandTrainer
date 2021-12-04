from unittest import TestCase
from sources.base_quiz import Quiz


class TestQuiz(TestCase):
    def test_get_canonic(self):
        quiz = Quiz({}, None, None, {}, None)
        v = quiz.get_canonic('sdfg--  sdfg   cwerg-etrzh')
        TestCase.assertEqual(self, v, "Sdfg-Sdfg-Cwerg-Etrzh")

        v = quiz.get_canonic("berlin")
        TestCase.assertEqual(self, v, "Berlin")