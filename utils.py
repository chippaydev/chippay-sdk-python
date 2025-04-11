# coding=utf-8

import requests
import json
import hmac
import hashlib
import base64
from hashlib import sha256
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5 as pk
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from rsa import key

def httpPost(url,params):
    
    headers = {}
    headers['Content-Type'] = 'application/json'
    resp = requests.post(url, data=json.dumps(params),headers=headers)
    respBody = {}
    respBody['code'] = 200
    respBody['msg'] = 'ok'
    respBody['success'] = True
    respBody['data'] = None
    if resp.status_code != 200:
        respBody['code'] = resp.status_code
        respBody['msg'] = resp.text
        return json.dumps(respBody)
    else:
        return resp.text

def removeEmptyValue(params):
    for k in list(params.keys()):
        if params[k] == None or str(params[k]) == '':
            del params[k]

def getBaseString(params):

    removeEmptyValue(params)

    keys = sorted(params)
    size = len(params)
    i = 0;
    baseString = ''
    for key in keys:
        i=i+1;
        if i == size:
            baseString=baseString+key+"="+str(params[key])
        else:
            baseString=baseString+key+"="+str(params[key])+"&"
    return baseString

def md5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

def hmacSha256(data,secretKey):
   return hmac.new(secretKey.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).hexdigest()


def rsaSign(data,privateKey):
    pkcs8Key = RSA.import_key(base64.b64decode(privateKey))
    h = SHA256.new(data.encode('utf-8'))
    signer = pk.new(pkcs8Key)
    signature = signer.sign(h)
    return base64.b64encode(signature).decode()


def rsaVerify(data, publicKey, sign):
    try:
        pkcs8Key = RSA.import_key(base64.b64decode(publicKey))
        h = SHA256.new(data.encode('utf-8'))
        signer = pk.new(pkcs8Key)
        return signer.verify(h, base64.b64decode(sign))
    except Exception as e:
        print("驗證失敗：", e)
        return False

def genKey():

    seeds = Random.new().read
    rsa = RSA.generate(1024, seeds)
    privateKey =base64.b64encode(rsa.exportKey(format='DER')).decode()
    publicKey = base64.b64encode(rsa.publickey().exportKey(format='DER')).decode()

    keys = {}
    keys['pubKey'] = publicKey
    keys['privKey'] = privateKey
    return keys

if __name__ == '__main__':

    params = {}
    params['d'] = 20
    params['c'] = '111'
    params['a'] = '2222'
    params['m'] = 100
    params['n'] = '1'
    params['l'] = None
    baseString = getBaseString(params)
    print(baseString)
    print(md5(baseString))
    print(hmacSha256(baseString,'xxxxxxxxxxxxxxxx'))

    keys = genKey()
    privKey = keys['privKey']
    pubKey = keys['pubKey']

    print(privKey)
    print(pubKey)

    sign = rsaSign(baseString,privKey)
    
    print(sign)

    print(rsaVerify(baseString,pubKey,sign))


