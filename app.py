from flask import Flask, render_template ,url_for

app= Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/add_page')
def add_page():
    return render_template('add.html')  


@app.route('/delete_page') 
def delete_page():
    return render_template('delete.html')
@app.route('/update_page')
def update_index():
    return render_template('update.html')

@app.route('/show_page')
def show_page():
    return render_template('update.html')



if __name__=="__main__":
      app.run(debug=True)

