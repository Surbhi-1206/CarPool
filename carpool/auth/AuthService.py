from carpool.auth.AuthRepository import AuthRespository


class UserExistsException(Exception):

    def __init__(self, *args, **kwargs):
        super(UserExistsException, self).__init__(self, *args, **kwargs)


class InvalidUserException(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidUserException, self).__init__(self, *args, **kwargs)


class AuthService:

    auth_repository = AuthRespository()
    def create_user(self, user_dto):
        """
        creates a new user
        :param user_dto:
        :return:
        """
        user = self.auth_repository.get_user(user_dto)
        if user is None:
            print("Creating new User")
            self.auth_repository.create_user(user_dto)
        else:
            raise UserExistsException()


    def load_user(self, user_dto):
        """
        loads an existing user
        :param user_dto:
        :return: user object
        """
        user = self.auth_repository.get_user(user_dto)
        if user:
            #print (user.email , user.id)
            return user
        raise InvalidUserException('User does not exist')


