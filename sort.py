#!/usr/bin/env python3
import re
def sort_key(s):
	if s:
		try:
			#c = re.findall('\d+$', s)[0]
			tp = re.findall(r'group\d+', s)[0]
			#print ( tp )
			c = re.findall(r'\d+', tp)[0]
		except:
			c = -1
		return int(c)

def strsort(alist):
	#alist.sort(key=sort_key, reverse=True)
	alist.sort(key=sort_key, reverse=False)
	return alist

#A = ['abc 15','abd 13','abe 9','abf 6','abg 2']
B = ['/data1/fanwei_group/wanghengchao/project/04.Apolygus_lucorum/01.assembly/06.hic/01.lachesis_out/main_results/group00', '/data1/fanwei_group/wanghengchao/project/04.Apolygus_lucorum/01.assembly/06.hic/01.lachesis_out/main_results/group1', '/data1/fanwei_group/wanghengchao/project/04.Apolygus_lucorum/01.assembly/06.hic/01.lachesis_out/main_results/group12', '/data1/fanwei_group/wanghengchao/project/04.Apolygus_lucorum/01.assembly/06.hic/01.lachesis_out/main_results/group2']
#print( strsort( A ) )
print( strsort( B ) )
