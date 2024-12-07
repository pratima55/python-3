# name ="kathmandu"

# for letter in name :
#     full_letter = "@" + letter
#     print(full_letter)

#####    #####################

first_data = ["apple", "ball", "cat", "dog"] #list
#wap to display below format output
# it is an apple
#it is a ball
#it is a  cat
#it is a dog

for word in first_data:
    if word[0] in ("a","e","i","o","u") :
        print("it is an", word)
    else:
        print("it is a", word)    
