from pathlib import Path


def creatingFile():
    name = input("Enter your file name:- ")
    path = Path(name)

    try:
        if not path.exists():
            with open(path, "w") as fs:
                data = input("What you want to write:- ")
                fs.write(data)
                print("File Created Sucessfully!")
        else:
            print("File already exist.")    
    except Exception as err:
        print(f"An error occured {err}")


def readingFile():

    name = input("What file u want to read:- ")

    path = Path(name)
    try:
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(f"Your file content is \n{content}")
        else:
            print("Error: No such file exists!")
    except Exception as err:
        print(f"An error occured {err}")


def updatingFile():
    try:
        
        name = input("Enter File name:- ")
        path = Path(name)

        if path.exists():
             
            print("Operations")
            print("Enter 1 for Rename the file name:- ")
            print("Enter 2 for Append the file content:- ")
            print("Enter 3 for Overwrite the file content:- ")

            option = int(input("Enter one of the following option:- "))    


            if option == 1:
                try:
                    newName = input("Enter file name for rename:- ")
                    newPath = Path(newName)
                    if not newPath.exists():
                        path.rename(newName)
                        print("Your file is renamed successfully!")
                    else:
                        print("Error: file name already exist!")
                except Exception as err:
                    print(f"An error occured  {err}")
                
            if option == 2:
                try:
                    content = input(" "+"Enter your content to append:- ")
                    with open(path,"a") as fs:
                        fs.write(content)
                    print("your Content append successfully!")
            
                except Exception as err:
                        print(f"An error occured  {err}")


            if option == 3:
                    try:
                        content = input("Enter content to overwrite:- ")
                        with open(path,'w') as fs:
                            fs.write(content)
                            print("Your Content Overwrite Successfully!")
                    except Exception as err:
                        print(f"An error occured  {err}")


        else:
            print("No such file exist!")

    except Exception as err:
            print(f"An error occured {err}")
     
def deletingFile():
    try:
        name = input("Enter file name to delete:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("Your file deleted Successfully!")
        else:
            print("No such file exist! ")
    except Exception as err:
        print(f"An error occured {err}")


print("Press 1 for Creating file:- ")
print("Press 2 for Reading file:- ")
print("Press 3 for Updating file:- ")
print("Press 4 for Deleting file:- ")

a = int(input("\nTell your response:- "))

if a == 1:
    creatingFile()

if a == 2:
    readingFile()

if a == 3:
    updatingFile()


if a == 4:
    deletingFile()