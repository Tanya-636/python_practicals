def LastNlines(f, N):
    with open(f) as file:
        print("Last 'n' lines from test: ",f)
        for line in (file.readlines() [-N:]):
            print(line, end ='')
name = input("Enter the file name: ")
N = int(input("No. of last lines to read: "))
try:
    LastNlines(name, N)
except:
    print('File not found')