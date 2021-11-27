from unittest import TestCase
import base_quiz


class Test(TestCase):
    def test_quiz(self):
        quiz = base_quiz.Quiz(
            {'q1': 'a1', 'q2': 'a2', 'q3': 'a3'},
            'A', 'Q',
            {'qq': 'q'},
            {'q1': 'q1 mnem'}
        )
        next = quiz.next_question()
        pass
