user=input()

choice = ['1 - google_kz.txt','2 - google_paris.txt','3 - google_uar.txt']
i=0
if user.lower() in 'hello':
    print('Choice file you want input to: ', choice)
    x=int(input())
    if x==1:
        myfile1=open("google_kz.txt","w")
        print("Name of a file is: ", myfile1.name)
        myfile1.write(input())
        print(myfile1)
        myfile1.close()
    if x==2:
        myfile2=open("google_paris.txt","w")
        print("Name of a file is: ", myfile2.name)
        myfile2.write(input())
        # info=myfile2.read()
        # print(info)
        myfile2.close()
    if x==3:
        myfile3=open("google_uar.txt","w")
        print("Name of a file is: ", myfile3.name)
        myfile3.write(input())
        myfile3.close()
        print(myfile3)