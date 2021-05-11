#基础爬虫类（框架）
import requests
import re

class MyCrawler:
	def __init__(self, filename):
		self.filename = filename
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
		}
	
	def download(self, url):
		r = requests.get(url, headers=self.headers)
		return r.text
	
	def extract(self, content, pattern):
		result = re.findall(pattern, content)
		return result
	
	def save(self, info):
		with open(self.filename, 'a', encoding='utf-8') as f:
			for item in info:
				f.write('|||'.join(item) + '\n')
	
	def crawl(self, url, pattern, headers=None):
		if headers:
			slef.headers.update(headers)
		content = self.download(url)
		info = self.extract(content, pattern)
		self.save(info)

#对豆瓣进行测试
#b_crawler = MyCrawler('douban_book.txt')
#b_crawler.crawl(
#	'https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C',
#	'src="(.*?\d+.jpg)"[\S\s]*?<a\shref="(https:\/\/book.douban.com/subject\/\d+/)"\stitle="(.*?)"[\S\s]*?<div class="pub">\s*(.*?)\s*<\/div>[\S\s]*?<div class="star\sclearfix">\s*([\S\s]*?)\s*<\/div>'
#)


class MyDoubanCrawler(MyCrawler):
	def extract(self, content, pattern_main, pattern_star):
		result = re.findall(pattern_main, content)
		for index in range(len(result)):
			if 'allstar' in result[index][4]:
				items = re.findall(pattern_star, result[index][4])
			else:
				items = [['0', '0', '0']]
			result[index] = list(result[index])
			del result[index][4]
			result[index].extend(items[0])
		return result
	
	def crawl(self, url, pattern_main, pattern_star, headers=None):
		if headers:
			self.headers.update(headers)
		content = self.download(url)
		info = self.extract(content, pattern_main, pattern_star)
		self.save(info)

b_douban_crawler = MyDoubanCrawler('douban_book_new.txt')
b_douban_crawler.crawl(
	'https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C',
	'src="(.*?\d+.jpg)"[\S\s]*?<a\shref="(https:\/\/book.douban.com/subject\/\d+/)"\stitle="(.*?)"[\S\s]*?<div class="pub">\s*(.*?)\s*<\/div>[\S\s]*?<div class="star\sclearfix">\s*([\S\s]*?)\s*<\/div>',
	'allstar(\d+)"[\S\s]*?rating_nums">([^<]*?)<\/span>[\S\s]*?\((\d+)'
)

