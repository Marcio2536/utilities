from itertools import permutations
import random
import re
def analyze(sign,a,b,c,d):
	global ele, enter, ddg_list
	ddg_list = []
	solution = ''
	enter = a + b + c + d
	ele = [int(a),int(b),int(c),int(d)]
	for i in range(4):
		for j in range(4):
			if i != j:
				ddg_list.append(int(str(ele[i])+str(ele[j])))
	if sign=="+":
		solution = plus()
	elif sign=="-":
		solution = minus()
	elif sign=="*":
		solution = multi()
	else:
		solution = divid()
	return solution
def plus():
	global ele, matched, enter, ddg_list
	matched = False
	solution = ''
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	templist = list(str(a) + str(b) + str(c) + str(d))
	if ele == [2,2,2,2]:
		return '2+22'
	if not matched:
		# 3 repeated numbers, will use match cases as not many possible answers
		if (len(re.findall(str(a),enter)) == 3 and re.findall(str(a),enter) == ['2','2','2']) or ((re.findall(str(b),enter) == ['2','2','2']) and  (len(re.findall(str(b),enter)) == 3)):
			return 	'2+22'
			matched = True
		else:   # AB + C eg: 18+6
			for i in range(len(ddg_list)):
				for j in range(4):
					if matched:
						break
					if ddg_list[i] <= 24:
						if ddg_list[i] != 17:
							if ddg_list[i] + ele[j] == 24:
								solution = str(ddg_list[i])+'+'+ str(ele[j])
								matched = True
								return solution
						elif len(re.findall('7',enter)) >= 2:
							if ddg_list[i] + ele[j] == 24:
								return str(ddg_list[i]) + '+' + str(ele[j])
								matched = True
	# A+B+C eg: 7+8+9
	if not matched and a+b+c == 24:
		return str(a)+'+'+str(b)+'+'+str(c)
		matched = True
	if not matched and a+b+d == 24:
		return str(a)+'+'+str(b)+'+'+str(d)
		matched = True
	if not matched and a+c+d == 24:
		return str(a)+'+'+str(c)+'+'+str(d)
		matched = True
	if not matched and b+c+d == 24:
		return str(b)+'+'+str(c)+'+'+str(d)
		matched = True
	# AB + CD eg: 11+13
	if not matched:
		if templist.count('1') == 3 and templist.count('3') == 1:
			return '11+13'
			matched = True
		if templist.count('1') == 2 and templist.count('2') == 2:
			return '12+12'
			matched = True
		if templist.count('1') == 2 and templist.count('4') == 1 and templist.count('0') == 1:
			return '10+14'
			matched = True
	#A+B+C+D eg: 6+6+6+6
	if (not matched) and (a+b+c+d ==24):
		return str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)
		matched = True
	# AB + C + D !! Must be placed in last part of the function !! eg: 19+4+1
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
				return str(sum1)+'+'+str(a3)+'+'+str(a4)
				matched = True
				break			
def minus():
	global matched
	if not matched:
		# AB - C eg: 33-9
		for i in range(len(ddg_list)):
			for j in range(4):
				if matched:
					break
				if ddg_list[i] >= 24 and ddg_list[i] <= 34:
					if ddg_list[i] != 26:
						if ddg_list[i] - ele[j] == 24:
							return str(ddg_list[i])+'-'+ str(ele[j])
							matched = True
					elif len(re.findall('2',enter)) >= 2:
						if ddg_list[i] - ele[j] == 24:
							return str(ddg_list[i])+'-'+ str(ele[j])
							matched = True
	# AB - CD eg: 99-75
	if not matched:
		for i in range(len(ddg_list)):
			for j in range(len(ddg_list)):
				if matched:
					break 
				if i != j and ddg_list[i] >=34:
					if (ddg_list[i] // 10 == ddg_list[j] % 10) or (ddg_list[j] // 10 == ddg_list[i] % 10):
						if (ddg_list[i] // 10 == ddg_list[j] % 10) and ele.count(ddg_list[i]//10) < 2:
							continue
						elif (ddg_list[j] // 10 == ddg_list[i] % 10) and ele.count(ddg_list[i]%10) < 2:
							continue
						elif ddg_list[i] - ddg_list[j] == 24:
							return str(ddg_list[i])+'-'+ str(ddg_list[j])
							matched = True
							break				
					else:
						if ddg_list[i] - ddg_list[j] == 24:
							return str(ddg_list[i])+'-'+str(ddg_list[j])
							matched = True						
	# AB - C - D !! Must be placed in the last part of the function !! eg: 37-5-8 = 24
	if not matched:
		opo_list = [0,0,0,0]
		for i in range(160):
			if matched:
				break
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
				return str(sum1)+'-'+str(a3)+'-'+str(a4)
				matched = True		
def multi():
	global ele
	a = int(ele[0])
	b = int(ele[1])
	c = int(ele[2])
	d = int(ele[3])
	index = 0
	# A * B eg: 6*4
	if index == 0:
		for i in range(4):
			for j in range(4):
				if (i < j):
					if ele[i] * ele[j] == 24:
						return str(ele[i])+'*'+str(ele[j])
						index = 1
				if index == 1:
					break
	# AB * C eg: 12*2
	if index == 0:
		for i in range(4):
			for j in range(4):
				if index == 1:
					break
				if i != j:
					enter = ele[i] * 10 + ele[j]
					temlist = [a,b,c,d]
					temlist.pop(i)
					if i < j:
						temlist.pop(j-1)
					else:
						temlist.pop(j)
					for k in range(2):
						if enter * temlist[k] == 24:
							index = 1
							return str(enter)+'*'+str(temlist[k])
	# A * B * C 6*2*2
	if (index == 0) and a*b*c == 24:
		return str(a) +'*'+ str(b) + '*' + str(c)
		index = 1
	if (index == 0) and a*b*d == 24:
		return str(a) +'*'+ str(b) + '*' + str(d)
		index = 1
	if (index == 0) and a*c*d == 24:
		return str(a) +'*'+ str(c) + '*' + str(d)
		index = 1
	if (index == 0) and b*c*d == 24:
		return str(b) +'*'+ str(c) + '*' + str(d)
		index = 1
	# A * B * C * D eg: 2 * 2 * 2 * 3
	if (a * b * c * d == 24) and (index == 0):
		return str(a) +'*'+ str(b) + '*' + str(c) + '*' + str(d)
		index = 1
def divid():
	global ele
	index = 0
	# AB / C eg: 96/4
	if index == 0:
		for i in range(len(ddg_list)):
			for j in range(len(ele)):
				if index == 1:
					break
				if ddg_list[i] / ele[j] == 24:
					return str(ddg_list[i])+'/'+str(ele[j])
					index = 1
	# ABC / D eg: 216/9
	if index == 0:
		tridig_list = list(''.join(p) for p in permutations(enter, 3))
		for i in range(len(tridig_list)):
			tridig_list[i] = int(tridig_list[i])
		for i in range(len(tridig_list)):
			for j in range(4):
				if index == 1:
					break
				if tridig_list[i] / ele[j] == 24:
					return str(tridig_list[i])+'/'+str(ele[j])
					index = 1
a = analyze('*','2','2','2','3')
print(a)
