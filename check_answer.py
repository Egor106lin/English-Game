import unittest
from words_list import english_excercices, answers_eng_keys


def check_answer(question: int, answer: str, answers: dict, exerscices: list[dict[list]]) -> bool:
    '''This function gets cookie value and users's answer, returns cookie value
    with 'count' +1 if the answer is correct, and returns it without changes if
    the answer is incorrect'''
    eng_answer = next(iter(exerscices[question]))
    return answers[eng_answer] == answer
    

class TestCookieFunctions(unittest.TestCase):

    def test_check_answer_correct_answer(self):
        question = 1
        answer = 'сумма'
        answers = answers_eng_keys
        exerscices = english_excercices
        result = check_answer(question, answer, answers, exerscices)
        self.assertTrue(result)

    def test_check_answer_incorrect_answer(self):
        question = 1
        answer = 'слон'
        answers = answers_eng_keys
        exerscices = english_excercices
        result = check_answer(question, answer, answers, exerscices)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
    