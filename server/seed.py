import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server.app import create_app, db
from server.models import User, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    user = User(username="testuser")
    user.set_password("testpass")
    db.session.add(user)

    guest = Guest(name="Tom Hanks", occupation="Actor")
    db.session.add(guest)

    from datetime import date
    episode = Episode(date=date(2023, 1, 1), number=1)
    db.session.add(episode)

    db.session.commit()