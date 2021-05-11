#1.采--网页的采集
import requests
#req = requests.get('https://wap.zol.com.cn/top/cell_phone/hot.html')

#2.抽--信息的抽取
#用正则表达式实现信息提取
import re
#result = re.findall(
#	'<p class="pro-info-name f28">(.*?)<\/p>[\S\s]*?<span class="pro-info-price f24">(.*?)<\/span>',
#	req.text
#)

#3.存--保存采集结果
#保存爬取信息
#with open('mobile.txt', 'w') as f:
#	for item in result:
#		f.write(item[0] + ' ' + item[1] + '\n')

#基础爬虫类（框架）
import requests
import re

class MyCrawler:
	def __init__(self, filename):
		self.filename = filename
	
	def download(self, url):
		r = requests.get(url)
		return r.text
	
	def extract(self, content, pattern):
		result = re.findall(pattern, content)
		return result
	
	def save(self, info):
		with open(self.filename, 'a', encoding='utf-8') as f:
			for item in info:
				f.write('|||'.join(item) + '\n')
	
	def crawl(self, url, pattern):
		content = self.download(url)
		info = self.extract(content, pattern)
		self.save(info)

#对zo.com.cn进行测试
#crawler = MyCrawler('mobile.txt')
#crawler.crawl(
#    'https://wap.zol.com.cn/top/cell_phone/hot.html', 
#	'<p class="pro-info-name f28">(.*?)<\/p>[\S\s]*?<span class="pro-info-price f24">(.*?)<\/span>'
#)

#对bilibili进行测试
b_crawler = MyCrawler('bilibili.txt')
#c = b_crawler.download('https://www.bilibili.com/v/popular/rank/all')
#info = b_crawler.extract(
#	c,
#	'<a\shref="([^"]*?)"\starget="_blank"\sclass="title">(.*?)<\/a>[\S\s]*?(.*?)万'
#)
#b_crawler.save(info)

#b_crawler.crawl(
#	'https://www.bilibili.com/v/popular/rank/all',
#	'<a\shref="([^"]*?)"\starget="_blank"\sclass="title">(.*?)<\/a>[\S\s]*?(.*?)万'
#)
#with open('bilibili.txt', 'r', encoding='utf-8') as f:
#	lines = f.read()
#	for line in lines.split('\n'):
#		print(line)

#对豆瓣进行测试
b_crawler = MyCrawler('douban_book.txt')
t = b_crawler.download('https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C')

#用curl.trillworks.com实现Chrome网络请求的“克隆”
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
}
response = requests.get('https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C', headers=headers)
print(len(response.text))
print('Hands-On Machine Learning' in response.text)
