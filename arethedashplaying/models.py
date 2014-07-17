from . import db

class Game(db.Model):
    """ A game being played by the Dash """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    ticket_url = db.Column(db.String(250))
    is_away = db.Column(db.Boolean)

    opponent_id = db.Column(db.Integer, db.ForeignKey('opponent.id'))
    opponent = db.relationship('Opponent', backref=db.backref('games', lazy='dynamic'))

    def __init__(self, opponent, date, time, ticket_url, is_away):
        self.opponent = opponent
        self.date = date
        self.time = time
        self.ticket_url = ticket_url
        self.is_away = is_away

    def __repr__(self):
        return '<Game %r>' % self.opponent


class Opponent(db.Model):
    """ And opponent being played by the Dash """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Opponent %r>' % self.name
