from chameleon.db.words_model import Words_model
from chameleon.services.words import Words
from chameleon.db.connection import dbConnector

words_model = Words_model()
db = dbConnector()
words = Words(words_model=words_model)