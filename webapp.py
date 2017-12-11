from flask import *
import os
import bow_query as bq
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/upload", methods=['POST'])
def upload_image():
    file = request.files['image']
    name = str(uuid.uuid4().hex) + '.' + file.filename.split('.')[-1]
    file.save(name)
    floor, x, y, rot = bq.Query(name)
    os.remove(name)
    return jsonify(floor=floor, x=x, y=y, orientation=rot)

@app.route('/maps/<path:path>')
def send_image(path):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)) + '/maps/', path);

@app.route('/<path:path>')
def send_static(path):
    return app.send_static_file(path)
