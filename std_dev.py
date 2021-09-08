# importing modules
import csv
import math 

# Reading the file
with open("data.csv",newline = "") as f :
    reader = csv.reader(f)
    file_data = list(reader)

#list of elements to calculate mean
data = file_data[0]

# Defining a function for calculating mean
def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total/n
    return mean

#squaring and getting all values
squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0

# Finding the sumation
for i in squared_list:
    sum = sum + i

# Dividing the sum by the total no. of values
result = sum/(len(data) - 1)

# Taking suqare root of the result
std_dv = math.sqrt(result)

# Printing
print(std_dv)
