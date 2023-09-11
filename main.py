# write your code here
person = {
    "name" : "zahraa" ,
    "age" : 18 ,
    "hobbies" : ["shopping" , "dancing" , "football"]
}
print(person["name"])
print(person["age"])

person["age"]=19
person["country"]="uk"
print(person)
print(f"number of objects in dictionry: {len((person))}")
person["hobbies"].append("coding")

def check_hobbies(person):
    if len(person["hobbies"])>=3:
        return print("wow you are amazing!")
check_hobbies(person)