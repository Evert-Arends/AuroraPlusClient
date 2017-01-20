import random
import string

from bin import encode
import uuid
import communication
Communication = communication.Communication()


class Register:
    def __init__(self):
        print 'Registering...'

    def register_agent(self):
        key = self.create_key()
        check = self.check_if_key_is_unique(key=key)
        if not check:
            print 'This key appears not to be an unique key.'
            return
        return key

    @staticmethod
    def create_key():
        # key = uuid.uuid4()
        key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(35))
        return key

    @staticmethod
    def check_if_key_is_unique(key):
        check = Communication.check_if_key_is_unique(key=key)
        if not check:
            return

        return True

if __name__ == '__main__':
    Register = Register()
    Register.register_agent()

