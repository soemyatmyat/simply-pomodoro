from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS 
import logging
import uuid

app = Flask(__name__) # Create an instance of Flask
app.config.from_pyfile("settings.py") # load environment variables 
CORS(app) # Enables CORS for all routes 
logging.basicConfig(filename="pwa-pomodoro.log", encoding="utf-8", level=logging.DEBUG)


TASKS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Write a report',
        'pomodoro': 5,
        'completed': 0,
        'status': 'Not Started'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Study Japanese',
        'pomodoro': 3,
        'completed': 3,
        'status': 'Completed'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Creative Project',
        'pomodoro': 4,
        'completed': 2,
        'status': 'In-Progress'
    }
]


# When accessing to the hostname, route the users to index.html
# By default, a route only answers to GET requests
@app.route("/")
def index():
  return render_template('index.html')	# Flask will look for 'index.html' in templates folder 

@app.route("/manifest.json")
def serve_manifest():
   return send_file('manifest.json', mimetype='application/manifest+json')

@app.route("/sw.js")
def serve_sw():
   return send_file('sw.js', mimetype='application/javascript')

# delete later 
@app.route("/ping")
def ping_poing():
   return jsonify('pong!')

@app.route('/tasks', methods=['GET', 'POST'])
def getTasks():
   response_object = {'status': 'success'}
   if request.method == 'POST':
      post_data = request.get_json()
      if post_data.get('name') == '':
         response_object['status'] = 'error'
         response_object['message'] = 'Name is empty!'
         return jsonify(response_object)

      if post_data.get('pomodoro') == '':
         response_object['status'] = 'error'
         response_object['message'] = 'Pomodoro is empty!'
         return jsonify(response_object)
      else:
         pomodoro = int(post_data.get('pomodoro'))
      
      TASKS.append({
         'id': uuid.uuid4().hex,
         'name': post_data.get('name'),
         'pomodoro': pomodoro,
         'completed': int(post_data.get('completed', 0)),
         'status': post_data.get('status', 'Not Started')
      })
      response_object['message'] = 'Task added!'
   else:
      response_object['tasks'] = TASKS
   return jsonify(response_object)

@app.route('/tasks/<task_id>', methods=['PUT', 'DELETE'])
def updateTask(task_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        removeTask(task_id)
        TASKS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'pomodoro': int(post_data.get('pomodoro')),
            'completed': int(post_data.get('completed', 0)),
            'status': post_data.get('status')
        })
    if request.method == 'DELETE':
       removeTask(task_id)
    return jsonify(response_object)

def removeTask(task_id):
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
            return True
    return False

# run the app at port:5000 
if __name__ == "__main__":
   app.run()