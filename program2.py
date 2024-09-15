choice=input('enter h=horizontal or v=vertical')
s="starting point "
e="ending point" 
U="updation"
if(choice=='h'):
    for i in range(s,e+1,U):
      print(i,end=" ")
elif(choice=='v'):
    for i in range(s,e+1,U):
      print(i)
else:
     print("invalid ")