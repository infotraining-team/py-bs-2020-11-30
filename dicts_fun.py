dic_list = [
    {"name": "Leszek",
     "age" : 43},
    
    {"name": "Stefan",
     "age" : 18},

    {"name" : "Ola",
     "age" : 27}
]

oldest = 0
oldest_name = ""
for dic in dic_list:    
    if dic["age"] > oldest:
        oldest_name = dic["name"]
        oldest = dic["age"]

print(oldest, oldest_name)

ages_names = []
for dic in dic_list:
    if dic['age'] > 20:
        ages_names.append( (dic["age"], dic["name"]) )    

ages_names.sort(reverse=True)

print(ages_names)
