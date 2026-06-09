#dog={ "name": "roger", "age" :5, 'color':"brown"}
 
#dog["name"] = "syd"

#dog["favorite foos"]="bones"
 
#print(dog.get("color", "black"))



#dogcopy= dog.copy()
#print(dog)
dic = {
    433: "pawan",
    343:"anku",
    432: "sachin"
}
print(dic[343])

info = {'name ': 'pawan', 'age':23, 'eligible':True}
print(info)
#print(info['name'])
print(info.get('age',0))

for key in info.keys():
    print(info[key])


print(info.items())

ep1={122: 45, 123:67, 124:54}
ep2={125: 78, 126:90}
ep1.update(ep2)