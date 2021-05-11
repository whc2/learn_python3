#上次课导入的莫尔斯电码对照表数据
morse_dict = {'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·', 'S': '···', 'T': '-', 'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··', '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····', '6': '-····', '7': '--···', '8': '---··', '9': '----·', '0': '-----', '.': '·-·-·-', ':': '---···', ',': '--··--', ';': '-·-·-·', '?': '··--··', '=': '-···-', "'": '·----·', '/': '-··-·', '!': '-·-·--', '-': '-····-', '_': '··--·-', '"': '·-··-·', '(': '-·--·', ')': '-·--·-', '$': '···-··-', '&': '·-···', '@': '·--·-·', '+': '·-·-·'}

morse_dict_r = {'·-': 'A', '-···': 'B', '-·-·': 'C', '-··': 'D', '·': 'E', '··-·': 'F', '--·': 'G', '····': 'H', '··': 'I', '·---': 'J', '-·-': 'K', '·-··': 'L', '--': 'M', '-·': 'N', '---': 'O', '·--·': 'P', '--·-': 'Q', '·-·': 'R', '···': 'S', '-': 'T', '··-': 'U', '···-': 'V', '·--': 'W', '-··-': 'X', '-·--': 'Y', '--··': 'Z', '·----': '1', '··---': '2', '···--': '3', '····-': '4', '·····': '5', '-····': '6', '--···': '7', '---··': '8', '----·': '9', '-----': '0', '·-·-·-': '.', '---···': ':', '--··--': ',', '-·-·-·': ';', '··--··': '?', '-···-': '=', '·----·': "'", '-··-·': '/', '-·-·--': '!', '-····-': '-', '··--·-': '_', '·-··-·': '"', '-·--·': '(', '-·--·-': ')', '···-··-': '$', '·-···': '&', '·--·-·': '@', '·-·-·': '+'}

#利用字符串追加实现的编码函数
def morse_encode(src_text):
	result = ''
	src_text = src_text.upper()
	for single_char in src_text:
		result += morse_dict.get(single_char, '\\') + ' '
	return result

#利用''.join()字符串拼接实现的编码函数
def morse_encode(src_text):
	result = []
	src_text = src_text.upper()
	for single_char in src_text:
		result.append(morse_dict.get(single_char, '\\') + ' ')
	return ''.join(result)

#用列表推导实现的编码函数
def morse_encode(src_text):
	return ''.join([morse_dict.get(
		single_char, '\\') + ' ' for single_char in src_text.upper()])

#print(morse_encode('I love you'))

#解码函数
def morse_decode(morse_txt):
	result = ''
	for seg in morse_txt.split():
		result += morse_dict_r.get(seg, ' ')
	return result
#print(morse_decode('·· \ ·-·· --- ···- · \ -·-- --- ··-'))


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

my_morse = morseCodec()
#print(my_morse.encode('I love you'))
#print(my_morse.decode('·· \ ·-·· --- ···- · \ -·-- --- ··-'))

#平滑莫尔斯编码解码类（未完成）
class smoothMorseCodec(morseCodec):
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
#print(my_smooth_morse.encode('I love you'))
#print(my_smooth_morse.decode('··\·-··---···-·\-·-----··-'))

#递归方式实现平滑莫尔斯电码片段的解码
max_moorse_len = max([len(k) for k in morse_dict_r])
print(max_moorse_len)
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

result = guess_morse('·-··---···-·', '', 0, [])
print('LOVE' in result)
print(result)
print(len(result))
