import unittest
from words_list import words

def check_answer(cookie_value_dictionary: dict, answer: str) -> dict:
    '''This function gets cookie value and users's answer, returns cookie value
    with 'count' +1 if the answer is correct, and returns it without changes if
    the answer is uncorrect'''
    count = cookie_value_dictionary['count']
    question = cookie_value_dictionary['question']
    values = []
    for value in words.values():
        values.append(value)
    if answer == values[question][1]:
        count += 1
    cookie_value_dictionary['count'] = count
    return cookie_value_dictionary


class TestCookieFunctions(unittest.TestCase):

    def test_check_answer(self):
        cookie_value_dictionary = {'state': 'words', 'count': 0, 'question': 1}
        answer = 'разность'
        values = []
        for value in words.values():
            values.append(value)  
        result = check_answer(cookie_value_dictionary, answer)
        self.assertEqual(result, {'state': 'words', 'count': 0, 'question': 1})


if __name__ == '__main__':
    unittest.main()
    