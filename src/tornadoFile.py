import tornado.ioloop
import tornado.web
import  os


INPUT_LIST = {'longInFlage': None}

class MainHandler (tornado.web.RequestHandler):
    def get(self):
        INPUT_LIST['longInFlage'] = None
        self.render(os.path.join('index.html'), user_info=INPUT_LIST)

class LonginHandler (tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        name = self.get_argument("name")
        pwd = self.get_argument("pwd")
        if name == "cxw" and pwd == "123":
            INPUT_LIST['longInFlage'] = True
            INPUT_LIST['name'] = name
            self.render(os.path.join("index.html"), user_info=INPUT_LIST)

        self.redirect("/index")

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/'
}

#路由映射
application = tornado.web.Application ([
    ("/index", MainHandler),
    ("/longIn", LonginHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

