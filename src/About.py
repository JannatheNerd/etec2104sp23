import tornado.web

class AboutPage(tornado.web.RequestHandler):
    def get(self):
        self.write("About my site!")