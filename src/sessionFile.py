import tornado.ioloop
import tornado.web
import  os

Session={}

class IndexHandler (tornado.web.RequestHandler):
    def get(self):
        self.render("session/sessionHtml.html")
    def post(self):
        self.write("OK")


class LonginHandler (tornado.web.RequestHandler):
    def get(self):

        self.render("session/sessionHtml.html")
    def post(self):

        userName = self.get_argument("userName")
        pwd = self.get_argument("pwd")
        if userName in ["cxw","ly"]:
            Session[userName] = {}
            Session[userName]["LongFlage"] = True
            Session[userName]["userName"] = userName
            Session[userName]["pwd"] = "123"
            self.set_cookie("userName", userName)
            self.write("/longIn")
        else:
            self.render("session/sessionHtml.html")

class magageHandler (tornado.web.RequestHandler):
    def get(self):
        Seesion_dic = self.get_cookie("userName");
        str = Session[Seesion_dic]
        self.render("session/sessionHtml.html")
    def post(self):
        self.write("OK")
settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/'
}

#路由映射
application = tornado.web.Application ([
    ("/index", IndexHandler),
    ("/longIn", LonginHandler),
    ("/magage", magageHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
