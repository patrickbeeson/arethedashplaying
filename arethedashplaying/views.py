from datetime import datetime
from datetime import date
from pytz import timezone

from flask import flash, render_template

from . import app
from .models import Game


@app.route('/')
def index():
    # Define our date variables
    now_utc = datetime.now(timezone('UTC'))
    now_eastern = now_utc.astimezone(timezone('US/Eastern'))
    season_end_date = date(2014, 9, 01)

    #Get all games, ordered by date, then filter for those greater than
    #or equal to the current date. We only need the first item in the query.
    game = Game.query.order_by(Game.date).filter(
        Game.date >= now_eastern.date()).first()
    last_game = Game.query.filter(Game.date == date(2014, 9, 01))
    # Get only upcoming games
    upcoming_games = Game.query.order_by(
        Game.date).filter(
        Game.date >= now_eastern.date(), Game.date <= season_end_date).all()

    # If there are upcoming games, proceed with messages on the home template.
    if upcoming_games:
        if game.date == now_eastern.date():
            flash('YES')
        else:
            flash('NO')
        return render_template('home.html', game=game, last_game=last_game)
    # Show the no upcoming games template if the season has ended
    elif now_eastern.date() == season_end_date:
        flash('NO')
        return render_template('no_upcoming_games.html')
    # Show that we're missing data with unique template
    else:
        return render_template('missing_data.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
