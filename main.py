import flask
import werkzeug
import time
from flask import request
import pickle
#from flask_socketio import SocketIO, send
#from subprocess import call
import ML

app = flask.Flask(__name__)
filepath = 'D:/Server/'

User_list = {}

try:
    file=open(filepath+"Flask_server/User_list","rb")
    User_list=pickle.load(file)
except:
    User_list = {}

print(User_list)

@app.route('/')
def hello_world():
    print(__name__)
    return "Hello Students!"

@app.route('/post', methods = ["POST"])
def hello_post():
    value=request.form['value']
    return (value)

@app.route('/sum', methods = ["POST"])
def hello_sum():
    value1=request.form['ID']
    value2=request.form['PW']
    if str(value1) in User_list:
        return "중복된 아이디 입니다"
    else:
        User_list[str(value1)] = [str(value2),int(0)]

        file = open(filepath+"Flask_server/User_list", "wb")
        pickle.dump(User_list, file)
        file.close()
        return "회원가입이 완료되었습니다"


@app.route('/confirm', methods = ["POST"])
def hello_confirm():
    try:
        file = open(filepath + "Flask_server/User_list", "rb")
        User_list = pickle.load(file)
    except:
        User_list = {}

    value1=request.form['ID']
    value2=request.form['PW']
    if str(value1) in User_list:
        if User_list[str(value1)][0] == str(value2):
            return "로그인되었습니다"
        else:
            return "아이디 또는 패스워드를 확인해주세요"
    else:
        return "아이디 또는 패스워드를 확인해주세요"

@app.route('/imgupload', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%H_%M_%S")
#        imagefile.save(filepath+'Android/'+timestr+'.jpg')
        imagefile.save(filepath+'Android/'+'Sample'+'.jpg')
        image_num = image_num + 1
    print("\n")
    ML.ML()
    return "Image(s) Uploaded Successfully. Come Back Soon."

@app.route('/result')
def result():
    f = open(filepath+'Python/'+"ML_result.txt", "w")
    f.write("파일 내용은 이거야. \n")
    f.close()

    return "TXT(s) Uploaded Successfully. Come Back Soon."


@app.route('/uploads/<filename>')
def send_file(filename):
    return flask.send_from_directory('D:/Server/Unity', filename)




app.run(host="192.168.0.3", port=5000, debug=True)




"""
socketio = SocketIO(app)

@app.route('/chat')
def chatting():
    return flask.render_template('chat.html')


@socketio.on("message")
def request(message):
    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = "새로운 유저가 난입하였다!!"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
# emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
        send(to_client, broadcast=True)

"""


