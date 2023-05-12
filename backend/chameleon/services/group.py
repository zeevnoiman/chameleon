import random
import string

class Groups:

    def create_group(self):
        letters = string.ascii_lowercase
        group_id = ''.join(random.choice(letters) for i in range(5))
        print(group_id)
        return group_id