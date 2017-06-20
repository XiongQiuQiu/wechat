from flask import Flask
from flask import request
import itchat

app = Flask(__name__)

@app.route('/sendmsg')
def send_msg():
    to = request.args.get('to')
    msg = request.args.get('msg')
    if not to or not msg:
        return str({'status': '900', 'reason' : 'to and msg arg must not empty'})
    send_name = itchat.search_friends(name=to)[0]
    send_name.send('hello world')
    return str({'status': 200})

if __name__ == '__main__':
    itchat.auto_login()
    app.run()

