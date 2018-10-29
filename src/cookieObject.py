import tornado.ioloop
import tornado.web
import  os
import time

class IndexHandler (tornado.web.RequestHandler):
    def get(self):

        self.render(os.path.join('cookieFile/index.html'))


class LongInHandler (tornado.web.RequestHandler):
    def get(self):
        self.render(os.path.join('cookieFile/login.html'))

    def post(self, *args, **kwargs):
        nameUser = self.get_argument("username")
        pwd = self.get_argument("pwd")
        if nameUser == 'cxw' and pwd == '123':
            times = time.time() + 10
            self.set_cookie('auth', '1', expires=times)
            self.redirect(os.path.join('/manager'))
        else:
            self.redirect('/longIn')

class ManagerHandler (tornado.web.RequestHandler):

    def get(self):
        auth = self.get_cookie('auth')
        if auth:
            self.render(os.path.join('cookieFile/manager.html'))
        else:
            self.redirect('/longIn')




class LongOutHandler (tornado.web.RequestHandler):
    def get(self):
        self.set_cookie('auth', 0, time.time())
        self.redirect('/longIn')


settings = {
    'template_path': 'template',
}

#路由映射
application = tornado.web.Application ([
    ("/index", IndexHandler),
    ("/manager", ManagerHandler),
    ("/longIn", LongInHandler),
    ("/longOut", LongOutHandler)

], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

