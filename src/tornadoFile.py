import tornado.ioloop
import tornado.web
import  os


INPUT_LIST = {'longInFlage': None}

MESSAGE_INFO = [
    {'tetile':'12133123123', 'textConte': '2312321312', 'bz': '1212'},
    {'tetile':'33333333333', 'textConte': '4444444444', 'bz': '121212321'}
]

SEND_MESSAGE_INFO = {

}


class MainHandler (tornado.web.RequestHandler):
    def get(self):
        INPUT_LIST['longInFlage'] = None
        self.render(os.path.join('index.html'), user_info=INPUT_LIST, message_info=MESSAGE_INFO)

class LonginHandler (tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        name = self.get_argument("name")
        pwd = self.get_argument("pwd")
        if name == "cxw" and pwd == "123":
            INPUT_LIST['longInFlage'] = True
            INPUT_LIST['name'] = name
            self.render(os.path.join("index.html"), user_info=INPUT_LIST, message_info=MESSAGE_INFO)

        self.redirect("/index")

class PublicMessageHandler (tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render(os.path.join("sendMessage.html"), user_info=INPUT_LIST, message_info=MESSAGE_INFO)

    def post(self, *args, **kwargs):
        tetile = self.get_argument("tetile")
        textConte = self.get_argument("textConte")
        bz = self.get_argument("bz")
        SEND_MESSAGE_INFO['tetile'] = tetile
        SEND_MESSAGE_INFO['textConte'] = textConte
        SEND_MESSAGE_INFO['bz'] = bz
        MESSAGE_INFO.append(SEND_MESSAGE_INFO)
        self.render(os.path.join("index.html"), user_info=INPUT_LIST, message_info=MESSAGE_INFO)
settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/'
}

#路由映射
application = tornado.web.Application ([
    ("/index", MainHandler),
    ("/longIn", LonginHandler),
    ("/publicMessage", PublicMessageHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

