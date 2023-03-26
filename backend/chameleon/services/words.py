import random
class Words():
    def __init__(self, words_model):
        self.words_model = words_model


    def get_a_word(self):
        all_words = self.words_model.get_words()
        word_obj = random.choice(all_words)
    
        return word_obj['value']