## 法大大 Python SDK 说明

#### 1.目录结构
client 为客户端
exception 主要包含客户端初始异常，以及服务端业务异常
utils 包含了http,hash工具类方法 和全局常量
test 目录为测试用例

#### 2.使用说明
本SDK是在python3.7环境下开发的，如果其他版本使用遇到问题请联系相关人员

直接在SDK压面下载压缩包，或者使用git 拷贝github上SDK文件
解压以后使用命令安装：
```python
python setup.py install
```

安装完sdk以后需要安装sdk使用的依赖包,执行以下命令安装：
```python
pip install -r requirements.txt
```

下面是配置以及获取token的demo：
token的有效期是2个小时，不一定每一次请求都要获取token。

```python
from fdd_sdk.client.client import FddClient
from fdd_sdk.client.oauth2 import Oauth2Client
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException
#默认请求正式环境
fdd_client = FddClient('appId', 'appKey')

#指定环境请求 log 日志默认关闭
fdd_client = FddClient('appId', 'appKey', request_url='请求url', log=True)

#获取token
try:
    result = Oauth2Client.get_token(fdd_client)
    print('token = %s' % result['data']['accessToken'])
except ClientException as  e:
#客户端初始化异常
    print(e)
except ServerException as e:
#服务端业务异常
    print(e)



```


