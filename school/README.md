# School Calendar Generator 

## What does it do?
Generate a calendar showing school days (i.e. Day 1 to Day 6) by retrieving the configuration from config.yaml and then output the calendar file (schday.ics) in .ics format

## Prerequisites 
- Have Python 3 installed on your devices 
- PyYAML and datetime modules are correctly installed  

###  Configurations
- All dates must be at YYYY/MM/DD format (eg. 2022/9/15)
- By default, the script will bypass dates which are Saturday and Sunday, so there is no need to specifically exclude these dates on `Exceptdate`.
- Available Records:

      - `output_path` : (Optional) Indicates the path for outputting the calendar file. By default the value is `schday.ics`
      
      - `startdate` : Indicates the date when the calendar will start from
      
      - `exceptdate` : Indicates the dates which will be excluded by the calendar
      
      - `skiprange` : Indicates the range of dates which will be excluded by the calendar. The format for this record is YYYY/MM/DD/Range. For example, 2022/7/13/4 indicates the calendar will bypass dates from 2022/7/13 to 2022/7/16 inclusively. 
         Ranges can also be calculated by subtracting the ending date by the start date plus 1. (eg. The range of a holiday from 2023/2/13 to 2023/2/24 can be derived by 24-13+1 = 12)


# How to use it

## - Windows
1. Install PyYAML module by typing `pip install pyyaml` on Command Prompt
2. Download  `config.yaml`  and  `calendar.py`  and place them in the same directory.
3. Open `calendar.py`  on notepad and modify the path to configuration on line 7 to your own directory. (Replace the backslash ” \\ “ with slash “/“ for the directory, eg: D:/Utilities/config.yaml)
4. Open `config.yaml`  and change  `output_path` (Same format as above) and other records if necessary.
5. Run it !

## - Pythonista (iOS/ iPad OS)
1. Install Stash by referring to [here](https://github.com/ywangd/stash).
2. Run the  `launch_stash.py`  script and enter  `pip install pyyaml`.
3. Download  `config.yaml`  and  `calendar.py`  and place them in the same directory.
4. Open `calendar.py`  on notepad and modify the path to configuration on line 7 to your own directory. (Usually it’s just “config.yaml” )
5. Open `config.yaml`  and change  `output_path` (Same format as above) and other records if necessary.
6. Run it !
