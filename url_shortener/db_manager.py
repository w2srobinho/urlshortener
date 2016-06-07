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


def add_url(user_id, url, host):
    """
    Insert url on database with user_id (name from owner)
    :param user_id: name from owner
    :param url: the address to add
    :return: True, if url added
             None otherwise
    """
    user = User.query.filter_by(name=user_id).first()
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


def add_user(user_id):
    """
    Insert user on database, user_id is the name from user
    :param user_id: name from user
    """
    user_found = User.query.filter_by(name=user_id).first()
    if user_found:
        return None
    user = User(name=user_id)
    db.session.add(user)
    db.session.commit()
    return {'id': user.name}


def _generate_statistics(urls, host):
    """
    Generate statistics of system
    :param urls: list of urls to generate the statistics
    :host: name of host from server
    :return: a dictionary with the statistics
    """
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

    return {
        'hits': total_hits,
        'urlCount': len(urls),
        'topUrls': top10
    }


def generate_user_statistics(user_id, host):
    """
    Generate statistics for a specific user
    :param user_id:
    :param host: name of host from server
    :return: a dictionary with the user statistics
    """
    user_found = User.query.filter_by(name=user_id).first()
    if not user_found:
        return None
    urls = Url.query.filter_by(owner_id=user_found.id).all()
    return _generate_statistics(urls, host)


def generate_global_statistics(host):
    """
    Generate statistics of all system
    :param host: name of host from server
    :return: a dictionary with the global statistics
    """
    urls = Url.query.order_by(Url.hits.desc()).all()
    return _generate_statistics(urls, host)


def generate_url_statistics(hash_code, host):
    """
    Generate statistics for a specific url
    :param host: name of host from server
    :return: a dictionary with the specific url statistics
    """
    id = decode(hash_code)
    url = Url.query.filter_by(id=id).first()
    if not url:
        return None
    return {
        "id": url.id,
        "hits": url.hits,
        "url": url.address,
        "shortUrl": encode(url.id)
    }


def remove_url(hash_code):
    """
    Remove a specific url by id
    :param hash_code: encoded id from url
    :return: None, if there some error
    """
    id = decode(hash_code)
    url = Url.query.filter_by(id=id).first()
    if not url:
        return None
    db.session.delete(url)
    db.session.commit()
    return True
