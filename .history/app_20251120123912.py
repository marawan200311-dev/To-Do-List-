from flask import Flask, render_template ,url_for,request,redirect
import sqlite3 
import os
db_py=os.path.join(os.path.dirname(__file__),'instance', 'data.db')
from instance.databas import initialise_data, add_data, show_up,delete




app= Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
#_____________ADD_______________
@app.route('/add_page')
def add_page():
    return render_template('add.html')  

@app.route('/add_assignment' ,methods=['POST'])
def assignment ():
   assignment=request.form['assignment']
   date= request.form['date']
   add_data(assignment,date)
   return render_template('add.html')

@app.route('/skip')
def skip ():
   return redirect('/')
#__________________________________

#_____________DELETE______________
@app.route('/delete_page') 
def delete_page():
    return render_template('delete.html')
def show_page():
    data=show_up()
    return render_template('show.html', schedule=data)
@app.route('/skip_show')

@app.route("/delet_form", methods=['POST'])
def delete_mission():
    id_of_mission=int(request.form['number'])
    delete(id_of_mission)
    return render_template('delete.html',id_of_mission=id_of_mission)

@app.route('/skip_delete')
def skip_delete():
   return redirect('/')

#___________________________________________

#__________UPDATE_____________________
@app.route('/update_page')
def update_index():
    return render_template('update.html')
#__________________________________________

#________SHOW_________________
@app.route('/show_page')
def show_page():
    data=show_up()
    return render_template('show.html', schedule=data)
@app.route('/skip_show')
def skip_show():
    return redirect('/')


if __name__=="__main__":
      app.run(debug=True)

