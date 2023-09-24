import hashlib
master_psw = "coolgamer".encode()
"SHA-256:", hashlib.sha256(master_psw).hexdigest()


password = input("Welcome! Write your password to proceed: ")

def manager():
    while True:
     master_psw2 = "coolgamer"
     if password == master_psw2:
        print("github password: idk")
        print("youtube password: idk")
        print("reddit password: idk")
        break
     else: print("Wrong password, try again!")
     return

manager()