# working with the items of a list 
data=[100, 200, 300, 400]
new_data =[]
for i in data: 
    new_data.append(i/2)
print(new_data)
 
#same things like above, we can do in inline pythone code using for loop (inline)
dataset=[100, 200, 300, 400]
new_data= [ data/2 for data in dataset]
print(new_data)

# use if condition in inline list comprehension ** to ignore missing data in datasets***
dataset=[200, 300, -9999, 400]
new_data=[data/5 for data in dataset if data != -9999 ]
# to replace missing data with zero  : ** if condition comes before the for loop 
new_data=[i if i!=-9999 else 0 for i in dataset]  
print(new_data)

#For converting list elements and sum up 
def sumCalc(input_list): 
    new_list=(float(i) for i in input_list)
    return sum(new_list)
print("Sum is : " ,sumCalc(['200', '-50','600']))

