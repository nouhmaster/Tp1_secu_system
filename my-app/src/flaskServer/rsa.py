from Cryptodome.Util.number import getPrime, inverse
import hashlib

def gen_rsa_keypair(taille):
    p = getPrime(taille//2)
    q = getPrime(taille//2)
    assert( p != q)
    n = p*q
    e = 65537

    d = inverse(e,(p-1) * (q-1))
    return ((e,n),(d,n))

def rsa(message,key):
    return pow(message,key[0],key[1])

def rsa_enc(message,key):
    msg = int.from_bytes(message.encode('utf-8'),'big')
    return rsa(msg,key)

def rsa_dec(message,key):
    m = rsa(message,key)
    return m.to_bytes((message.bit_length() + 7) // 8,'big').decode('utf-8')

def to_Byte(msg):
        return int.from_bytes(msg.encode('utf-8'),'big')

def h(entier):
    sign = hashlib.sha256(entier.to_bytes(64, 'big')).hexdigest()
    return int(sign, 16)


def rsa_sign(message,key):
    msg_sign = h(message)
    return rsa(msg_sign,key)

def rsa_verify(kp,ks,m):
        print(ks)
        s = rsa((m[0]),kp)
        dec = rsa((m[1]),ks)
        if( s != h(dec)):
            print("ERROR")
            exit()
        else:
            return dec.to_bytes((dec.bit_length() + 7) // 8, 'big').decode('utf-8')



public_a , secret_a =  gen_rsa_keypair(512)
public_b , secret_b =  gen_rsa_keypair(512)

msg = "text pour test"
print("message en claire : ",msg,"\n")

msg_byte = to_Byte(msg)
print("message en byte: ",msg_byte,"\n")
s = rsa_sign(msg_byte,secret_b)
print("message signé hashé avec la clef secret b: ",s,"\n")
enc = rsa(msg_byte,public_a)
print("message chiffre avec rsa et la clef public de a: ",enc,"\n")
m = (s,enc)
print("message dechiffre : ",rsa_verify(public_b,secret_a,m))