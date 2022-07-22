# Original Repo: https://github.com/MCL7D9/RoBoMaster
from ast import Pass
from itertools import permutations
import  time
enter=input("Enter 4 number and a sign: ")
startime = time.time()
sign=enter[4]
ele=[0,0,0,0]
ddg_list =[]
enter_list=[0,0,0,0]
reslt=0
solution=""
matched = False
length=0
def analyze():
	global length
	for i in range(4):
		enter_list[i]=enter[i]
		ele[i] = int(enter[i])
	for i in range(4):
		for j in range(4):
			if i != j:
				enter_list.append(str(enter_list[i])+str(enter_list[j]))
				ddg_list.append(str(enter_list[i])+str(enter_list[j]))
	length = len(enter_list)
	for i in range(length):
		enter_list[i]=int(enter_list[i])
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
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	plist=enter_list
	length=len(plist)
	plist.sort(reverse=True)
	i = 0
	#A+B+C+D
	if a+b+c+d ==24:
		print('index: 0+1+2+3=24')
		matched = True
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
	# AB + C + D
	if not matched:
		temp = str(ele[0]) + str(ele[1]) + str(ele[2]) + str(ele[3])
		templist = list(p for p in permutations(temp, 2))
		templist = [item for t in templist for item in t]
		for i in range(len(templist)):
			templist[i] = int(templist[i])
		for i in range(12):
			tempsum = templist[2*i]*10 + templist[2*i + 1]
			tempele = ele
			try:
				for k in range(4):
					if templist[2*i] == ele[k]:
						tempele.pop(k)
			except:
				pass
			try:
				for k in range(len(tempele)):
					if templist[2*i + 1] == ele[k]:
						tempele.pop(k)
			except:
				pass
			tempsum2 = 0
			for k in range(len(tempele)):
				tempsum2 += tempele[k]
			if tempsum + tempsum2 == 24:
				print(tempsum,'+',tempele[0],'+',tempele[1],'= 24')
				matched = True
				break
	while not matched:
		if plist[0]>24:
			del plist[0]
		else:
			matched = True
		solution = ""
		for i in range(len(plist)):
			for j in range(len(plist)):
				reslt=plist[i]+plist[j]
				if reslt==24:
						solution= str(plist[i]) + ' + ' + str(plist[j]) +' = 24'
						break
		print(solution)
def minus():
	global matched
	mlist=enter_list
	length=len(mlist)
	mlist.sort(reverse=True)
	i = 0
	solution = ""
	# AB - C - D
	if not matched:
		temp = str(ele[0]) + str(ele[1]) + str(ele[2]) + str(ele[3])
		templist = list(p for p in permutations(temp, 2))
		templist = [item for t in templist for item in t]
		for i in range(len(templist)):
			templist[i] = int(templist[i])
		for i in range(12):
			tempsum = templist[2*i]*10 + templist[2*i + 1]
			tempele = ele
			try:
				for k in range(4):
					if templist[2*i] == ele[k]:
						tempele.pop(k)
			except:
				pass
			try:
				for k in range(len(tempele)):
					if templist[2*i + 1] == ele[k]:
						tempele.pop(k)
			except:
				pass
			tempsum2 = 0
			for k in range(len(tempele)):
				tempsum2 += tempele[k]
			if tempsum - tempsum2 == 24:
				print(tempsum,'-',tempele[0],'-',tempele[1],'= 24')
				matched = True
				break
	
	# A - B
	if not matched:
		for i in range(length):
			for j in range(length):
				if mlist[i] > mlist[j]:
					reslt=mlist[i] - mlist[j]
					if reslt==24:
						solution= str(mlist[i]) + ' - ' + str(mlist[j]) +' = 24'
						break
		print(solution)
def multi():
	global ele
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	index = 0
	# A*B*C*D
	if matched:
		index = 1
	if (a * b * c * d == 24):
		print(a,'*', b,'*', c,'*', d,'= 24')
		index = 1
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
	#A*B
	if index == 0:
		for i in range(4):
			for j in range(4):
				if (i < j):
					if ele[i] * ele[j] == 24:
						print(i,'*',j,'= 24')
						index = 1
						break
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
