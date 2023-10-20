import json
import time
import hashlib
import hmac
import base64
import uuid

# Declare empty header dictionary
apiHeader = {}
# open token
token = '794c291dfb43e965e2783065a76d051d6441107f71517724e86e1579f981c31aec43fda255032948af24886a4df74fd5'  # copy and paste from the SwitchBot app V6.14 or later
# secret key
secret = 'e1214b43e2914fbe949ac07aac7f0154'  # copy and paste from the SwitchBot app V6.14 or later
nonce = uuid.uuid4()
t = int(round(time.time() * 1000))
string_to_sign = '{}{}{}'.format(token, t, nonce)

string_to_sign = bytes(string_to_sign, 'utf-8')
secret = bytes(secret, 'utf-8')

sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
print('Authorization: {}'.format(token))
print('t: {}'.format(t))
print('sign: {}'.format(str(sign, 'utf-8')))
print('nonce: {}'.format(nonce))

# Build api header JSON
apiHeader['Authorization'] = token
apiHeader['Content-Type'] = 'application/json'
apiHeader['charset'] = 'utf8'
apiHeader['t'] = str(t)
apiHeader['sign'] = str(sign, 'utf-8')
apiHeader['nonce'] = str(nonce)
