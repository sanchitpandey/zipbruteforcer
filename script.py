import zipfile

file = open("wordlist.txt","rb")
count=1
found = False
for passb in file.readlines():
    passb = passb.strip()
    password = passb.decode('utf8')
    x =  zipfile.ZipFile("Secret.zip","r")
    try:
        x.extractall(pwd=passb)
        print("Found correct password:",password)
        found = True
        break
    except:
        print("{}) {} is wrong".format(count,password))
        count+=1

if not found:
    print("Password not in wordlist")
        
