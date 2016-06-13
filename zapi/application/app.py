__author__ = 'zhonghong'
from zapi import Zapi

app = Zapi('./')
app.serve_forever()

