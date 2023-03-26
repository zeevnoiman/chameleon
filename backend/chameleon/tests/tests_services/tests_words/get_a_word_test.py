from services.words import Words
from db.words_model import Words_model
class Test_get_a_word_test:
    def test_get_a_simple_word(self):
        words_model = Words_model()
        words = Words(words_model=words_model)
        word_result = words.get_a_word()
        assert type(word_result) == str