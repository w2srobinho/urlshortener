from . import db
from .models import Url, User


def add_url(userid, url):
    """
    Insert url on database with userid (name from owner)
    :param userid: name from owner
    :param url: the address to add
    :return: True, if url added
             None otherwise
    """
    user = User.query.filter_by(name=userid).first()
    if not user:
        return None
    url = Url(address=url, owner=user, hits=0)
    db.session.add(url)
    db.session.commit()
    return {
        'id': url.id,
        'hits': url.hits,
        'url': url.address
    }


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
