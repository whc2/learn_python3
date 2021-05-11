print('# 先用顺序代码实现串到川的加密/解密')
alphabet_src = 'abcdefghijklmnopqrstuvwxyz'
alphabet_tar = 'defghijklmnopqrstuvwxyzabc'

src_str = 'hello world!'

encrypted_str = ''
for single_char in src_str:
	if single_char in alphabet_src:
		index = alphabet_src.index(single_char)
		encrypted_str = encrypted_str + alphabet_tar[index]
	else:
		encrypted_str = encrypted_str + single_char
print(encrypted_str)

decrypted_str = ''
for single_char in encrypted_str:
	if single_char in alphabet_src:
		index = alphabet_tar.index(single_char)
		decrypted_str = decrypted_str + alphabet_src[index]
	else:
		decrypted_str = decrypted_str + single_char
print(decrypted_str)

print('# 为了改善可读性、方便重用、隔离命名空间，做函数化改造')
def encryptIt(src_str):
	global alphabet_src, alphabet_tar
	encrypted_str = ''
	for single_char in src_str:
		if single_char in alphabet_src:
			index = alphabet_src.index(single_char)
			encrypted_str = encrypted_str + alphabet_tar[index]
		else:
			encrypted_str = encrypted_str + single_char
	return encrypted_str

print(encryptIt('hello world!'))

def decryptIt(encrypted_str):
	global alphabet_src, alphabet_tar
	decrypted_str = ''
	for single_char in encrypted_str:
		if single_char in alphabet_tar:
			index = alphabet_tar.index(single_char)
			decrypted_str = decrypted_str + alphabet_src[index]
		else:
			decrypted_str = decrypted_str + single_char
	return decrypted_str

print(decryptIt('khoor zruog!'))

print(decryptIt(encryptIt('hello world!')))

print("# 函数对命名空间的隔离")
a = 1

def mytest():
	a = 2
	print(a)

mytest()
print(a)

print('# 用断言验证加密解密函数功能是否正常')
assert(decryptIt(encryptIt('AbCdefgH!')) == 'AbCdefgH!')

print('# 为函数增加文档字符串（用help时显示的帮助信息）')
def encryptIt(src_str):
	'''用于对字符串进行简单替换加密
	输入参数：
	src_str: 原始文本内容
	返回结果：加密/解密文本
	'''
	global alphabet_src, alphabet_tar
	encrypted_str = ''
	for single_char in src_str:
		if single_char in alphabet_src:
			index = alphabet_src.index(single_char)
			encrypted_str = encrypted_str + alphabet_tar[index]
		else:
			encrypted_str = encrypted_str + single_char
	return encrypted_str

def decryptIt(encrypted_str):
	'''用于对字符串进行简单替换解密
	输入参数：
	encrypted_str: 加密文本内容
	返回结果：解密文本
	'''
	global alphabet_src, alphabet_tar
	decrypted_str = ''
	for single_char in encrypted_str:
		if single_char in alphabet_tar:
			index = alphabet_tar.index(single_char)
			decrypted_str = decrypted_str + alphabet_src[index]
		else:
			decrypted_str = decrypted_str + single_char
	return decrypted_str

#print(help(encryptIt))
print('# 对两个函数进行验证')
assert(decryptIt(encryptIt('AbCdefgH!')) == 'AbCdefgH!')

print('# 为了出现异常时方便调试，可以使用pdb魔法指令')
#%pdb

print('# 把两个函数合并成一个，并改成索引位置平移法实现')
def cryptIt(src_str: str, if_decrypt: bool=False) -> str:
	'''用于对字符串进行简单替换加密/解密
	输入参数：
	src_str: 原始文本内容
	if_decrypt: True表示解密过程, False表示加密过程
	返回结果: 加密/解密文本
	'''
	global alphabet_src
	result = ''
	for single_char in src_str:
		if single_char in alphabet_src:
			old_index = alphabet_src.index(single_char)
			if if_decrypt == True:
				new_index = (old_index - 3) % 26
			else:
				new_index = (old_index + 3) % 26
			result = result + alphabet_src[new_index]
		else:
			result = result + single_char
	return result

assert('abcdefghijklmnopqrstuvwxyz!' == cryptIt(cryptIt('abcdefghijklmnopqrstuvwxyz!'), True))

print(cryptIt('I love you!'))
print(cryptIt('I oryh brx!', True))

