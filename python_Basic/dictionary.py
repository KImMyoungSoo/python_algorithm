dic = {"name" : '홍길동', "age":25}

print(dic["name"])
print(dic.get("name"))

dic["job"] = "개발자"
print(dic)

# dic.pop("job")
# print(dic)

for i in dic.keys() :
    print(i)

for i in dic.values() :
    print(i)

for key, val in dic.items() :
    print(f"{key} : {val}")