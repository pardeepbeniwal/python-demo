class Config(object):
    BASE_URL="https://uat.trupay.in/TruPay/"
    AUTHORISATION="476f85dd-f29e-461c-aeb3-a7426ac11f1a"
    SALT="f1443a27"
    RET_URL_SUCC="http://127.0.0.1:5000/callbacks"
    RET_URL_FAIL="http://127.0.0.1:5000"

    WEB_SESSION_URL="v1/api/getOneTimeWebSessionKey"
    MERCHANT_REQUEST_STATUS= "v1/api/merchantRequestStatus"

    REQUEST_MONEY = "v1/api/merchantRequestMoney"
    CANCEL_REQUEST= "v1/api/cancelRequest"
    
    
"""Api Token: 476f85dd-f29e-461c-aeb3-a7426ac11f1a
Client Id: TRUAPI14823
Api Salt: f1443a27"""
