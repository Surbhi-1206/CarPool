


class IllegalArgumentsException(Exception):

    def __init__(self,*args,**kwargs):
        super(IllegalArgumentsException,self).__init__(self,*args,**kwargs)


# ride data transfer object
class RideDto:

    def __init__(self, start, end, car_num="", user_id="", seats="", email=""):
        if not (start and end):
            raise IllegalArgumentsException('start and end location required')
        self.start = start
        self.end = end
        self.car_num = car_num
        self.seats = seats
        self.email = email
        self.user_id = user_id