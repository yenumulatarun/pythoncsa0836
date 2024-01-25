p=int(input("enter the principle amount:"))
n=int(input(" enter the number of years:"))
sc=input("senior citizen yes/no:")
g=input("male/female:")
if sc=='y' and g=='m':
 print("si=",(p*n*12)/100)
elif sc=='y' and g=='f':
 print("si=",(p*n*15)/100)
else:
     print("si=",(p*n*10)/100)











