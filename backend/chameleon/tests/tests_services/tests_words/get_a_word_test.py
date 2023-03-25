from services.words import Words

class Test_get_a_word_test:
    def test_get_a_simple_word(self):
        print("hello")
        words = Words()
        word_result = words.get_a_word()
        assert word_result == "example1"