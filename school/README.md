# School Calendar Generator 

## What does it do?
Generate a calendar showing school days (i.e. Day 1 to Day 6) by retrieving the configuration from config.yaml and then output the calendar file (schday.ics) in .ics format

## Prerequisites 
- Have Python 3 installed on your devices 
- PyYAML and datetime modules are correctly installed 
- `config,yaml`  and `calendar.py`  are placed in same directory 

###  Configurations
- All dates must be at YYYY/MM/DD format (eg. 2022/9/15)
- By default, the script will bypass dates which are Saturday and Sunday, so there is no need to specifically exclude these dates on `Exceptdate`.
- Available Records: 
  - `startdate` : Indicates the date when the calendar will start from
  - `output_path` : (Optional) Indicates the path for outputting the calendar file. By default the value is `schday.ics`
  - `exceptdate` : Indicates the dates which will be excluded by the calendar
  - `skiprange` : Indicates the range of dates which will be excluded by the calendar. The format for this record is YYYY/MM/DD/Range. For example, 2022/7/13/4 indicates the calendar will bypass dates from 2022/7/13 to 2022/7/16 inclusively. 
         Ranges can also be calculated by subtracting the ending date by the start date plus 1. (eg. The range of a holiday from 2023/2/13 to 2023/2/24 can be derived by 24-13+1 = 12)
         ![Calendar Example](https://github.com/Marcio2536/utilities/raw/main/school/calendar.jpg)