print('# 对函数实现行数进行缩减（条件选择赋值语句+续行）')
def crypt_it(src_str: str, if_decrypt: bool=False) -> str:
	'''用于对字符串进行简单替换加密/解密
	输入参数：
	src_str: 原始文本内容
	if_decrypt: True表示解密过程，False表示加密过程
	返回结果：加密/解密文本
	'''
	global alphabet_src
	result = ''
	for single_char in src_str:
		if single_char in alphabet_src:
			#字符串替换
			new_index = (alphabet_src.index(single_char) - 3) % 26 \
				if if_decrypt is True \
				else (alphabet_src.index(single_char) + 3) % 26 
			result += alphabet_src[new_index]
		else:
			result += single_char
	return result

assert('abcdefghijklmnopqrstuvwxyz!' == crypt_it(crypt_it('abcdefghijklmnopqrstuvwxyz!'), True))

print(crypt_it('I love you!'))
print(crypt_it('I oryh brx!', True))


print('# 行数进一步缩减')
def crypt_it(src_str: str, if_decrypt: bool=False) -> str:
	'''用于对字符串进行简单替换加密/解密
	输入参数：
	src_str: 原始文本内容
	if_decrypt: True表示解密过程，False表示加密过程
	返回结果：加密/解密文本
	'''
	global alphabet_src
	result = []
	for single_char in src_str:
		if single_char in alphabet_src:
			#字符串替换
			new_index = (alphabet_src.index(single_char) - 3) % 26 \
				if if_decrypt is True \
				else (alphabet_src.index(single_char) + 3) % 26 
			result.append(alphabet_src[new_index])
		else:
			result.append(single_char)
	return ''.join(result)

assert('abcdefghijklmnopqrstuvwxyz!' == crypt_it(crypt_it('abcdefghijklmnopqrstuvwxyz!'), True))

print(crypt_it('I love you!'))
print(crypt_it('I oryh brx!', True))


print('# 再缩减')
def crypt_it(src_str: str, if_decrypt: bool=False) -> str:
	'''用于对字符串进行简单替换加密/解密
	输入参数：
	src_str: 原始文本内容
	if_decrypt: True表示解密过程，False表示加密过程
	返回结果：加密/解密文本
	'''
	global alphabet_src
#	result = []
#	for single_char in src_str:
#		result.append(alphabet_src[(alphabet_src.index(single_char) - 3) % 26 \
#			if if_decrypt is True \
#			else (alphabet_src.index(single_char) + 3) % 26] if \
#			single_char in alphabet_src else single_char)
	result = [alphabet_src[(alphabet_src.index(single_char) - 3) % 26 \
				if if_decrypt is True \
				else (alphabet_src.index(single_char) + 3) % 26] if \
				single_char in alphabet_src else single_char \
				for single_char in src_str]
	return ''.join(result)

assert('abcdefghijklmnopqrstuvwxyz!' == crypt_it(crypt_it('abcdefghijklmnopqrstuvwxyz!'), True))

print(crypt_it('I love you!'))
print(crypt_it('I oryh brx!', True))


print('# 最终缩减版本')
def crypt_it(src_str: str, if_decrypt: bool=False) -> str:
	'''用于对字符串进行简单替换加密/解密
	输入参数：
	src_str: 原始文本内容
	if_decrypt: True表示解密过程，False表示加密过程
	返回结果：加密/解密文本
	'''
	global alphabet_src
	return ''.join([alphabet_src[(alphabet_src.index(single_char) - 3) % 26 \
				if if_decrypt is True \
				else (alphabet_src.index(single_char) + 3) % 26] if \
				single_char in alphabet_src else single_char \
				for single_char in src_str])

assert('abcdefghijklmnopqrstuvwxyz!' == crypt_it(crypt_it('abcdefghijklmnopqrstuvwxyz!'), True))

print(crypt_it('I love you!'))
print(crypt_it('I oryh brx!', True))


print('# 设计convert_char函数，通过局部重用，缩减行数的同时提高可读性')
alphabet_src = 'abcdefghijklmnopqrstuvwxyz'
alphabet_tar = 'defghijklmnopqrstuvwxyzabc'

def convert_char(single_char, operation):
	global alphabet_src, alphabet_tar
	result = ''
	if single_char in alphabet_src:
		if operation == 'encrypt':
			result = alphabet_tar[alphabet_src.index(single_char)]
		elif operation == 'decrypt':
			result = alphabet_src[alphabet_tar.index(single_char)]
	else:
		result = single_char
	return result

def encrypt_it(src_str: str) -> str:
	'''用于对字符串进行简单替换加密
	输入参数：
	src_str: 原始文本内容
	返回结果：加密文本
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

print('#对两个函数进行互反性验证')
assert(decrypt_it(encrypt_it('AbCdefgH!')) == 'AbCdefgH!')

print(encrypt_it('hello world!'))
print(decrypt_it('khoor zruog!'))

