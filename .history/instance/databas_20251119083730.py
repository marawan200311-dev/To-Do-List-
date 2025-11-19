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
   cursor.execute('INSERT INTO user_assignment (assignment,date) VALUES(?,?)', (assignment,date))
   connect.commit()
   connect.close()

def show_up():
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()
  schedule=[]
  cursor.execute('SELECT * FROM user_assignment')
  all_date = 





initialise_data()