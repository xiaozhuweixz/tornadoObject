import tornado.ioloop
import tornado.web
import  os

class IndexHandler (tornado.web.RequestHandler):
    def get(self):
        self.render("ajax/JqueryAjaxHtml.html")

    def post(self):
        print(self.get_argument("k1"))
        print(self.get_argument("k2"))
        self.write("OK")

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/'
}

#路由映射
application = tornado.web.Application ([
    ("/index", IndexHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

