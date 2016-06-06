from . import ALPHA_NUMERIC_RANGE


def encode(id):
    """
    Create a code based on id parameter
    :param id: int param to generate code
    :return: string hash code to use on url
    """
    if not id:
        return ALPHA_NUMERIC_RANGE[0]

    hash_code = ''
    while id:
        id, r = divmod(id, len(ALPHA_NUMERIC_RANGE))
        hash_code += ALPHA_NUMERIC_RANGE[r]
    return hash_code

def decode(hash_code):
    """
    Inverse of encode function
    recover id using code parameter
    :param hash_code: string to decode on id
    :return: id to url
    """
    id = 0
    while hash_code:
        id = id * len(ALPHA_NUMERIC_RANGE) + ALPHA_NUMERIC_RANGE.find(hash_code[-1])
        hash_code = hash_code[:-1]
    return id
