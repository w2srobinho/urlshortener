from . import db
from .codefy import decode, encode
from .models import Url, User


def find_url(hash_code):
    """
    Find url on database, decode hash_code using decode function to take the id
    :param hash_code: the encoded code of url
    :return: the url address, if found in database
             None otherwise
    """
    id = decode(hash_code)
    url = Url.query.filter_by(id=id).first()
    if not url:
        return None
    url.hits += 1
    db.session.commit()
    return url.address


def add_url(userid, url, host):
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
        'url': url.address,
        'shortUrl': '{}/{}'.format(host, encode(url.id))
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


def generate_global_statistics(host):
    """
    Generate state of all system
    :return: a dictionary with the global statistics
    """
    urls = Url.query.order_by(Url.hits.desc()).all()
    total_hits = sum(url.hits for url in urls)  # sum all hits
    # Generate a list with top10 using python list comprehensions
    top10 = [
        {
            'id': url.id,
            'hits': url.hits,
            'url': url.address,
            'shortUrl': '{}/{}'.format(host, encode(url.id))
        }
        for url in urls[:10]
        ]

    return {'hits': total_hits,
            'urlCount': len(urls),
            'topUrls': top10}
