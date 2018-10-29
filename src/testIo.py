#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from tornado import httpclient
from tornado.web import asynchronous
from tornado import gen



class MainHandler(tornado.web.RequestHandler):
        @asynchronous
        @gen.coroutine
        def get(self):
            print('start get')
            http = httpclient.AsyncHTTPClient()
            http.fetch("www.baidu.com", self.callback)
            self.write('end')

        def callback(self, response):
            print('hello word')
            self.get_cookie()

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/'
}

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

