import random
import pandas as pd
print('Important Caution-Please do not change csv name')
print('Welcome to Invoice Maker')
a=input('Enter the name of customer: ')
bv=input('Enter the products he ordered: ')
cv=input('In what quantity he ordered the products: ')
vc=input('Total: ')
vm=random.randint(1,100000)
nb=input('What do you want to do\n1)Make a new invoice\n2)Open One and Edit\nJust enter the number: ')
if nb=='1':
 dict1={
    'Name':[a],
    'Products':[bv],
    'Quantity':[cv],
    'Total':[vc],
    'Special Number':[vm]
}
 df=pd.DataFrame(dict1)
 print(df)
 b=input('Do you want it as excel: ')
 if b=='yes':
    c=input('Do you want index: ')
    if c=='yes':
     df.to_csv('Invoice of '+vm+'.csv')
    elif c=='no':
       df.to_csv('Invoice of '+vm+'.csv',index=False)
 elif b=='no':
   bn=input('Press Enter:')
elif nb=='2':
  s=input('Just Enter CSV name you want to open with .csv extension: ')
  f=pd.read_csv(s)
  print(f)
  h=input('Do you want to edit something in you invoice')
  if h=='yes':
    bh=input('What do you want to change\n1)Name\n2)Products\n3)Quantity\n4)Total\nJust Enter The Number: ')
    if bh=='1':
      
print('Thankyou for working with Invoice Maker')
print('Made by Vampire with ❤️')
g=input('Press Enter to exit')
