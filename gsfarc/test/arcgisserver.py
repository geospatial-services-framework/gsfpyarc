"""

"""
try:
    from urllib.parse import urlparse, urlunparse, urlencode
    from urllib.request import urlopen, Request
except ImportError:
    from urlparse import urlparse, urljoin, urlunparse
    from urllib import urlencode
    from urllib2 import urlopen, Request

import json


class ArcGISServer(object):
    """Uses the server's rest spec for user and admin services."""
    def __init__(self, site_url, username=None, password=None):
        """Initializes REST connection to the arcgis server"""
        self.site_url = self.normalize_url(site_url)
        self.username = username
        self.password = password
        self.referer = 'http://www.harrisgeospatial.com'
        self.token = None
        self.admin_token = None

        self.info = self._http_get('rest/info')

        if self.username:
            self._generate_admin_token()

    def normalize_url(self, site_url):
        """
        Takes the input url and adds a protocol if one does not exits.
        Normalizes the path to just the site folder. e.g.
        http://server:port/<site>
        :param site_url:
        :return: The normalized url
        """

        # Add protocol if one does not exist
        if ('http://' not in site_url.lower() and
                'https://' not in site_url.lower()):
            site_url = ''.join(('http://', site_url))

        parsed_url = urlparse(site_url)
        split_path = parsed_url.path.split('/')
        # The first element is always empty from the leading /
        split_path.pop(0)
        if len(split_path) == 0:
            split_path.append('arcgis')

        site_url = urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            split_path[0],
            None,
            None,
            None
        ))

        return site_url
    
    def delete_service(self, service_name, service_type):
        """

        :param service_name:
        :return:
        """
        service = '.'.join((service_name, service_type))
        path = '/'.join(('admin', 'services', service, 'delete'))
        return self._http_post(path, admin=True)

    def _http_get(self, path, query={}, admin=False):
        query['f'] = 'json'
        data = urlencode(query)
        headers = {
            'Referer': self.referer
        }

        url = '/'.join((self.site_url, path))
        url = '?'.join((url, data))
        req = Request(url, headers=headers)
        resp = urlopen(req).read().decode('utf-8')
        return json.loads(resp)

    def _http_post(self, path, query={}, admin=False):
        query['f'] = 'json'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': self.referer
        }

        if admin and self.admin_token:
            query['token'] = self.admin_token

        data = urlencode(query).encode('utf-8')
        url = '/'.join((self.site_url, path))
        req = Request(url, data, headers)
        resp = urlopen(req).read().decode('utf-8')
        return json.loads(resp)

    def _generate_admin_token(self):
        """

        :return: The generated token
        """

        if not self.username or not self.password:
            return ''

        generate_token_path = 'admin/generateToken'
        query = {
            'client': 'referer',
            'referer': self.referer,
            'username': self.username,
            'password': self.password
        }

        resp = self._http_post(generate_token_path, query)
        self.admin_token = resp['token']