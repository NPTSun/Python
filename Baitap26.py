n = int(input())
gio = n//3600
phut =(n-gio*3600)//60
giay = n-gio*3600-phut*60
print("{:02}:{:02}:{:02}".format(gio,phut,giay))
      
