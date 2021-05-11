print('# 用字典实现的表-表随机加密')
import random

alphabet_src = [chr(i) for i in range(33, 127)]
alphabet_tar = alphabet_src.copy()
random.shuffle(alphabet_tar)
alphabet_s2t_dict = dict()
alphabet_t2s_dict = dict()
for i in range(len(alphabet_src)):
	alphabet_s2t_dict[alphabet_src[i]] = alphabet_tar[i]
	alphabet_t2s_dict[alphabet_tar[i]] = alphabet_src[i]

def convert_char(single_char: str, operation: str) -> str:
	'''对单个字符进行加密
	输入参数：
	single_char: 要加密的单个字符
	operation: 加密还是解密，encrypt->加密, decrypt->解密
	返回结果：加密/解密后的单个字符
	'''
	global alphabet_src, alphabet_tar

	result = ''
	if ord(single_char) >= 33 and ord(single_char) <= 126:
		if operation == 'encrypt':
			result = alphabet_s2t_dict[single_char]
		elif operation == 'decrypt':
			result = alphabet_t2s_dict[single_char]
	else:
		result = single_char
	return result

def encrypt_it(src_str: str) -> str:
	'''用于对字符串进行简单替换加密
	输入参数：
	src_str: 原始文本内容
	返回结果：加密/解密文本
	'''
	encrypted_str = ''
	for single_char in src_str:
		encrypted_str += convert_char(single_char, 'encrypt')
	return encrypted_str

def decrypt_it(encrypted_str: str) -> str:
	'''用于对字符串进行简单替换解密
	输入参数：
	encrypted_str: 加密文本内容
	返回结果：解密文本
	'''
	decrypted_str = ''
	for single_char in encrypted_str:
		decrypted_str += convert_char(single_char, 'decrypt')
	return decrypted_str

#对两个函数互反性进行验证
assert(decrypt_it(encrypt_it('AbCdefgH!')) == 'AbCdefgH!')


print('# 类化的改造：对紧密联系的函数和变量进行封装')
import random

class CryptIt:
	""" """
	alphabet_src = [chr(i) for i in range(33, 127)]
	alphabet_tar = alphabet_src.copy()
	alphabet_s2t_dict = dict()
	alphabet_t2s_dict = dict()

	def __init__(self):
		random.shuffle(self.alphabet_tar)
		for i in range(len(self.alphabet_src)):
			self.alphabet_s2t_dict[self.alphabet_src[i]] = self.alphabet_tar[i]
			self.alphabet_t2s_dict[self.alphabet_tar[i]] = self.alphabet_src[i]

	def convert_char(self, single_char: str, operation: str) -> str:
		'''对单个字符进行加密
		输入参数：
		single_char: 要加密的单个字符
		operation: 加密还是解密，encrypt->加密, decrypt->解密
		返回结果：加密/解密后的单个字符
		'''
		result = ''
		if ord(single_char) >= 33 and ord(single_char) <= 126:
			if operation == 'encrypt':
				result = self.alphabet_s2t_dict[single_char]
			elif operation == 'decrypt':
				result = self.alphabet_t2s_dict[single_char]
		else:
			result = single_char
		return result

	def encrypt_it(self, src_str: str) -> str:
		'''用于对字符串进行简单替换加密
		输入参数：
		src_str: 原始文本内容
		返回结果：加密/解密文本
		'''
		encrypted_str = ''
		for single_char in src_str:
			encrypted_str += self.convert_char(single_char, 'encrypt')
		return encrypted_str

	def decrypt_it(encrypted_str: str) -> str:
		'''用于对字符串进行简单替换解密
		输入参数：
		encrypted_str: 加密文本内容
		返回结果：解密文本
		'''
		decrypted_str = ''
		for single_char in encrypted_str:
			decrypted_str += self.convert_char(single_char, 'decrypt')
		return decrypted_str

print('# alphabet_tar是可变类型，作为类变量为所有实例共享，会造成逻辑问题')
my_crypt_a = CryptIt()
print(my_crypt_a.encrypt_it('AbCdefgH'))
my_crypt_b = CryptIt()
print(my_crypt_b.encrypt_it('AbCdefgH'))
print(my_crypt_a.encrypt_it('AbCdefgH'))

print("# 前后两次调用 my_crypt_a.encryptit('AbCdefgH') 结果不同，所以将可变类型类变量改成\_init__()里初始化的实例变量")
import random

class CryptIt:
	""" """
	def __init__(self):
		self.alphabet_src = [chr(i) for i in range(33, 127)]
		self.alphabet_tar = self.alphabet_src.copy()
		self.alphabet_s2t_dict = dict()
		self.alphabet_t2s_dict = dict()
		random.shuffle(self.alphabet_tar)
		for i in range(len(self.alphabet_src)):
			self.alphabet_s2t_dict[self.alphabet_src[i]] = self.alphabet_tar[i]
			self.alphabet_t2s_dict[self.alphabet_tar[i]] = self.alphabet_src[i]

	def convert_char(self, single_char: str, operation: str) -> str:
		'''对单个字符进行加密
		输入参数：
		single_char: 要加密的单个字符
		operation: 加密还是解密，encrypt->加密, decrypt->解密
		返回结果：加密/解密后的单个字符
		'''
		result = ''
		if ord(single_char) >= 33 and ord(single_char) <= 126:
			if operation == 'encrypt':
				result = self.alphabet_s2t_dict[single_char]
			elif operation == 'decrypt':
				result = self.alphabet_t2s_dict[single_char]
		else:
			result = single_char
		return result

	def encrypt_it(self, src_str: str) -> str:
		'''用于对字符串进行简单替换加密
		输入参数：
		src_str: 原始文本内容
		返回结果：加密/解密文本
		'''
		encrypted_str = ''
		for single_char in src_str:
			encrypted_str += self.convert_char(single_char, 'encrypt')
		return encrypted_str

	def decrypt_it(self, encrypted_str: str) -> str:
		'''用于对字符串进行简单替换解密
		输入参数：
		encrypted_str: 加密文本内容
		返回结果：解密文本
		'''
		decrypted_str = ''
		for single_char in encrypted_str:
			decrypted_str += self.convert_char(single_char, 'decrypt')
		return decrypted_str
	
	def assert_crypt(self):
		assert(self.decrypt_it(self.encrypt_it('AbCdefgH!')) == 'AbCdefgH!')
		print('Assertion OK!')

my_crypt = CryptIt()
my_crypt.assert_crypt()
print(my_crypt.encrypt_it('AbCdefgH!'))
print(my_crypt.decrypt_it('?#7,eIGp$'))
my_crypt_a = CryptIt()
print(my_crypt_a.encrypt_it('AbCdefgH!'))
print(my_crypt.encrypt_it('AbCdefgH!'))
print(my_crypt.decrypt_it('?#7,eIGp$'))

