#Building own function to calculate mean: 
def mean(mylist):
    the_mean= sum(mylist)/len(mylist)
    return the_mean
print(mean([1, 2, 3, 4]))

# Buliding function to return the number of items in list:
def lengther(mylist): 
    return len(mylist)
print(lengther([1,2,3,4]))

# Building own function to calculate square of given input
def squareCalc(myinput):
    the_Square= myinput*myinput
    return the_Square
print("Square calculator: 7^2 =",squareCalc(7))
# Converting fluid ounces to milimeters : 1 ounce = 29.57353
def Ounce_to_Mili(my_input_ounce):
    the_result=my_input_ounce*29.57353
    return the_result
print("\nHere we will print Ounce to Mili conversion:")
print(Ounce_to_Mili(5))
