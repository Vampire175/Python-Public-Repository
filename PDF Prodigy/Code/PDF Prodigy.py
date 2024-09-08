import webbrowser
print('Welcome to PDF Prodigy')
y=input('What do you want to do:\n1)Open and edit pdf\n2)Make and edit\n3)Only Edit\nJust enter the  number: ')
if y=='1':
    a=input('Enter file name without extension: ')
    with open(a+'.pdf') as f:
        s=f.read()
        print(s)
        t=input('Do you want to edit the pdf\n1)Yes\n2)No\nJust enter the number: ')
        if t=='1':
            webbrowser.open('https://www.sejda.com/')
        elif t=='2':
            f.close()
elif y=='2':
    g=input('Enter the name of pdf without extension: ')
    with open(g+'.pdf','w') as p:
       h=input('Enter the text: ')
       p.write(h)
       t=input('Do you want to edit the pdf\n1)Yes\n2)No\nJust enter the number: ')
       if t=='1':
           webbrowser.open('https://www.sejda.com/')
       elif t=='2':
         p.close()
elif y=='3':
    webbrowser.open('https://www.sejda.com/')
print('Thankyou for using PDF Prodigy')
print('Made by Vampire with ❤️')
jh=input('Press Enter to Exit')