a={"key1":1, "key2":2,"key3":3,"key4":5 }
a["key4"]=5
a.pop("key2")
a.keys()
for i in a.keys():
    print(i,a.get(i))
a.values()
for i in a.values():
    print(i)
a.items()
for key,value in a.items():
    print(key,value)
