#Conditionals: 
# conditional *---if else---** to check whether it's a dict or list passing mean function: 
def mean(my_input):
    if type(my_input)== dict:  
 # here we could also use **
    #if isinstance(my_input, dict): 
        the_mean= sum(my_input.values())/len(my_input)
        
    else:
        the_mean= sum(my_input)/len(my_input)

    return the_mean
today_expenses=[20.0, 20.0, 8.0]
Other_expense={"Electricity": 146, "rent":162, "meal": 100, "Health_insaurance":107}
print("Mean of list ",today_expenses,"=",mean(today_expenses))
print("\nMean of dict ",Other_expense,"=",mean(Other_expense))

# check whether string is less than 8 characters or not
def str_check(my_input):
    if len(my_input)<8: 
        return False
    else: 
        return True
print("\n str checked as '",str_check("Somewords"),"'")

#nested else if 
def temperatureUpdate(reading): 
    if reading>25: 
        return "Hot"
    elif reading <=25 and reading >=15:
        return "Warm"
    else :
        return "Cold"
print(temperatureUpdate(50))







