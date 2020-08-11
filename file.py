import json
path = "/home/ranoa/Documents/udemy/Udemy_tsiky/file.json"
# with open(path,"r") as file:
#     content=file.read().splitlines()
#     # print (len(content))
#     join_content=' '.join(content)
#     print(join_content)

# with open(path,"w") as file_write:
#     file_write.write("hello mum")
# with open(path,"a") as file_write:
#     file_write.write("\n hello")

a="hello babe"
b= list(range(1000))

# with open(path,"w") as file:
#     json.dump(a,file)
#     json.dump(b,file,indent=2)

# with open(path,"r") as f:
#     lst_json=json.load(f)
#     print(lst_json)
with open(path,"w") as file:
    json.dump("écho",file,ensure_ascii=False)