# coding=utf-8

from utils import getBaseString, hmacSha256, httpPost, md5, rsaSign


class ApiV2:
    def __init__(self,privateKey):
        self.privateKey = privateKey
    
    def call(self,url,params):
        baseString = getBaseString(params)
        sign = rsaSign(baseString,self.privateKey)
        params['sign'] = sign
        return httpPost(url,params)