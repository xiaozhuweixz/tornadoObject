import tornado.ioloop
import tornado.web
import  os


PAGE_INDEX = {}
INPUT_INDEX = []
for i in range(1, 100):
    PAGE_INDEX["code"] = "学校"+str(i)
    PAGE_INDEX["age"] = "年龄"+str(i)
    PAGE_INDEX["name"] = "姓名"+str(i)
    PAGE_INDEX["sex"] = "性别"+str(i)
    INPUT_INDEX.append(PAGE_INDEX)


class IndexHandler (tornado.web.RequestHandler):
    def get(self, name):
        print(name)
        page = (int(name)-1) * 5
        cruuer = int(name) * 5
        returnIndex = INPUT_INDEX[page:cruuer]
        aStr = "<a href=%s>%s</a>" %("#","上一页")
        self.render("page/pageIndex.html", inpur_index = returnIndex, aStr=aStr, name=name)

    def post(self,name):
        print(name)
        self.redirect("/index/"+name)

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/'
}




#路由映射
application = tornado.web.Application ([
    ("/index/(?P<name>\d+)", IndexHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
