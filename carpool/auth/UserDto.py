

# TODO: Read about Exception handling
class IllegalArgumentException(Exception):

    def __init__(self, *args, **kwargs):
        super(IllegalArgumentException, self).__init__(self, *args, **kwargs)


# User data transfer object
# TODO: Read about DTOs
class UserDto:

    def __init__(self, email, password="", name="", contact=""):
        if not (email):
            #print("illegal arguments")
            raise IllegalArgumentException('email is required')
        self.email = email
        self.password = password
        self.name = name
        self.contact = contact


