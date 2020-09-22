''' reading a file'''
''' myfile = open("fruits.txt")
#print(myfile.read())
# crouser stands end of the file that's why myfile.read() will result into empty spaces
#to show content multiple times : 
content = myfile.read()
myfile.close()
print(content)
print(content) '''
''' using with ... 
with open("files/fruits.txt") as myfile: 
    content= myfile.read()
print(content)
'''
''' writting files'''
with open("files/vegetables.txt", "w") as myfile2:
    myfile2.write("Tomato\nCucumber\nPotato\n")
    myfile2.write("Garlic")
#reading up to a specific character
with open("files/fruits.txt","w") as myfile: 
    content = myfile.write("A,B,C,D,E,F,G,H,I,J,K")
print(content)
#Counting character occurances in a file :
def NumberOfOccurances(character, filepath):
    file = open(filepath)
    content = file.read()
    return content.count(character)
print(NumberOfOccurances("T","files/vegetables.txt"))
#writting some data from a file to another
with open("files/fruits.txt") as inputfile: 
     content= inputfile.read()
    
with open("files/first.txt", "w") as newfile: 
     newfile.write(content[:18])
print("--------------------Appending--------------------------------")
#Appending texts form one file to another using 'a' mode:  
with open("files/fruits.txt") as file1: 
    content1=file1.read()
with open("files/fruits2.txt","a+") as file2: 
    file2.write(content1)
    file2.seek(0) # with sek(0) command the cursor goes to the beginning of the file.
    print(file2.read())

print("''''''''''''''''''''''''''''''''''''''''''")
with open("files/vegetables.txt","a+") as file: 
    file.seek(0)
    content=file.read()
    file.write("\n"+content)
    file.write("\n"+content)
    file.seek(0)
    content= file.read()
    print(content)