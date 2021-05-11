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
