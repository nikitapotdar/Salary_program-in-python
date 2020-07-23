# miniproject : Lesson 11 - Python Nested conditional IF
'''Program to calculate salary of employees Basic + DA

Write a program to be used to calculate salary of employees.
Salary consists of two components (1)Basic (2)DA an allowance
specified as some % of basic. Input to the program -> Basic
Rules and rates :
* Basic range minimum 1800 to maximum 10000 only allowed
* Basic less than 3600 the DA rate is 180% of basic
* Basic 3600 to less than 6000 DA rate 160% subject to
  minimum DA amount of 6480
* Basic 6000 and above DA rate is 140% subject to minimum
  DA amount of 9600
* salary = Basic + DA amount.
* Output -> basic, DA and salary
'''
#Solution :
import sys
#set variables to known values(easy to change later in revision)
minBasic = 1800 #minimum basic value
basicLevel1 = 3600 #basic for first slab
basicLevel2 = 6000 #basic for second slab
maxBasic = 10000 #maximum basic value
daRateLevel1 = 180/100 #da rate for first slab 1800-3600 -> 180%
daRateLevel2 = 160/100 #da rate for second slab 3600-6000 -> 160%
daRateLevel3 = 140/100 #da rate for 6000 and above -> 140%
minDaLevel2 = 6480 #minimum DA for 3600-6000 slab
minDaLevel3 = 9600 #minimum DA for 6000-10000 slab
basic = int(input('Input Basic 1800 to 10000 : ') or 0)
if basic >= minBasic and basic <= maxBasic:
      if basic >= minBasic and basic < basicLevel1:
            da = basic * daRateLevel1
      elif basic >= basicLevel1 and basic < basicLevel2:
            da = basic * daRateLevel2
            if da < minDaLevel2:
                  da = minDaLevel2
      elif basic >= basicLevel2 and basic <= maxBasic:
            da = basic * daRateLevel3
            if da < minDaLevel3:
                  da = minDaLevel3
      salary = basic + da
else:
      print('Basic range 1800-10000 only allowed')
      sys.exit()
print('======output below========')
print('Basic = ', basic)
print('DA = ', da)
print('Salary = ', salary)
