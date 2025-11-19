import sqlite3
import os

def initialise_data():
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS user_assignment( id INTEGER PRIMARY KEY AUTOINCREMENT,
  assignment TEXT NOT NULL ,
dat TEXT )
''')





def add_data(assignment,dat):
   connect = sqlite3.connect('data.db')
   cursor= connect.cursor()
   cursor.execute('INSERT INTO user_assignment (assignment,dat) VALUES(?,?)', (assignment,dat))
   connect.commit()
   connect.close()

def show_up():
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()
 
  cursor.execute('SELECT * FROM user_assignment')
  all_date = cursor.fetchall()

  schedule=[]
  empty_schedule=[]
  for dat in all_date:
    schedule.append(f'{dat[0]}. Your mession {dat[1]} You decided to do that in that time==>{dat[2]}')
  if schedule is None:
    empty_schedule.append('YOU HAVE NOT ADD IT ANY THING YET!:)')
    
    

  






initialise_data()