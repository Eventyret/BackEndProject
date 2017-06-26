from flask import Flask, render_template
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
app = Flask(__name__)

# Adding MongoDB Connection
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'movies'
COLLECTION_NAME = 'projects'
FIELDS = {
    '_id': True,
    'MovieName': True,
    'Genre1': True,
    'Genre2': True,
    'Genre3': True,
    'Genre4': True,
    'Genre5': True,
    'Genre6': True

}

# For auto Reloading
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
@app.route('/movies')
def movies():
    return render_template('movies.html')
@app.route('/api/data/data.json')
def apidata():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects
if __name__== '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    print "Server Running"
    app.run(debug=True)