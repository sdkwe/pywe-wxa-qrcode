# pywe-wxa-qrcode

Wechat MiniProgram QRCode Module for Python.

# Sandbox

* https://developers.weixin.qq.com/sandbox

# Installation

```shell
pip install pywe-wxa-qrcode
```

# Usage

```python
from pywe_wxa_qrcode import WxaQRCode, create_wxa_qrcode, get_wxa_code, get_wxa_code_unlimit
```

# Method

```python
class WxaQRCode(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(WxaQRCode, self).__init__(appid=appid, secret=secret, token=token, storage=storage)

def get_wxa_code(self, path, width=430, auto_color=False, line_color={'r': '0', 'g': '0', 'b': '0'}, is_hyaline=False, appid=None, secret=None, token=None, storage=None, res_to_base64=True, data_uri_scheme=True):

def get_wxa_code_unlimit(self, sence, page=None, width=430, auto_color=False, line_color={'r': '0', 'g': '0', 'b': '0'}, is_hyaline=False, appid=None, secret=None, token=None, storage=None, res_to_base64=True, data_uri_scheme=True):

def create_wxa_qrcode(self, path, width=430, appid=None, secret=None, token=None, storage=None, res_to_base64=True, data_uri_scheme=True):
```
