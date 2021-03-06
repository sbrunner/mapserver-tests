# -*- coding: utf-8 -*-

import logging
import httplib2
import re
from unittest import TestCase

log = logging.getLogger(__name__)

class TestXML(TestCase):
    url = "http://localhost/mapserv-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&"
#    url = "http://localhost/mapserv603-tests?map=/home/sbrunner/workspace/mapserver-wfs-tests/data/test.map&"
    http = httplib2.Http()
    _re = re.compile("<!-- .* -->")

    def _post(self, body):
#        log.info(self.url)
#        log.info(body)
        response, content = self.http.request(self.url, method='POST', body=body.encode('utf-8'));
        self.assertEquals(int(response['status']), 200)
#        log.info(content)
        return content

    def _get(self, query):
#        log.info(self.url + '&'.join(('%s=%s'%v for v in query)))
        response, content = self.http.request(self.url + \
                '&'.join(('%s=%s' % v for v in query)))
        self.assertEquals(int(response['status']), 200)
#        log.info(content)
        return content

    def _assert_result_equals(self, content, value):
#        log.info(content)
#        log.info(value)
        for test in zip(value.split('\n'),
                unicode(content.decode('utf-8')).split('\n')):
#            log.info(test[0])
#            log.info(test[1])
            if test[0] != 'PASS...':
                self.assertEquals(test[0].strip(), self._re.sub('', test[1]).strip())
