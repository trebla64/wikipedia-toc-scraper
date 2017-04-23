from pyramid.view import view_config
import urllib3
import re
import rfc3987
from lxml import etree


def get_domain(page_url):
    d = rfc3987.parse(page_url, rule='URI')
    return d['authority']

def test_page(page_url):
    http = urllib3.PoolManager()
    r = http.request('GET', page_url)
    return r.status

@view_config(route_name='toc', renderer='templates/toc.jinja2')
def toc_view(request):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    domain   = 'Invalid'
    res      = 404
    is_valid = False
    page_url = request.GET.get('page_url', '')
    m = regex.match(page_url)
    if m:
        domain = get_domain(page_url)
        is_valid = True
    else:
        page_url = 'https://' + page_url
        if regex.match(page_url):
            domain = get_domain(page_url)
            is_valid = True

    # If the URL was found to be valid, ensure that the domain name contains 'wikipedia.org'
    if is_valid:
        domain_regex = re.compile(r'^.*?wikipedia\.org$', re.IGNORECASE)
        if domain_regex.match(domain):
            http = urllib3.PoolManager()
            r = http.request('GET', page_url)
            output = ''
            if r.status == 200:
                root = etree.fromstring(r.data.decode('utf-8'))
                toc = root.find('.//div[@id="toc"]')
                output = etree.tostring(toc)

            return {'protocol': 'See code', 'domain': domain, 'res': r.status, 'code': output.decode('utf-8')}
        else:
            return {'protocol': 'N/A', 'domain': "Doesn't contain 'wikipedia.org'", 'res': 404}

    return {'protocol': 'N/A', 'domain': 'N/A', 'res': 404}

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'wikipedia-toc-scraper'}
