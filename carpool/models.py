from carpool import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    contact = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, contact, password):
        self.name = name
        self.email = email
        self.contact = contact
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)


class Rides(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    start = db.Column(db.String(100))
    end = db.Column(db.String(100))
    car_num = db.Column(db.String(100))
    seats = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, email, start, end, car_num, seats, user_id):
        self.email = email
        self.start = start
        self.end = end
        self.car_num = car_num
        self.seats = seats
        self.user_id = user_id

    def __repr__(self):
        return '<Service %r>' % self.email


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rider = db.Column(db.String(100))
    owner = db.Column(db.String(100))
    ride_id = db.Column(db.Integer, db.ForeignKey('rides.id'))
    pickup = db.Column(db.String(100))
    drop = db.Column(db.String(100))
    status = db.Column(db.String(100))

    def __init__(self, rider, owner, ride_id, pickup, drop, status):
        self.rider = rider
        self.owner = owner
        self.ride_id = ride_id
        self.pickup = pickup
        self.drop = drop
        self.status = status
