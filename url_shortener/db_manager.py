from . import db
from .models import User


def add_user(userid):
    """
    Insert user on database, userid is the name from user
    :param userid: name from user
    """
    user_found = User.query.filter_by(name=userid).first()
    if user_found:
        return None
    user = User(name=userid)
    db.session.add(user)
    db.session.commit()
    return {'id': user.name}

