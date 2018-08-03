# -*- coding: utf-8 -*-

import base64

from pywe_token import BaseToken, final_access_token


class WxaQRCode(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(WxaQRCode, self).__init__(appid=appid, secret=secret, token=token, storage=storage)
        # 获取二维码, Refer: https://developers.weixin.qq.com/miniprogram/dev/api/qrcode.html
        # 接口A: 适用于需要的码数量较少的业务场景
        self.GET_WXA_CODE = self.API_DOMAIN + '/wxa/getwxacode?access_token={access_token}'
        # 接口B：适用于需要的码数量极多的业务场景
        self.GET_WXA_CODE_UNLIMIT = self.API_DOMAIN + '/wxa/getwxacodeunlimit?access_token={access_token}'
        # 接口C：适用于需要的码数量较少的业务场景
        self.CREATE_WXA_QRCODE = self.API_DOMAIN + '/cgi-bin/wxaapp/createwxaqrcode?access_token={access_token}'

    def get_wxa_code(self, path, width=430, auto_color=False, line_color={'r': '0', 'g': '0', 'b': '0'}, is_hyaline=False, appid=None, secret=None, token=None, storage=None, res_to_base64=True, data_uri_scheme=True):
        data = self.post(
            self.GET_WXA_CODE.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            data={
                'path': path,
                'width': width,
                'auto_color': auto_color,
                'line_color': line_color,
                'is_hyaline': is_hyaline,
            },
            res_to_json=False
        )
        if not res_to_base64:
            return data
        return '{0}{1}'.format('data:image/png;base64,' if data_uri_scheme else '', base64.b64encode(data.content))

    def get_wxa_code_unlimit(self, sence, page=None, width=430, auto_color=False, line_color={'r': '0', 'g': '0', 'b': '0'}, is_hyaline=False, appid=None, secret=None, token=None, storage=None, res_to_base64=True, data_uri_scheme=True):
        data = self.post(
            self.GET_WXA_CODE_UNLIMIT.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            data={
                'sence': sence,
                'page': page,
                'width': width,
                'auto_color': auto_color,
                'line_color': line_color,
                'is_hyaline': is_hyaline,
            },
            res_to_json=False
        )
        if not res_to_base64:
            return data
        return '{0}{1}'.format('data:image/png;base64,' if data_uri_scheme else '', base64.b64encode(data.content))

    def create_wxa_qrcode(self, path, width=430, appid=None, secret=None, token=None, storage=None, res_to_base64=True, data_uri_scheme=True):
        data = self.post(
            self.CREATE_WXA_QRCODE.format(access_token=final_access_token(self, appid=appid, secret=secret, token=token, storage=storage)),
            data={
                'path': path,
                'width': width,
            },
            res_to_json=False
        )
        if not res_to_base64:
            return data
        return '{0}{1}'.format('data:image/png;base64,' if data_uri_scheme else '', base64.b64encode(data.content))


wxaqrcode = WxaQRCode()
get_wxa_code = wxaqrcode.get_wxa_code
get_wxa_code_unlimit = wxaqrcode.get_wxa_code_unlimit
create_wxa_qrcode = wxaqrcode.create_wxa_qrcode
