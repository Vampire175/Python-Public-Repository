from PIL import Image
print("Notice-Please read all the instructions carefully for best experience and photos and videos are not opened.Enjoy!\nVampire")
t=input("Can we start type yes or no: ")
if t=="yes":
    print("Note-For making excel files use xls extension")
    print("Welcome to Vampire's file manager.Here you can create or open the files which are in the folder of app")
    print("1)Make new file\n2)Open one")
    a=input("Choose any one: ")
    #a is the input for making and viewing
    if a=="Make new file":
            b=input("What is the name of the file,type without extension: ")
            #b is only for making file
            with open(b,"w") as f:
                        c=input("What do you want to type in the file type here: ")
                        f.write(c)
                        #c is only for writing a file
    elif a=="Open one":
          g=input("Do you want to open image yes or no: ")
          if g=="yes":
              n=input("Enter the name of image with the extension: ")
              img=Image.open(n)
              img.show()
          elif g=="no":
              d=input("Type the name of the file here which you want to open: ")
              #d is only for open one
              with open(d,"r") as f:
                j=f.read()
                print(j)
    if a=="1":
      b=input("What is the name of the file type with extension: ")
      #b is only for making file
      with open(b,"w") as f:
        c=input("What do you want to type in the file type here: ")
        f.write(c)
        #c is only for writing a file
    elif a=="2":
          g=input("Do you want to open image yes or no: ")
          if g=="yes":
              n=input("Enter the name of image with the extension: ")
              img=Image.open(n)
              img.show()
          elif g=="no":
              d=input("Type the name of the file here which you want to open: ")
              #d is only for open one
              with open(d,"r") as f:
                j=f.read()
                print(j)
print("Made by Vampire in India with ❤️")
x=input("Press enter to exit")
if t=="no":
  exit()