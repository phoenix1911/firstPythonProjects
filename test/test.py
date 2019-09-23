# -*- coding: utf-8 -*-
import urllib.request

# 1、网址url  --豆瓣网
url = 'https://v2.cloopm.com/#/itsm/eventOne?type=organization&id=36&name=中国移动&organizationId=36'

# 2、直接请求  返回结果
response = urllib.request.urlopen(url)

# 3、获取状态码，如果是200表示获取成功
print('状态码：', response.getcode())

# 4、读取内容
data = response.read()

# 5、设置编码
data = data.decode('utf-8')


# 6、打印结果
print(data)
