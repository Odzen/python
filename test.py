
#With the command with, the code that is inside the block
# executes and the the file close automatically after that,
#even if it happens an exception, thats why its better 
# with order('file', 'r') as name: 
# That is a good practice 

#After the context manger block, the variable f still exists
# but it exists as a close file 

with open('testFile','r') as f:
    #f_contents= f.read() just read
    #f_contents= f.readlines() # You get a list with all the lines in the file 
    #print(f_contents)

    
    #Read line by line readline()
    #f_contents= f.readline()
    #print(f_contents, end='')

    #Now the second line is the following to read 
    #f_contents= f.readline()
    #print(f_contents, end='')


    #To read al the lines efficiently
    for line in f:
        print(line, end='')

print(f.closed)