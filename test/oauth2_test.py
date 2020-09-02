from fdd_sdk.client.client import FddClient
from fdd_sdk.client.oauth2 import Oauth2Client
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

# 默认请求正式环境
fdd_client = FddClient('appId', 'appKey')

# 指定环境请求
fdd_client = FddClient('appId', 'appKey', request_url='指定环境url')

# 开启日志（默认是关闭日志的）
fdd_client = FddClient('appId', 'appKey', log=True)

# 设置超时时间 单位秒
fdd_client = FddClient('appId', 'appKey', timeout=5)

# 获取token
try:
    result = Oauth2Client.get_token(fdd_client)
    print('token = %s' % result['data']['accessToken'])
except ClientException as  e:
    print('client异常：%s' % e.__str__())
except ServerException as e:
    print('业务异常：%s' % e.__str__())
