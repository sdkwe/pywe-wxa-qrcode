# -*- coding: utf-8 -*-

import requests
from pywe_wxa_qrcode import WxaQRCode, create_wxa_qrcode, get_wxa_code, get_wxa_code_unlimit

from local_wecfg_example import WECHAT


class TestWxaQRCodeCommands(object):
    def test_get_wxa_code(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        wxaqr = WxaQRCode(appid=appid, secret=appsecret)
        data = wxaqr.get_wxa_code(path='pages/index/index', res_to_base64=False)
        assert isinstance(data, requests.Response)
        assert data.status_code == 200

        b64 = get_wxa_code(path='pages/index/index', appid=appid, secret=appsecret)
        assert isinstance(b64, basestring)
        assert b64.startswith('data:image/png;base64,')

    def test_get_wxa_code_unlimit(self):
        sence = 'un_gt_32'
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        wxaqr = WxaQRCode(appid=appid, secret=appsecret)
        data = wxaqr.get_wxa_code_unlimit(sence, page='pages/index/index', res_to_base64=False)
        assert isinstance(data, requests.Response)
        assert data.status_code == 200

        b64 = get_wxa_code_unlimit(sence, page='pages/index/index', appid=appid, secret=appsecret)
        assert isinstance(b64, basestring)
        assert b64.startswith('data:image/png;base64,')

    def test_create_wxa_qrcode(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        wxaqr = WxaQRCode(appid=appid, secret=appsecret)
        data = wxaqr.create_wxa_qrcode(path='pages/index/index', res_to_base64=False)
        assert isinstance(data, requests.Response)
        assert data.status_code == 200

        b64 = create_wxa_qrcode(path='pages/index/index', appid=appid, secret=appsecret)
        assert isinstance(b64, basestring)
        assert b64.startswith('data:image/png;base64,')
