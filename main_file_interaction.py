# Python provides built-in functions and methods for file handling, including open(), read(), write(), close(), and others. You can use the open() function to open a file and specify the mode (e.g., read, write, append). Once the file is opened, you can use methods like read() or write() to perform read or write operations on the file. After you're done working with the file, it's essential to close it using the close() method to release system resources. 

# the r stands for read only
r = open('read.txt', 'r')
first_line = r.readline()
# print the first line
print(first_line)

print('Pring each line in the text file:')
for line in r:
    print(line)
r.close()

# the w stands for write only
w = open('write.txt', 'w')
w.write("You are finally writing")
w.close()

# the a stands for append the file
a = open('write.txt', 'a')
a.write("""\nI may not not know your name, 
but I can sure as hell open your file""")
a.close()