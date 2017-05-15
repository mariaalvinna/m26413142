import cherrypy
import random
import string

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update('server.conf')

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        #return "Good morning, class! from string generator"
         return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""
    @cherrypy.expose
    def generate(self, length=18):
        mystring = "".join(random.sample(string.hexdigits,int(length)))
        cherrypy.session['astring']=mystring
        return mystring 
    @cherrypy.expose
    def display(self):
        return cherrypy.session['astring']

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator(),'/', 'app.conf')

