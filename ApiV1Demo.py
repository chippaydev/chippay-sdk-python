# coding=utf-8

import time
from ApiV1 import ApiV1


def testAddBuyOrder():

    params = {}
    params['username'] = 'haha';
    params['areaCode'] = "86";
    params['phone'] = '18900000008';
    params['idCardType'] = 1;
    params['idCardNum'] = '430524143201097878';
    params['kyc'] = 2;
    params['companyOrderNum'] =  int(round(time.time() * 1000000)) #must to be unique
    params['coinSign'] = 'USDT';
    params['coinAmount'] = 20;
    params['total'] = 200;
    params['orderPayChannel'] = 3;
    params['payCoinSign'] = 'cny';
    params['companyId'] = '12511234561'; #merchantId
    params['orderTime'] = int(round(time.time() * 1000)); #milli seconds
    params['orderType'] = 1; #1 add buy order,2 sell order
    params['signType'] = 1;
    params['syncUrl'] = 'http://127.0.0.1:8088';
    params['asyncUrl'] = 'http://127.0.0.1:8088/v1/callback';

    apiV1 = ApiV1('b7ef76e3b52a9d793d98fd6a3d92d6cf');

    print(apiV1.call('https://open-v2.chippaytest.com/cola/order/addOrder',params))



if __name__ == '__main__':
    testAddBuyOrder()