from urllib.parse import urlparse


def get_hostname(url):
    parsed_url = urlparse(url)

    return f'{parsed_url.scheme}://{parsed_url.netloc}'
