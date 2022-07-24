from ast import Pass
from itertools import permutations
import time
import random
import re
enter = input("Enter a sign and 4 numbers (eg: *8964, +2318) : ")
startime = time.time()
sign = enter[0]
enter = enter[slice(1,5)]
ele = [0,0,0,0]
ddg_list = []
enter_list = [0,0,0,0]
solution = ""
matched = False
length = 0
def analyze():
	global length
	for i in range(4):
		enter_list[i]=int(enter[i])
		ele[i] = int(enter[i])
	for i in range(4):
		for j in range(4):
			if i != j:
				enter_list.append(int(str(enter_list[i])+str(enter_list[j])))
				ddg_list.append(int(str(enter_list[i])+str(enter_list[j])))
	length = len(enter_list)
	if sign=="+":
		pass
		plus()
	elif sign=="-":
		pass
		minus()
	elif sign=="*":
		pass
		multi()
	else:
		pass
		divid()
def plus():
	global ele, matched
	tempstr = str(ele[0]) + str(ele[1]) + str(ele[2]) + str(ele[3])
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	if ele == [2,2,2,2]:
		print('2 + 22 = 24')
		matched = True
	plist=enter_list
	length=len(plist)
	plist.sort(reverse=True)
	i = 0
		# Others 
	if not matched:
		# 3 repeated numbers
		if (len(re.findall(str(a),tempstr)) == 3 and re.findall(str(a),tempstr) == ['2','2','2']) or ((re.findall(str(a),tempstr) == ['2','2','2']) and  (len(re.findall(str(b),tempstr)) == 3)):
			print('2 + 22 = 24')
			matched = False
		if (len(re.findall(str(a),tempstr)) == 3 and re.findall(str(a),tempstr) == ['1','1','1']) or ((re.findall(str(a),tempstr) == ['1','1','1']) and  (len(re.findall(str(b),tempstr)) == 3)):
			print('11 + 13 = 24')
			matched = False
		else:   # AB + C
			for i in range(len(ddg_list)):
				for j in range(4):
					if ddg_list[i] <= 24:
						if ddg_list[i] != 17:
							if ddg_list[i] + ele[j] == 24:
								print(ddg_list[i],'+', ele[j],'= 24')
								matched = True
						elif len(re.findall('7',tempstr)) >= 2:
							if ddg_list[i] + ele[j] == 24:
								print(ddg_list[i],'+', ele[j],'= 24')
								matched = True
					if matched:
						break
	# A+B+C
	if not matched and a+b+c == 24:
		print(a,'+', b, '+', c,'= 24')
		matched = True
	if not matched and a+b+d == 24:
		print(a,'+', b, '+', d,'= 24')
		matched = True
	if not matched and a+c+d == 24:
		print(a,'+', c, '+', d,'= 24')
		matched = True
	if not matched and b+c+d == 24:
		print(b,'+', c, '+', d,'= 24')
		matched = True
	# AB + CD
	if not matched:
		templist = list(str(ele[0]) + str(ele[1]) + str(ele[2]) + str(ele[3]))
		if templist.count('1') == 3 and templist.count('3') == 1:
			print('11 + 13 = 24')
			matched = True
		if templist.count('1') == 2 and templist.count('2') == 2:
			print('12 + 12 = 24')
			matched = True
		if templist.count('1') == 2 and templist.count('4') == 1 and templist.count('0') == 1:
			print('10 + 14 = 24')
			matched = True
	#A+B+C+D
	if (not matched) and (a+b+c+d ==24):
		print(a,'+',b,'+',c,'+',d,'= 24')
		matched = True
	# AB + C + D !! Must be placed in last part of the function !!
	if not matched:
		opo_list = [0,0,0,0]
		for i in range(160):
			opo_list = [ele[0],ele[1],ele[2],ele[3]]
			r1 = random.randint(0,3)
			a1 = opo_list[r1]
			opo_list.pop(r1)
			r2 = random.randint(0,2)
			a2 = opo_list[r2]
			opo_list.pop(r2)
			sum1 = a1 *10 + a2
			r3 = random.randint(0,1)
			a3 = opo_list[r3]
			opo_list.pop(r3)
			a4 = opo_list[0]
			if sum1 + a3 + a4 == 24:
				print(sum1,'+',a3,'+',a4,'= 24')
				matched = True
				break			
