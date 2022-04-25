def swap():
    file1=input("Please enter the first file")
    file2=input("Please enter the second file")
    data_a=open(file1)
    data_b=open(file2)
    a=data_a.read()
    b=data_b.read()
    data_a=open(file1,"w")
    data_b=open(file2,"w")
    data_a.write(b)
    data_b.write(a)
    
swap()