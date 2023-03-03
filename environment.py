import os
import threading 
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Framework import app

#CHROME_DRIVER=os.path.join(os.path.join(os.path.join.dirname(__file__),'driver'),'chromedriver')
CHROME_DRIVER=os.path.join(os.path.dirname(os.path.abspath(__file__)),'driver','chromedriver')


chrome_options=Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")

def before_all(context):
  context.server = simple_server.WSGIServer(("",5000),WSGIRequestHandler)
  context.server.set_app(app)
  context.pa_app=threading.Thread(target=context.server.server_forever)
  context.pa_app.start()

def after_all(context):
  context.browser.quit()
  context.server.shutdown()
  context.pa_app.join()