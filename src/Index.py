import tornado.web
import datetime

current_time = datetime.datetime.now()
day = current_time.strftime("%d")
year = current_time.strftime("%Y")
month = current_time.strftime("%m")
clock_time = current_time.strftime("%H:%M:%S")

date_and_time = "It is " + month + "/" + day + "/" + year + " at " + clock_time +"\n"

class IndexPage(tornado.web.RequestHandler):
    def get(self):
        self.write(date_and_time)

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/quote">Get a quote</a>')