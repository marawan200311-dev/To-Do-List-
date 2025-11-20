import sqlite3
import os

def initialise_data():
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS user_assignment( id INTEGER PRIMARY KEY AUTOINCREMENT,
  assignment TEXT NOT NULL ,
data TEXT )
''')





def add_data(assignment,data):
   connect = sqlite3.connect('data.db')
   cursor= connect.cursor()
   cursor.execute('INSERT INTO user_assignment (assignment,data) VALUES(?,?)', (assignment,data))
   connect.commit()
   connect.close()

def show_up():
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()
 
  cursor.execute('SELECT * FROM user_assignment')
  all_date = cursor.fetchall()

  schedule=[]
  for data in all_date:
    schedule.append(f'{data[0]}. Your mession {data[1]} You decided to do that in this time==>{data[2]}')
  if len(schedule)==0 :
    print('The user does not add anything :)')
  return schedule


def delete (assignmentNumber):
  connect = sqlite3.connect('data.db')
  cursor= connect.cursor()

  cursor.execute('SELECT * FROM user_assignment WHERE id=?', (assignmentNumber,))
  row= cursor.fetchone()
  if row is None:
   return f"This {row} doesn't valid "
  cursor.execute('DELETE FROM user_assignment WHERE id = ? ', (assignmentNumber,))
  connect.commit()
  connect.close()
  return f"This mission has been deleted successfully!"
  


 




    

  






initialise_data()