import json
jsonData = """ {
    "ID"       : 310450,
    "login"    : "admin",
    "name"     : "James Bond",
    "password" : "root",
    "phone"    : 3330303,
    "email"    : " bond@mail.com",
    "online"   : true
} """
dictData = json.loads(jsonData)
print(dictData["name"])
print(dictData["phone"])
print(dictData["email"])
print(dictData["online"])

