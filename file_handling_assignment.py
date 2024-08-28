try:
# Creating  my_file.txt file
    with open('my_file.txt', 'w') as file:
    # Writing three lines of content in my_file.txt
        file.write("Hello, my name is Asiphe Masoka\n")
        file.write("I am really enjoying this journey of learning python\n")
        file.write("this is my " + str(5) + " assignment\n")

# Enhancing the my_file.txt to be in a reading format
    with open('my_file.txt', 'r') as file:
    # creating a variable I would use when displaying my_file.txt content to the console
        content = file.read()
# displaying my_file.txt to the console
    print(content)   

    with open('my_file.txt', 'a') as file:
        file.write("Learning is so fun!!!\n")
        file.write("Python is a very important skill in nowadays\n")
        file.write("File handling is really not hard")
# Error to be displayed when the file is not found        
except FileNotFoundError:
    print("File not found!!!")
# Error to be displayed when permision to access the file is denied    
except PermissionError:
    print("Permission to open the file denied") 
# Error to be displayed, if the error is not any of the aforementioned errors    
except Exception as e:
    print(f"unexpected error occured: {e}")
# statement to be displayed whether an exception occurred or not.    
finally:
    print("file operation completed")           