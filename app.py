from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
# Adding Mysql Connection
app.config['MYSQL_DATABASE_USER'] = 'exam'
app.config['MYSQL_DATABASE_PASSWORD'] = 'exam123'
app.config['MYSQL_DATABASE_DB'] = 'exam'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# For auto Reloading
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/overview')
def overview():
    return render_template('overview.html')
@app.route('/movie')
def movie():
    return render_template('movie.html')
if __name__== '__main__':
    app.run(debug=True)