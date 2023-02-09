from flask import Flask, request
from flask_cors import CORS
import regex as re
from rsa import *
import connectionDB

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/password/',methods=['GET'])
def password():
    
    psw = request.args.get('psw')
    mail = request.args.get('mail')
    print(psw)
    public_a , secret_a =  gen_rsa_keypair(512)
    public_b , secret_b =  gen_rsa_keypair(512)
    msg_byte = to_Byte(psw)
    s = rsa_sign(msg_byte,secret_b)
    enc = rsa(msg_byte,public_a)
    m = (s,enc)
    print(m)
    message = connectionDB.add_user(mail,str(m))
    return str(message)
    
    
@app.route('/connection/',methods=['GET'])
def verifPassword():
    mail = request.args.get('mail')
    public_a , secret_a =  gen_rsa_keypair(512)
    public_b , secret_b =  gen_rsa_keypair(512)
    if connectionDB.user_exists(mail):
        print("L'utilisateur existe.")
        password = request.args.get('psw') 
        psw  = connectionDB.get_password(mail)
        numbers = re.findall(r'\d+', psw)
        res = [eval(i) for i in numbers]
        print(res)
        # tuple_obj = tuple(map(int, res).split(','))
        print(password)
        if password == rsa_verify(public_b,secret_a,res):
            return "bon mot de pass"
        else:
            return "mauvais"
    else:
        return "L'utilisateur n'existe pas."
    
if __name__ == '__main__':
    app.run(debug=True)