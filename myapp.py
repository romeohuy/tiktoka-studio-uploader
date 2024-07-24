from tsup.tiktok.sessionId.uploader import  upload2TiktokSessionId
from tsup.utils.tools import get_duration_timestamp
from flask import Flask, url_for ,render_template
from flask import request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_video():    
    file = request.files['file']
    bt = file
    #json = request.form.get('inputField')
    sessionid =  request.form.get('sessionid')
    #file = json.get('file')
    title = request.form.get('title')
    tags = []
    result = upload2TiktokSessionId(sessionid, file, title, tags)
    return str(result)
    #return str(uploadVideo(session_id, file, title, tags, verbose=True))
		
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9111)