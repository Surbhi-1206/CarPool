from carpool import models, db
from flask_sqlalchemy import SQLAlchemy


# This class performs database CRUD operations

class AuthRespository:

    def get_user(self, user_dto):
        """
        Fetches the user from the db using his email
        :param user_dto:
        :returns: user
        """
        user = models.Users.query.filter_by(email=user_dto.email).first()
        # print (user.email)
        return user

    def create_user(self, user_dto):
        """
        Creates a user of the system
        :param user_dto:
        """
        print(user_dto.name)
        print(user_dto.email)
        print(user_dto.contact)
        print(user_dto.password)
        user = models.Users(user_dto.name, user_dto.email, user_dto.contact, user_dto.password)
        db.session.add(user)
        db.session.commit()
