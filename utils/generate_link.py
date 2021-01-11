import short_url


def generate_short_link(pk: int):
    url = short_url.encode_url(pk)
    return url
