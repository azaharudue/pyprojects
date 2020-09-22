#user input manipulation
def temperature_condition(_user_input): 
    if _user_input<7:
        return "Cold"
    else:
        return "Warm"
##Normally python takes all user entries as strng .
user_input= float(input("Please enter today's temperature: "))
print(temperature_condition(user_input))
print(type(user_input))


# round  up values  with ** for ** loop: 
print("-------------using for  loop iteration: -------------")
expenses=[10.5, 11.5, 24.5, 18.5]
for i in expenses:
    print(round(i))

#another example : 
for letters in ["hello"]: 
    print(letters.title())
#iteration on dictionaries: 
country_code={"Bangladesh":"+88", "Saudi Arabia": "+966", "Singapore": "+65"}
for countryname,code in country_code.items(): 
    print("{} has country code :{}".format(countryname,code) )

# replace a string value of a dictionary [from + to 00] : 
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for number in phone_numbers.values(): 
    print(number.replace("+","00"))

# while loop  : 
username=''
while username!= 'azahar': 
    username=input("Enter username:")
# while loop with break and  continue :
while True: 
    username= input("ENter username:")
    if username== 'azahar':
        break 
    else :
         continue
