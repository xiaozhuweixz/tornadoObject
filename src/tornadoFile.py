import tornado.ioloop
import tornado.web
import  os


INPUT_LIST = []

class MainHandler (tornado.web.RequestHandler):
    def get(self):

        #self.write("Hello, world")

        self.render(os.path.join('s2.html'), xxx=INPUT_LIST)
    def post(self, *args, **kwargs):
        data = self.get_argument("xxx")
        INPUT_LIST.append(data)
        self.render(os.path.join('s2.html'), xxx=INPUT_LIST)

settings = {
    'template_path': 'template/test'
}


#路由映射
application = tornado.web.Application ([
    ("/index", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()