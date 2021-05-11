#上次课导入的莫尔斯电码对照表数据
morse_dict = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··', '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····', '6': '-····', '7': '--···', '8': '---··', '9': '----·', '0': '-----', '.': '·-·-·-', ':': '---···', ',': '--··--', ';': '-·-·-·', '?': '··--··', '=': '-···-', "'": '·----·', '/': '-··-·', '!': '-·-·--', '-': '-····-', '_': '··--·-', '"': '·-··-·', '(': '-·--·', ')': '-·--·-', '$': '···-··-', '&': '·-···', '@': '·--·-·', '+': '·-·-·'}

morse_dict_r = {'·-': 'A', '-···': 'B', '-·-·': 'C', '-··': 'D', '·': 'E', '··-·': 'F', '--·': 'G', '····': 'H', '··': 'I', '·---': 'J', '-·-': 'K', '·-··': 'L', '--': 'M', '-·': 'N', '---': 'O', '·--·': 'P', '--·-': 'Q', '·-·': 'R', '···': 'S', '-': 'T', '··-': 'U', '···-': 'V', '·--': 'W', '-··-': 'X', '-·--': 'Y', '--··': 'Z', '·----': '1', '··---': '2', '···--': '3', '····-': '4', '·····': '5', '-····': '6', '--···': '7', '---··': '8', '----·': '9', '-----': '0', '·-·-·-': '.', '---···': ':', '--··--': ',', '-·-·-·': ';', '··--··': '?', '-···-': '=', '·----·': "'", '-··-·': '/', '-·-·--': '!', '-····-': '-', '··--·-': '_', '·-··-·': '"', '-·--·': '(', '-·--·-': ')', '···-··-': '$', '·-···': '&', '·--·-·': '@', '·-·-·': '+'}

#莫尔斯编解码的类实现
class morseCodec:
	"""Morse Encoding and Decoding
	"""
	def __init__(self):
		self.morse_dict = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··', '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····', '6': '-····', '7': '--···', '8': '---··', '9': '----·', '0': '-----', '.': '·-·-·-', ':': '---···', ',': '--··--', ';': '-·-·-·', '?': '··--··', '=': '-···-', "'": '·----·', '/': '-··-·', '!': '-·-·--', '-': '-····-', '_': '··--·-', '"': '·-··-·', '(': '-·--·', ')': '-·--·-', '$': '···-··-', '&': '·-···', '@': '·--·-·', '+': '·-·-·'}
		self.morse_dict_r = {'·-': 'A', '-···': 'B', '-·-·': 'C', '-··': 'D', '·': 'E', '··-·': 'F', '--·': 'G', '····': 'H', '··': 'I', '·---': 'J', '-·-': 'K', '·-··': 'L', '--': 'M', '-·': 'N', '---': 'O', '·--·': 'P', '--·-': 'Q', '·-·': 'R', '···': 'S', '-': 'T', '··-': 'U', '···-': 'V', '·--': 'W', '-··-': 'X', '-·--': 'Y', '--··': 'Z', '·----': '1', '··---': '2', '···--': '3', '····-': '4', '·····': '5', '-····': '6', '--···': '7', '---··': '8', '----·': '9', '-----': '0', '·-·-·-': '.', '---···': ':', '--··--': ',', '-·-·-·': ';', '··--··': '?', '-···-': '=', '·----·': "'", '-··-·': '/', '-·-·--': '!', '-····-': '-', '··--·-': '_', '·-··-·': '"', '-·--·': '(', '-·--·-': ')', '···-··-': '$', '·-···': '&', '·--·-·': '@', '·-·-·': '+'}
	def encode(self, src_text):
		result = ''
		src_text = src_text.upper()
		for single_char in src_text:
			result += self.morse_dict.get(single_char, '\\') + ' '
		return result
	
	def decode(self, morse_txt):
		result = ''
		for seg in morse_txt.split():
			result += self.morse_dict_r.get(seg, ' ')
		return result


#平滑莫尔斯编码解码类（未完成）
class smoothMorseCodec(morseCodec):
	def __init__(self):
		morseCodec.__init__(self)
		pass

	def encode(self, src_text):
		result = ''
		src_text = src_text.upper()
		for single_char in src_text:
			result += self.morse_dict.get(single_char, '\\')
		return result
	
	def decode(self, morse_txt):
		result = ''
		for seg in morse_txt.split('\\'):
			result += self.morse_dict_r.get(seg, ' ')
		return result

my_smooth_morse = smoothMorseCodec()
#print(my_smooth_morse.encode('I love you').replace('\\', ''))

