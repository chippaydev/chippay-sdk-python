# coding=utf-8

from utils import getBaseString, hmacSha256, httpPost, md5


class ApiV1:
    def __init__(self,secretKey):
        self.secretKey = secretKey
    
    def call(self,url,params):
        params['secretKey'] = self.secretKey
        if params['signType'] == 1:
            baseString = getBaseString(params)
            sign = hmacSha256(baseString,self.secretKey)
            del params['secretKey']
            params['sign'] = sign
            return httpPost(url,params)
        else:
            baseString = getBaseString(params)
            sign = md5(baseString)
            del params['secretKey']
            params['sign'] = sign
            return httpPost(url,params)