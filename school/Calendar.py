import datetime
import yaml
def readconfig():
	global exceptdate,skiprange,startdate
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
	startdate = yml['startdate']
def writeics(py,pm,pd,ey,em,ed,schday):
	global ics
	context = 'BEGIN:VEVENT\n'
	context += 'DTSTART;VALUE=DATE:' + py + pm + pd + '\nDTEND;VALUE=DATE:' + ey + em + ed + '\nTRANSP:TRANSPARENT\nSUMMARY:Day ' + str(schday) + '\nEND:VEVENT\n'
	ics.write(context)
def skipday(year,dayofyr):
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
def exception(year,dayofyr):
	global exceptdate
	givendate = datetime.datetime(year, 1, 1) + datetime.timedelta(dayofyr - 1)
	for i in range(len(exceptdate)):
		tempdate = datetime.datetime(exceptdate[i][0],exceptdate[i][1],exceptdate[i][2])
		if tempdate == givendate:
			return True
	return False
def main():
	global initdate, ics, exceptdate
	schtuple = (1,2,3,4,5,6)
	schday = iter(schtuple)
	ics = open('schday.ics','at')
	readconfig()
	yyyy, mm, dd = map(int,startdate.split('/'))	
	ics.write('BEGIN:VCALENDAR\nPRODID:-//Pythonista\nVERSION:2.0\nCALSCALE:GREGORIAN\nX-WR-TIMEZONE:Asia/Hong_Kong\nX-WR-CALNAME:School Day\nX-WR-CALDESC:School Day\n')
	initdate = datetime.datetime(yyyy,mm,dd)
	currentyr = datetime.datetime(yyyy,12,31)
	endmonth = datetime.datetime(yyyy+1,8,31)
	daynum = int(initdate.strftime("%j"))
	yearofday = int(currentyr.strftime("%j"))
	endsummer = (int(endmonth.strftime("%j"))-1) if (yyyy+1) % 4 == 0 else int(endmonth.strftime("%j"))
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
	print('Done')
main()