def minus():
	global matched
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	tempstr = str(ele[0]) + str(ele[1]) + str(ele[2]) + str(ele[3])
	mlist=enter_list
	mlist.sort(reverse=True)
	i = 0
	solution = "no solution"
	# Others
	if not matched:
		# AB - C
		for i in range(len(ddg_list)):
			for j in range(4):
				if ddg_list[i] >= 24 and ddg_list[i] <= 34:
					if ddg_list[i] != 26:
						if ddg_list[i] - ele[j] == 24:
							print(ddg_list[i],'-', ele[j],'= 24')
							matched = True
							break
					elif len(re.findall('2',tempstr)) >= 2:
						if ddg_list[i] - ele[j] == 24:
							print(ddg_list[i],'-', ele[j],'= 24')
							matched = True
							break
		# AB - CD
	if not matched:
		for i in range(len(ddg_list)):
			for j in range(len(ddg_list)): 
				if i != j and ddg_list[i] >=34:
					if (ddg_list[i] // 10 == ddg_list[j] % 10) or (ddg_list[j] // 10 == ddg_list[i] % 10):
						if (ddg_list[i] // 10 == ddg_list[j] % 10) and ele.count(ddg_list[i]//10) < 2:
							continue
						elif (ddg_list[j] // 10 == ddg_list[i] % 10) and ele.count(ddg_list[i]%10) < 2:
							continue
						elif ddg_list[i] - ddg_list[j] == 24:
							print(ddg_list[i],'-', ddg_list[j],'= 24')
							matched = True
							break				
					else:
						if ddg_list[i] - ddg_list[j] == 24:
							print(ddg_list[i],'-', ddg_list[j],'= 24')
							matched = True
							break						
	# AB - C - D !! Must be placed in the last part of the function !!
	if not matched:
		opo_list = [0,0,0,0]
		for i in range(160):
			opo_list = [ele[0],ele[1],ele[2],ele[3]]
			r1 = random.randint(0,3)
			a1 = opo_list[r1]
			opo_list.pop(r1)
			r2 = random.randint(0,2)
			a2 = opo_list[r2]
			opo_list.pop(r2)
			sum1 = a1 *10 + a2
			r3 = random.randint(0,1)
			a3 = opo_list[r3]
			opo_list.pop(r3)
			a4 = opo_list[0]
			if sum1 - a3 - a4 == 24:
				print(sum1,'-',a3,'-',a4,'= 24')
				break
				matched = True		
def multi():
	global ele
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	index = 0
	#A*B
	if index == 0:
		for i in range(4):
			for j in range(4):
				if (i < j):
					if ele[i] * ele[j] == 24:
						print(ele[i],'*',ele[j],'= 24')
						index = 1
						break
				if index == 1:
					break
	# AB*C
	for i in range(4):
		for j in range(4):
			if i != j:
				temp = ele[i] * 10 + ele[j]
				temlist = [a,b,c,d]
				temlist.pop(i)
				if i < j:
					temlist.pop(j-1)
				else:
					temlist.pop(j)
				for k in range(2):
					if temp * temlist[k] == 24:
						index = 1
						print(temp,'*',temlist[k],'= 24')
	# A*B*C=
	if (index == 0) and a*b*c == 24:
		print(a,'*', b, '*', c,'= 24')
		index = 1
	if (index == 0) and a*b*d == 24:
		print(a,'*', b, '*', d,'= 24')
		index = 1
	if (index == 0) and a*c*d == 24:
		print(a,'*', c, '*', d,'= 24')
		index = 1
	if (index == 0) and b*c*d == 24:
		print(b,'*', c, '*', d,'= 24')
		index = 1
	# A*B*C*D
	if (a * b * c * d == 24) and (index == 0):
		print(a,'*', b,'*', c,'*', d,'= 24')
		index = 1
def divid():
	global ele
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	index = 0
	# AB / C
	if index == 0:
		for i in range(len(ddg_list)):
			for j in range(len(ele)):
				if int(ddg_list[i]) / int(ele[j]) == 24:
					print(ddg_list[i],'/',ele[j],'= 24')
					index = 1
					break
	# ABC / D
	temp = str(ele[0]) + str(ele[1]) + str(ele[2]) + str(ele[3])
	if index == 0:
		tridig_list = list(''.join(p) for p in permutations(temp, 3))
		for i in range(len(tridig_list)):
			tridig_list[i] = int(tridig_list[i])
		for i in range(len(tridig_list)):
			for j in range(4):
				if tridig_list[i] / ele[j] == 24:
					print(tridig_list[i],'/',ele[j],'= 24')
					index = 1
					break
analyze()
endtime = time.time()
usedtime = endtime - startime
print(usedtime)
