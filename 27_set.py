# set1 ={1,5,7}
# print(type(set1))



#type casting( removing duplicate item from list by converting list to set)
# list1 = [1,5,4,6,5,5]
# print(list1)
# print(set(list1))

#UNION
alphabet ={ "a","b","c","d" , "hari"}
people = {"ram","shyam","hari", "a", "usa"}
country = {"usa", "russia", "china", "b","c", "ram"}

print("union")
total_1 = alphabet.union(people)
print(total_1)

total_2 = people | country
print(total_2)

print("intersection: ")
total_3 = alphabet.intersection(country)
print(total_3)

total_4 = people & alphabet
print(total_4)