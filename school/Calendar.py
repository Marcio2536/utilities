import datetime
import yaml
def readconfig():
	global exceptdate,skiprange,startdate
	with open('config.yaml', 'r') as file:
		yml = yaml.safe_load(file)
	startdate = yml['startdate']
	exceptls = yml['exceptdate'] # Retrieve the dates that are going to be excluded
	exceptdate = []
	for i in range(len(exceptls)):
		yyyy, mm, dd = exceptls[i].split('/')
		exceptdate.append([int(yyyy),int(mm),int(dd)])
	rangels = yml['skiprange'] # Retrieve the range of dates that are going to be ignored
	skiprange = []
	for i in range(len(rangels)):
		yyyy, mm, dd, dayofrange = rangels[i].split('/')
		skiprange.append([int(yyyy),int(mm),int(dd),int(dayofrange)])
def appendics(py,pm,pd,ey,em,ed,schday): # Append the corresponding date and school day to the calendar file
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
def checkweek(year,dayofyr): # Check if the date passed by the main program is weekend or not
	tempdate = datetime.datetime(year, 1, 1) + datetime.timedelta(dayofyr - 1)
	if (int(tempdate.strftime("%u")) == 6)or (int(tempdate.strftime("%u")) == 7):
		return False
	else:
		return True
def exception(year,dayofyr): # Check if the date passed by the main program matches the records on the config file or not  
	global exceptdate
	givendate = datetime.datetime(year, 1, 1) + datetime.timedelta(dayofyr - 1)
	for i in range(len(exceptdate)):
		tempdate = datetime.datetime(exceptdate[i][0],exceptdate[i][1],exceptdate[i][2])
		if tempdate == givendate:
			return True
	return False
def main():
	global initdate, ics, exceptdate
	schtuple = (1,2,3,4,5,6) # Set up a tuple for school day iteration
	schday = iter(schtuple)
	ics = open('schday.ics','at') 
	readconfig() # Retrieve configuration from config.yaml
	yyyy, mm, dd = map(int,startdate.split('/'))	# Retrieve the first record from configuration
	ics.write('BEGIN:VCALENDAR\nPRODID:-//Pythonista\nVERSION:2.0\nCALSCALE:GREGORIAN\nX-WR-TIMEZONE:Asia/Hong_Kong\nX-WR-CALNAME:School Day\nX-WR-CALDESC:School Day\n')
	initdate = datetime.datetime(yyyy,mm,dd)
	currentyr = datetime.datetime(yyyy,12,31)
	endmonth = datetime.datetime(yyyy+1,8,31)
	daynum = int(initdate.strftime("%j")) # Turn the start date to day number of a year (1-366)
	yearofday = int(currentyr.strftime("%j")) # Determine the number of days in a year (i.e. 365 Days for 2023, 366 Days for 2024)
	endsummer = (int(endmonth.strftime("%j"))-1) if (yyyy+1) % 4 == 0 else int(endmonth.strftime("%j"))
	i = daynum
	while  i != endsummer:
		if checkweek(yyyy,i) and (not exception(yyyy,i)) and (skipday(yyyy,i)==1):
			printdate = datetime.datetime(yyyy, 1, 1) + datetime.timedelta(i - 1)
			endate = printdate.date() + datetime.timedelta(days=1)		
			i += 1
			try:	# Append the corresponding school day to the calendar file and reset the tuple iteration if StopIteration Error was prompt 		
				appendics(printdate.strftime('%Y'),printdate.strftime('%m'),printdate.strftime('%d'),endate.strftime('%Y'),endate.strftime('%m'),endate.strftime('%d'),next(schday))
			except:
				schday = iter(schtuple)
				appendics(printdate.strftime('%Y'),printdate.strftime('%m'),printdate.strftime('%d'),endate.strftime('%Y'),endate.strftime('%m'),endate.strftime('%d'),next(schday))
		else:
			i += skipday(yyyy,i)
		if i >= yearofday: # Proceed to the next year if the index is bigger than the number of days in a year 
			yyyy += 1
			i -= yearofday
	ics.write('END:VCALENDAR')
	ics.close()
	print('Done')
main()
