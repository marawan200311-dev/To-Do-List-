import sqlite3
import os

def initialise_data():
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS user_assignment( id INTEGER PRIMARY KEY AUTOINCREMENT,
  assignment TEXT NOT NULL ,
date TEXT )
''')





def add_data(assignment,date):
   connect = sqlite3.connect('data.db')
   cursor= connect.cursor()
   cursor.execute('INSERT INTO user_assignment (id,assignment,date) VALUES(?,?)', (assignment,date))
   connect.commit()
   connect.close()

#EmptyDataError doesnot Not included in python 

class EmptyDataError(Exception):
   @staticmethod
   def show_up():
      result=[]
      connect= None #>> if something wrong happens when we connecting so we are literally off
      try:
         connect=sqlite3.connect('data.db')
         cursor=connect.cursor()
         cursor.execute('SELECT * FROM user_assignment')
         rows= cursor.fetchall()
         
         
         if not rows:
            raise EmptyDataError("YOU HAVE NOT ADD IT ANY THING YET :)?")
         
         
         for row in rows:
            result.append(f"{row[0]}.{row[1]} You determined to do that in==> {row[2]}")
         
      #until the programmer understand the mistake from where exactly 
      # except EmptyDataError as e :
      #    result =[]
      #    print('The user did not add anything')
      #    raise e 
      finally:
         if connect:
            connect.close()




initialise_data()