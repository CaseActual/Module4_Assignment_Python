# zcrowell_module4_programmingassignment.py
# Chapter 4, problem 2 -> Celsius to Fahrenheit Table
# last edited by Zane Crowell - Oct. 4, 2020
# CSCI 111 Section 002

# programming assignment - print list of temperatures from in columns

# create nested list of temps and their conversions (C on left, F on right)
tempList = [['Celsius','Fahrenheit'],['   0','   32.0'],['   1','   33.8'],['   2','   35.6'],
            ['   3','   37.4'],['   4','   39.2'],['   5','   41.0'],['   6','   42.8'],
            ['   7','   44.6'],['   8','   46.4'],['   9','   48.2'],['   10','   50.0'],
            ['   11','   51.8'],['   12','   53.6'],['   13','   55.4'],['   14','   57.2'],
            ['   15','   59.0'],['   16','   60.8'],['   17','   62.6'],['   18','   64.4'],
            ['   19','   66.2'],['   20','   68'],['   21','   69.8'],['   22','   71.6'],
            ['   23','   73.4'],['   24','   75.2'],['   25','   77.0'],['   26','   78.8'],
            ['   27','   80.6'],['   28','   82.4'],['   29','   84.2'],['   30','   86.0'],
            ['   31','   87.8'],['   32','   89.6'],['   33','   91.4'],['   34','   93.2'],
            ['   35','   95.0'],['   36','   96.8'],['   37','   98.6'],['   38','   100.4'],
            ['   39','   102.2'],['   40','   104.0']]

# get input to show table
userInput = str(input("Would you like to see the C to F conversion table? (y or n): "))

# processing - get list to display uniformly as table
length_list = [len(element) for row in tempList for element in row]     # get lengths of list elements
column_width = max(length_list)     #set column width with length of longest element

# print label for table
print('Celsius to Fahrenheit Conversion:')
# display list 
for row in tempList:
    row = "".join(element.ljust(column_width + 2) for element in row)
    print(row)

# program end















