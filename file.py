path = "/home/ranoa/Documents/udemy/Udemy_tsiky/fichier.txt"

# with open(path,"r") as file:
#     content=file.read().splitlines()
#     # print (len(content))
#     join_content=' '.join(content)
#     print(join_content)

# with open(path,"w") as file_write:
#     file_write.write("hello mum")
with open(path,"a") as file_write:
    file_write.write("\n hello")
    
