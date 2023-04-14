import random
import string

class Groups:

    def create_group(self):
        letters = string.ascii_lowercase
        print ( ''.join(random.choice(letters) for i in range(5)) )