

class IllegalArgumentsException(Exception):

    def __init__(self,*args,**kwargs):
        super(IllegalArgumentsException,self).__init__(self,*args,**kwargs)


# ride data transfer object
class BookingDto:

    def __init__(self, owner="", pickup="", drop="", rider="", ride_id="", status="pending"):
        #if not (owner):
         #   raise IllegalArgumentsException('Rider email required')
        self.rider = rider
        self.pickup = pickup
        self.drop = drop
        self.owner = owner
        self.ride_id = ride_id
        self.status = status
