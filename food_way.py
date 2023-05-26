# -*- coding: utf-8 -*-
import http.client, urllib, json
import os
warming='''100	内部服务器错误	报此错误码请及时反馈或等待官方修复
110	当前API已下线	接口已下线无法使用，可关注相关通知
120	API暂时维护中	接口暂时关闭维护中，请注意相关公告
130	API调用频率超限	超过每秒请求数上限，可在控制台-接口管理中查询
140	API没有调用权限	请检查是否自行在接口管理中停用或被禁用了该接口
150	API可用次数不足	免费类接口套餐超限或计次类接口余额不足
160	账号未申请该API	请先在接口文档页面申请该接口，点此查看说明
170	Referer请求来源受限	设置了Referer白名单，但来源Referer不在白名单内
180	IP请求来源受限	设置了IP白名单，但来源IP不在白名单内
190	当前账号已限制使用	通常为账号被限制使用，此状态无法恢复
230	key错误或为空	请检查apikey是否填写错误，点此查看帮助
240	缺少key参数	请检查是否传递了key参数或者编码格式是否符合要求
250	数据返回为空	数据查询或转换失败，请检查输入值或注意中文编码问题
260	参数值不得为空	请检查关键参数是否传递了空值
270	参数值不符合要求	参数值不符合基本格式要求，点此查看说明
280	缺少必要的参数	缺少必填的参数，请根据接口文档检查
290	超过最大输入字节限制	超出最大字符限制，请查看接口文档的说明
错误码1开头的是系统级错误，2开头的是用户级错误，其中200表示请求成功处理并计费。'''


print('\033[0;32m%s\033[0m' % '=========================================')		  
print('\033[0;33m%s\033[0m' % '【菜谱搜索 by 王熙业】终端应用')
print('\033[0;36m%s\033[0m' % '所有资源来于网络api')
print('\033[0;35m%s\033[0m' % '该文件用于菜谱查询,需要去apis.tianapi.com网站获取key才可使用，且只有免费100次每天')
print('the requirements of run the codes: pip3 install urllib,json,http.client ')
print('\033[0;32m%s\033[0m' % '=========================================')
os.system('date')
while 1:	
	conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
	look=input('\033[0;32m%s\033[0m' %'(每日100次免费,退出输入：q)输入要搜索的菜谱名字：')
	if look=='q':
		print('感谢使用！')
		break
	params = urllib.parse.urlencode({'key':'ede818a4f86014d25a8027050244ca87','word':look})
	headers = {'Content-type':'application/x-www-form-urlencoded'}
	conn.request('POST','/caipu/index',params,headers)
	tianapi = conn.getresponse()
	result = tianapi.read()
	data = result.decode('utf-8')
	dict_data = json.loads(data)
	msg=dict_data['msg']
	code=dict_data['code']
	print('状态码:' + str(code))
	if msg!='success':
		print('错误，看状态码........')
		print(warming)
	else:
		result=dict_data['result']
		list=result['list'][0]
		type_name=list['type_name']
		cp_name=list['cp_name']
		zuofa=list['zuofa']
		texing=list['texing']
		tishi=list['tishi']
		tiaoliao=list['tiaoliao']
		yuanliao=list['yuanliao']
		content='菜名：'+cp_name+'\n\n类别：'+type_name+'\n\n原料：'+yuanliao+'\n\n调料：'+tiaoliao+'\n\n做法：'+zuofa+'\n\n特性：'+texing+'\n\n提示：'+tishi
		print(content)
		
		
		