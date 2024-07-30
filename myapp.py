from tsup.tiktok.sessionId.uploader import  upload2TiktokSessionId
from tsup.utils.tools import get_duration_timestamp
from flask import Flask, url_for ,render_template
from flask import request
import random
app = Flask(__name__)
nature_titles = [
    "Khám phá vẻ đẹp thiên nhiên",
    "Hành trình khám phá rừng xanh",
    "Thế giới dưới lòng đại dương",
    "Ngắm hoàng hôn tuyệt đẹp",
    "Bình minh trên đỉnh núi",
    "Cảnh quan thiên nhiên hùng vĩ",
    "Vẻ đẹp của mùa thu",
    "Thiên nhiên hoang dã",
    "Thác nước hùng vĩ",
    "Cánh đồng hoa bất tận",
    "Dòng suối trong lành",
    "Rừng thông yên tĩnh",
    "Vườn quốc gia tuyệt đẹp",
    "Thiên nhiên kỳ bí",
    "Hành trình khám phá động vật hoang dã",
    "Cảm nhận thiên nhiên",
    "Thiên đường nhiệt đới",
    "Vẻ đẹp của biển cả",
    "Cảnh đẹp vùng quê",
    "Thiên nhiên hoang sơ"
]

nature_hashtags = [
    "Nature",
    "Explore",
    "Forest",
    "Adventure",
    "Ocean",
    "Underwater",
    "Sunset",
    "Beauty",
    "Sunrise",
    "Mountain",
    "Landscape",
    "Autumn",
    "Fall",
    "Wildlife",
    "Waterfall",
    "FlowerField",
    "Stream",
    "Peaceful",
    "PineForest",
    "Tranquil",
    "NationalPark",
    "Mystery",
    "FeelNature",
    "Relax",
    "Tropical",
    "Paradise",
    "Sea",
    "Countryside",
    "Untouched"
]

# Số lượng tiêu đề muốn chọn ngẫu nhiên
num_tag = 5
@app.route('/upload', methods=['POST'])
def upload_video():    
    file = request.files['file']
    bt = file
    #json = request.form.get('inputField')
    sessionid =  request.form.get('sessionid')
    #file = json.get('file')
    title = random.choice(nature_titles) #request.form.get('title')
    tags = random.sample(nature_hashtags, num_tag)
    result = upload2TiktokSessionId(sessionid, file, title, tags)
    print(title)
    return str(result)
    #return str(uploadVideo(session_id, file, title, tags, verbose=True))
		
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9111)