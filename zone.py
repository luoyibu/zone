#!/usr/bin/python
#encoding:UTF-8
import requests
import time
from bs4 import BeautifulSoup as bs

def getZone(userId, userPsw):

	headers = {
	'Host' : 'www.wuhaneduyun.cn',
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
	'Referer' : 'http://www.wuhaneduyun.cn/?r=api/sso/portal&app_id=2',
	'Origin' : 'http://www.wuhaneduyun.cn'
	}

	s = requests.Session()
	r = s.get('http://www.wuhaneduyun.cn/portal/html/wuhan/', headers=headers)

	formData = {
		'userId' : userId,
		'userPsw' : userPsw
	}

	resp = s.post('http://www.wuhaneduyun.cn/index.php?r=portal/user/doLogin&ajax=1', formData, headers=headers)

	s.get('http://www.wuhaneduyun.cn/index.php?r=center/person/index', headers=headers)

	s.get('http://www.wuhaneduyun.cn/index.php?r=space/person/index&sid=F259F9AB38677692E04010AC73D40970', headers=headers)

	f = s.get('http://www.wuhaneduyun.cn/index.php?r=space/person/index/GetModuleHtml&wname=&name=visitor&spacetype=space_person&sid=F259F9AB38677692E04010AC73D40970')

	soup = bs(f.content)

	# count = soup.find('i')
	count = soup.find('i', {'class': 'blue'}).string

	print(count)

	return



datas = [
	'300524807',
	'300817074',
	'300461925',
	'300594310',
	'300706764',
	'300309970',
	'300876713',
	'300153338',
	'300579460',
	'300277033',
	'300607012',
	'300359454'
]



for x in xrange(0,len(datas) - 1):
	getZone(datas[x], '12345678')

