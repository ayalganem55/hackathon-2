from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    fullname = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    teamId = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    #meetings = db.relationship('Meeting', backref='who_booked', lazy='dynamic')


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    teamName = db.Column(db.String(64), nullable=False,unique=True)
    members = db.relationship('User',backref='team',lazy='dynamic')
    #meetings=db.relationship('Meeting',backref='team',lazy='dynamic')

    def __repr__(self):
        return f'<Team {self.teamName}>'


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(64),nullable=False,unique=True)
    #teamId = db.Column(db.Integer, db.ForeignKey('team.id'))
    #roomId = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    #bookerId = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime,nullable=False)
    startTime = db.Column(db.Integer,nullable=False)
    endTime = db.Column(db.Integer,nullable=False) # should be calculated with startTime and duration
    duration = db.Column(db.Integer,nullable=False)
    #cost=db.Column(db.Integer,nullable=False)
    #participant_users=db.relationship('Participants_user',backref='meeting')
    #participant_partners=db.relationship('Participants_partner',backref='meeting')

    def __repr__(self):
        return f'Meeting {self.id} for {self.id} last for {self.duration}'


