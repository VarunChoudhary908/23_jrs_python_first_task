Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
Brand=[]
Os=[]
for a in Computers:
    for b in Computers[a]:
        if b == "brand":
            Brand.append(Computers[a][b])
        elif b == "OS":
            Os.append(Computers[a][b])
            
print(Brand)
print(Os)

print("Varun Choudhary")