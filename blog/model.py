import os, os.path
import random
import string
import MySQLdb

import cherrypy
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'server.socket_port': 13004})

def connect(thread_index): 
    # Create a connection and store it in the current thread 
    cherrypy.thread_data.db = MySQLdb.connect('localhost', 'root', '', 'blog') 
 
cherrypy.engine.subscribe('start_thread', connect)
 
class Root: 
    def index(self): 
        # Sample page that displays the number of records in "table" 
        # Open a cursor, using the DB connection for the current thread 
        c = cherrypy.thread_data.db.cursor() 
        c.execute('select * from tbl_news where visible = 0') 
        res = c.fetchone() 
        data = "<table><tr><td>lala</td></tr></table>"
        if res:
           return "<html><body>Hello, you have %d records in your table %s</body></html>" % (res[0],data) 
        c.close() 
        
    index.exposed = True 

cherrypy.quickstart(Root())
