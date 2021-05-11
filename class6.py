print('# 上节课最后版本：独立出的convert_char函数')
def convert_char(single_char: str, operation: str) -> str:
	'''对单个字符进行加密
	输入参数：
	single_char: 要加密的单个字符
	operation: 加密还是解密, encrypt->加密, decrypt->解密
	返回结果：加密/解密后的单个字符
	'''
	ALPHABET_SRC = 'abcdefghijklmnopqrstuvwxyz'
	ALPHABET_TAR = 'defghijklmnopqrstuvwxyzabc'

	result = ''
	if single_char in ALPHABET_SRC:
		if operation == 'encrypt':
			result = ALPHABET_TAR[ALPHABET_SRC.index(single_char)]
		elif operation == 'decrypt':
			result = ALPHABET_SRC[ALPHABET_TAR.index(single_char)]
	else:
		result = single_char
	return result

def encrypt_it(src_str: str) -> str:
	'''用于对字符串进行简单加密
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
	encyrpted_str: 加密文本内容
	返回结果：解密文本
	'''
	decrypted_str = ''
	for single_char in encrypted_str:
		decrypted_str += convert_char(single_char, 'decrypt')
	return decrypted_str

print('对两个函数进行互反性验证')
assert(decrypt_it(encrypt_it('AbCdefgH!')) == 'AbCdefgH!')


print('# 字母表位置偏移法实现')
def convert_char(single_char: str, operation: str) -> str:
	'''对单个字符进行加密
	输入参数：
	single_char: 要加密的单个字符
	opeartion: 加密还是解密，encrypt->加密, decrypt->解密
	返回结果：加密/解密后的单个字符
	'''
	OFFSET = 10
	ALPHABET_SRC = 'abcdefghijklmnopqrstuvwxyz'

	result = ''
	if single_char in ALPHABET_SRC:
		if operation == 'encrypt':
			result = ALPHABET_SRC[(ALPHABET_SRC.index(single_char) + OFFSET) % 26]
		elif operation == 'decrypt':
			result = ALPHABET_SRC[(ALPHABET_SRC.index(single_char) - OFFSET) % 26]
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

def decrypt_it(encryped_str: str) -> str:
	'''用于对字符串进行简单替换解密
	输入参数：
	encrypted_str: 加密文本内容
	返回结果：解密文本
	'''
	decryped_str = ''
	for single_char in encryped_str:
		decryped_str += convert_char(single_char, 'decrypt')
	return decryped_str

print('对两个函数互反性进行验证')
assert(decrypt_it(encrypt_it('AbCdefgH!')) == 'AbCdefgH!')

print('# ASCII偏移置换实现(ASCII范围：33-126)')
def convert_char(single_char: str, operation: str) -> str:
	'''对单个字符进行加密
	输入参数：
	single_char: 要加密的单个字符
	opeartion: 加密还是解密，encrypt->加密, decrypt->解密
	返回结果：加密/解密后的单个字符
	'''
	OFFSET = 10

	result = ''
	if ord(single_char) >= 33 and ord(single_char) <= 126:
		if operation == 'encrypt':
			result = chr((ord(single_char) - 33 + OFFSET) % (126 - 33 + 1) + 33)
		elif operation == 'decrypt':
			result = chr((ord(single_char) - 33 - OFFSET) % (126 - 33 + 1) + 33)
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

def decrypt_it(encryped_str: str) -> str:
	'''用于对字符串进行简单替换解密
	输入参数：
	encrypted_str: 加密文本内容
	返回结果：解密文本
	'''
	decryped_str = ''
	for single_char in encryped_str:
		decryped_str += convert_char(single_char, 'decrypt')
	return decryped_str

print('对两个函数互反性进行验证')
assert(decrypt_it(encrypt_it('AbCdefgH!')) == 'AbCdefgH!')

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
