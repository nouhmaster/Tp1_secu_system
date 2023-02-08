from flask import Flask
from flask_cors import CORS

from rsa import *


app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/password/<psw>',methods=['POST'])
def password(psw):
    to_Byte(psw)
    public_a , secret_a =  gen_rsa_keypair(512)
    public_b , secret_b =  gen_rsa_keypair(512)
    msg_byte = to_Byte(psw)
    s = rsa_sign(msg_byte,secret_b)
    enc = rsa(msg_byte,public_a)
    m = (s,enc)
    print("message dechiffre : ",rsa_verify(public_b,secret_a,m))
    return
    
@app.route('/verifPassword/<psw>',methods=['GET'])
def verifPassword(psw):
    to_Byte(psw)
    public_a , secret_a =  gen_rsa_keypair(512)
    public_b , secret_b =  gen_rsa_keypair(512)
    msg_byte = to_Byte(psw)
    s = rsa_sign(msg_byte,secret_b)
    enc = rsa(msg_byte,public_a)
    m = (s,enc)
    if "sa" == rsa_verify(public_b,secret_a,m):
        return "true"
    else:
        return "false"

if __name__ == '__main__':
    app.run(debug=True)