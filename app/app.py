import os
import json
from flask import Flask, request, jsonify
from functools import wraps
from utils import send_telegram_msg

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['TOKEN'] = os.getenv('TOKEN')
app.config['TELEGRAM_TOKEN'] = os.getenv('TELEGRAM_TOKEN')
app.config['TELEGRAM_CHATID'] = os.getenv('TELEGRAM_CHATID')

def check_token(fn):
    """
        This decorator will check if the request
        have a valid token.
        TOKEN must be configured on a environment variable
    """
    @wraps(fn)
    def new_fn(*args, **kwargs):
        msg = 'Access Unauthorized'
        if 'token' in request.headers:
            if request.headers['token'] != app.config['TOKEN']:
                return jsonify({'message': msg}), 401
        else:
            return jsonify({'message': msg}), 401
        return fn(*args, **kwargs)
    return new_fn

@app.route('/tgmessage', methods=['POST'])
@check_token
def traction_guest_message():
    # check content-type to accept only json
    if request.content_type != 'application/json':
        return jsonify({'message': 'Bad Request'}), 400
    response = send_telegram_msg(request.get_json(), app.config['TELEGRAM_CHATID'], app.config['TELEGRAM_TOKEN'])
    return (jsonify(response))

if __name__ == '__main__':
    app.run(debug=False)