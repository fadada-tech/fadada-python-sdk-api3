"""
公共全局参数
"""


class Params:
    # api请求头参数key
    APP_ID_KEY = 'X-FDD-Api-App-Id'
    SIGN_TYPE_KEY = 'X-FDD-Api-Sign-Type'
    TOKEN_KEY = 'X-FDD-Api-Token'
    TIMESTAMP_KEY = 'X-FDD-Api-Timestamp'
    NONCE_KEY = 'X-FDD-Api-Nonce'
    GRANT_TYPE_KEY = 'X-FDD-Api-Grant-Type'
    SIGN_KEY = 'X-FDD-Api-Sign'
    BIZ_CONTENT_KEY = 'bizContent'
    # 签名方式
    SIGN_TYPE = 'HMAC-SHA256'
    GRANT_TYPE = 'client_credential'
    # 编码类型
    ENCODE_TYPE = 'utf-8'

    # 时间字符串格式
    TIME_FORMAT_MILLISECOND = '%Y-%m-%d %H:%M:%S.%f'

    TIME_FORMAT = '%Y%m%d%H%M%S'

    # 字典拼接填充
    DICT_TO_STR = '%s=%s&'

    # 接口请求成功code
    REQUEST_SUCCESS_CODE = '100000'

    # 响应数据data里面 code key
    REQUEST_DATA_CODE = 'code'

    # 响应数据data里面 msg key
    REQUEST_DATA_MSG = 'msg'
