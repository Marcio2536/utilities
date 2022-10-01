import datetime
import yaml
def exception(year,dayofyr):
	global exceptdate
	givendate = datetime.datetime(year, 1, 1) + datetime.timedelta(dayofyr - 1)
	for i in range(len(exceptdate)):
		tempdate = datetime.datetime(exceptdate[i][0],exceptdate[i][1],exceptdate[i][2])
		if tempdate == givendate:
			return True
	return False
def readconfig():
	global exceptdate,skiprange
	with open('config.yaml', 'r') as file:
		yml = yaml.safe_load(file)
	exceptls = yml['exceptdate']
	exceptdate = []
	for i in range(len(exceptls)):
		yyyy, mm, dd = exceptls[i].split('/')
		exceptdate.append([int(yyyy),int(mm),int(dd)])
	rangels = yml['skiprange']
	skiprange = []
	for i in range(len(rangels)):
		yyyy, mm, dd, dayofrange = rangels[i].split('/')
		skiprange.append([int(yyyy),int(mm),int(dd),int(dayofrange)])
def writeics(py,pm,pd,ey,em,ed,schday):
	global ics
	context = 'BEGIN:VEVENT\n'
	context += 'DTSTART;VALUE=DATE:' + py + pm + pd + '\nDTEND;VALUE=DATE:' + ey + em + ed + '\nTRANSP:TRANSPARENT\nSUMMARY:Day ' + str(schday) + '\nEND:VEVENT\n'
	ics.write(context)
def skipday(year,dayofyr):
	#skiprange = [[2022,12,22,12],[2023,1,19,11],[2023,2,18,5],[2023,4,5,12],[2023,5,25,4],[2023,6,6,23],[2023,7,5,5],[2023,7,14,48]]
	givendate = datetime.datetime(year, 1, 1) + datetime.timedelta(dayofyr - 1)
	for i in range(len(skiprange)):
		tempdate = datetime.datetime(skiprange[i][0],skiprange[i][1],skiprange[i][2])
		if tempdate == givendate:
			return skiprange[i][3]
	return 1
def checkweek(year,dayofyr):
	tempdate = datetime.datetime(year, 1, 1) + datetime.timedelta(dayofyr - 1)
	if (int(tempdate.strftime("%u")) == 6)or (int(tempdate.strftime("%u")) == 7):
		return False
	else:
		return True
def main():
	global initdate, ics, exceptdate
	schtuple = (1,2,3,4,5,6)
	schday = iter(schtuple)
	#exceptdate = [[2022,9,12],[2022,10,3],[2022,10,4],[2022,11,3],[2022,11,4],[2022,12,1],[2023,1,5],[2023,1,6],[2023,5,1],[2023,5,18],[2023,5,30],[2023,7,12]]
	ics = open('schday.ics','at')
	print('Enter the date you want the calendar to start from (Format: 2022 9 2) ')
	try:
		yyyy, mm, dd = map(int,input().split())
	except:
		yyyy = 2022
		mm = 9
		dd = 2
	ics.write('BEGIN:VCALENDAR\nPRODID:-//Pythonista\nVERSION:2.0\nCALSCALE:GREGORIAN\nX-WR-TIMEZONE:Asia/Hong_Kong\nX-WR-CALNAME:School Day\nX-WR-CALDESC:School Day\n')
	readconfig()
	initdate = datetime.datetime(yyyy,mm,dd)
	currentyr = datetime.datetime(yyyy,12,31)
	endmonth = datetime.datetime(yyyy+1,8,31)
	daynum = int(initdate.strftime("%j"))
	yearofday = int(currentyr.strftime("%j"))
	endsummer = int(endmonth.strftime("%j"))
	i = daynum
	while  i != endsummer:
		if checkweek(yyyy,i) and (not exception(yyyy,i)) and (skipday(yyyy,i)==1):
			printdate = datetime.datetime(yyyy, 1, 1) + datetime.timedelta(i - 1)
			endate = printdate.date() + datetime.timedelta(days=1)		
			i += 1
			try:					
				writeics(printdate.strftime('%Y'),printdate.strftime('%m'),printdate.strftime('%d'),endate.strftime('%Y'),endate.strftime('%m'),endate.strftime('%d'),next(schday))
			except:
				schday = iter(schtuple)
				writeics(printdate.strftime('%Y'),printdate.strftime('%m'),printdate.strftime('%d'),endate.strftime('%Y'),endate.strftime('%m'),endate.strftime('%d'),next(schday))
		else:
			i += skipday(yyyy,i)
		if i >= yearofday:
			yyyy += 1
			i -= yearofday
	ics.write('END:VCALENDAR')
	ics.close()
main()