#递归方式实现平滑莫尔斯电码片段的解码
max_moorse_len = max([len(k) for k in morse_dict_r])

def guess_morse(morse_seg, cur_morse, cur_start, result):
	for end in range(cur_start + 1, min(cur_start + max_moorse_len + 1, len(morse_seg) + 1)):
		single_char = morse_dict_r.get(morse_seg[cur_start:end], None) #对切片尝试进行解码
		if single_char:
			if end == len(morse_seg): #解码至串末尾递归结束
				result.append(cur_morse + single_char)
				break
			else:
				guess_morse(morse_seg, cur_morse + single_char, end, result) # 递归解码剩余部分
	if cur_start == 0:
		return result

result = guess_morse('·--··-······-·-·--··----·', '', 0, [])
#print(len(result))

#用词典进行筛选
word_set = {}
num = 0
with open('google-10000-english.txt') as f:
	for word in f.read().split():
		num += 1
		word_set[word.upper()] = num

#print(set([1, 2, 3]))
#print(len(word_set))

#用四种方法实现筛选
#for word in result:	#循环遍历方式
#	if word in word_set:
#		print(word, word_set[word])

#print([word for word in result if word in word_set]) #列表推导
#list(filter(lambda x: x in word_set, result)) #利用filter()函数
#set(result) & word_set #利用集合运算

all_word_dict = {}
my_smooth_morse = smoothMorseCodec()

with open('words.txt') as f:
	for word in f.read().split():
		all_word_dict[my_smooth_morse.encode(word)] = word.upper()

def guess_morse_new(morse_seg):
	if morse_seg in all_word_dict:
		print(all_word_dict[morse_seg])
	else:
		print('N/A')

#guess_morse_new('·--··-······-·-·--··----·')

word_dict = {}
with open('google-10000-english.txt') as f:
	for word in f.read().split()[:3000]:
		word_dict[my_smooth_morse.encode(word)] = word

#添加缺失单词
word_dict[my_smooth_morse.encode('i')] = 'i'

#单词级递归解码
max_moorse_len = max([len(k) for k in word_dict])
min_moorse_len = min([len(k) for k in word_dict])

def guess_morse(morse_seg, cur_morse, cur_start, result, depth):
	for end in range(cur_start + min_moorse_len, min(cur_start + max_moorse_len + 1, len(morse_seg) + 1)):
		single_word = word_dict.get(morse_seg[cur_start:end], None) #对切片尝试解码
		if single_word:
			if end == len(morse_seg): #解码至串末尾递归结束
				result.append(cur_morse + ' ' + single_word)
				break
			elif depth <= 7:
				guess_morse(morse_seg, cur_morse + ' ' + single_word, end, result, depth + 1) #递归解码剩余部分
	if cur_start == 0:
		return result
result = guess_morse('···-··---···-·-·-----··-', '', 0, [], 0)
#print(len(result))

result_ = []
for item in result:
	result_.append((len(item.split()), item))
result_ = sorted(result_)
'I' in word_dict.values()
#print(result_[:30])

#用递归实现反向最大匹配解码
max_moorse_len = max([len(k) for k in word_dict])
min_moorse_len = min([len(k) for k in word_dict])

def guess_morse_reverse_max_len(morse_seg, if_add_space=False):
	if morse_seg == '':
		return ''
	else:
		for start in range(max(len(morse_seg) - max_moorse_len, 0), len(morse_seg)):
			single_word = word_dict.get(morse_seg[start:], None)
			if single_word:
				break
		print(morse_seg[:start], single_word)
		return guess_morse_reverse_max_len(morse_seg[:start], True) + single_word + (' ' if if_add_space else '')

#result = guess_morse_reverse_max_len('···-··---···-·-······-----·-··-··-··')
#print(result)

#result = guess_morse_reverse_max_len('···-··---···-·')

morse_seg = ''.join([chr(i) for i in range(ord('A'), ord('z')+1)])
#print(len(morse_seg))
#print(morse_seg)

#for start in range(max(len(morse_seg) - max_moorse_len, 0), len(morse_seg)):
#	print(morse_seg[start:], len(morse_seg[start:]))



import requests
req = requests.get('https://wap.zol.com.cn/top/cell_phone/hot.html')

#用正则表达式实现信息提取
import re
result = re.findall(
	'<p class="pro-info-name f28">(.*?)<\/p>[\S\s]*?<span class="pro-info-price f24">(.*?)<\/span>',
	req.text
)

#保存爬取信息
with open('mobile.txt', 'w') as f:
	for item in result:
		f.write(item[0] + ' ' + item[1] + '\n')


