names = []
for x in range (0,10):
    n1 = input("enter name ")
    names.append(n1)

keepsearching = True
while keepsearching:
    search = input("search for name ")
    if search in names:
        print ("name found")
    elif search == "End":
        keepsearch = False
        
