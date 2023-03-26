from pathlib import Path
import json

class Words_model:
    def __init__(self):
        self.path_to_db = Path(__file__).parent.joinpath('words.json').resolve()

    def get_words(self):
        f = open (self.path_to_db, "r")
        data = json.loads(f.read())
        return data
