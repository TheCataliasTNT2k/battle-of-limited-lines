from flask import Flask, request, send_file, send_from_directory,  render_template, jsonify
import config,pafy, os
import threading
import logging, json

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

app = Flask(__name__)

for file in os.listdir('downloads'):
    os.remove('downloads/' + file)

def download(video, url):
    print("Downloading...")
    video.getbest().download(filepath='downloads/' + url.split('watch?v=')[1] + '.mp4')
    print("Downloaded")
@app.route('/api/new', methods=['POST'])
def new():
    url = request.args.get('url')
    video = pafy.new(url)
    thread = threading.Thread(target=download, args=(video,url))
    thread.start()
    #video.getbest('downloads/' + url.split('watch?v=')[1] + '.mp4')
    print('New')
    return ''
@app.route('/api/get', methods=['GET'])
def get():
    url = request.args.get('url').split('watch?v=')[1] + '.mp4'
    video =  pafy.new(url.replace('.mp4',''))
    return send_file('downloads/'+url, attachment_filename=video.title + '.mp4')
@app.route('/api/isthere')
def isthere():
    url = request.args.get('url').split('watch?v=')[1] + '.mp4'

    if os.path.exists('downloads/' + url):
        print("Yes")
        return jsonify({'ok': True})
    return jsonify({'ok': False})

@app.route('/javascript/<string:js>')
def getjs(js):
    return send_from_directory(directory='javascript', filename=js)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__': app.run(host=config.FLASK_SERVER_HOST.split(':')[0], threaded=config.FLASK_THREADING, debug=config.FLASK_DEBUG, port=config.FLASK_SERVER_HOST.split(':')[1])