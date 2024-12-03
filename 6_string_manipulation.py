# concatenation
first_name ="ram"
second_name = "shyam"
print(first_name + second_name)


# example
a= "ram"
b= 9
print(a+ str(b))


# strip
first_sentence = "   hello i am from mars"
print(first_sentence.strip())  
# strip remove white space


# split
# example 1
skill_shikshya = "skillshikshya@gmail.com"
splitted_data = skill_shikshya.split("@")
print(splitted_data)
# output =['skillshikshya', 'gmail.com']


# replace
about_nepal ="nepal is ......nepal...jcjdhhjsj kshdjskhja jdhjsdhj... ... ksjdjdasfj india jjdjdjdj ... india"
corrected_data=about_nepal.replace("india", "nepal")
corrected_data = corrected_data.replace(".", "the")
print(corrected_data)


# 
father_name = "some name"
print(father_name.upper()) 
# upper make all letter capital
print(father_name.capitalize())
# capitalize make first letter capital
print(father_name.title())
# title make every word's  first letter capital


# class work, decribe 10 string manipulation function in python with example

# join() concatenate strings
# startswith() and endswith() these methods check if a string starts or ends with a specific substring , which is useful for validation
# find() this methods locate a substring within a string.
# count() this method returns the no. of occurances of a substring
# translate() returns a translated string
# swapcase() swaps cases, lower case become upeer care and vice versa
# centre() returns a centred string
# casefold() converts the string into lower case
# len()
# index()


data = "my name is prateema." 

data_2 = "  i am from biratnagar."

print(data.capitalize()) #output: My name is prateema.
print(data.upper()) #output:MY NAME IS PRATEEMA.
print(",".join(data)) #output: m,y, ,n,a,m,e, ,i,s, ,p,r,a,t,e,e,m,a,.
print(data.find("name")) #output : 3
print(data.count("a")) #output: 3
print(data.swapcase()) #output: MY NAME IS PRATEEMA.
print(data.center(30,"0")) #output: 00000my name is prateema.00000
print(data.casefold()) #output: my name is prateema.
print(len(data)) #output : 20
print(data.index("is")) #output: 8
print(data.startswith("my")) #output: true
print(data.endswith("dhakal")) #output:False
print(data.split(" ")) #output: ['my', 'name', 'is', 'prateema.']
