#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dell
#
# Created:     09-11-2022
# Copyright:   (c) Dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
student={'name':'anshul','reg':45729,'section':'m1013','branch':'me','marks':{'s1':92,'s2':87},'s3':74,'s4':65,'s5':45}
calculate_marks=student['marks']
total=0
for x in calculate_marks:
    total=total+calculate_marks[x]
per=(total/500)*100
avg=total/5
print('percentage of student',student['name'],'is=',per)
print('average=',avg)