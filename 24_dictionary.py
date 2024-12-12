# {key : "value"}
user_data_detail = {"name": "skill shikshya", "location":"ktm"}
# print(user_data_detail["location"])
for key in user_data_detail:
    print(user_data_detail[key]) #output: skill shikshya ktm

    

################
user_data_detail = {"name": "skill shikshya", "number": "98080"}
for key in user_data_detail:
    if key == "number":
        user_data_detail["number"] = "+977" + user_data_detail["number"]

print(user_data_detail)          
