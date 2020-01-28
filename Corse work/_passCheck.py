###############################################################################
##                                                                           ##
##                                HOW TO USE                                 ##
##                                                                           ##
## checkUser('Username','Password',True/False,'name of file(no extension)')  ##
##                                     ^                                     ##
##                        Create new user if available                       ##
##                                                                           ##
###############################################################################


import tkinter.messagebox
from tkinter import *

def checkUser(n,p,allowNew,fileName):
    fileName += '.txt'
    if allowNew:
        f=open(fileName,'a')
        f.close()
        f=open(fileName,'r')
        usrs=[]
        passwords=[]
        while True:
            temp=f.readline()
            if temp == '':
                break
            else:
                usrs.append(temp.split(',')[0])
                passwords.append(temp.split(',')[1])
        f.close()
        for i in range(len(usrs)):
            usrs[i]=decrypt(usrs[i])
            passwords[i]=decrypt(passwords[i])
        if n in usrs:
            for i in range(len(usrs)):
                if usrs[i] == n and passwords[i]== p:
                    tkinter.messagebox.showinfo("PassCheck","Password accepted.")
                    return True,i
            tkinter.messagebox.showinfo("PassCheck","Password not accepted.")
        else:
            nu=tkinter.messagebox.askquestion("PassCheck","Create new user?")
            if nu=='yes':
                f=open(fileName,'a')
                string=encrypt(str(n)+','+str(p)+',')
                f.write(string)
                f.write('\n')
                f.close()
                tkinter.messagebox.showinfo("PassCheck","User added.")
                return False,False
            else:
                tkinter.messagebox.showinfo("PassCheck","User not added.")
    else:
        f=open(fileName,'a')
        f.close()
        f=open(fileName,'r')
        usrs=[]
        passwords=[]
        while True:
            temp=f.readline()
            if temp == '':
                break
            else:
                usrs.append(temp.split(',')[0])
                passwords.append(temp.split(',')[1])
        f.close()

        if n in usrs:
            for i in usrs:
                if usrs[i] == n and passwords[i]== p:
                    tkinter.messagebox.showinfo("PassCheck","Password accepted.")
                    return True,i
        else:
            tkinter.messagebox.showinfo("PassCheck","Password not accepted.")
            return False,False

def encrypt(m):
    a = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    a = a.split(" ")
    n = 7
    ca = a
    for i in range(n):
        for i in range(len(ca)-1):
            i2 = len(ca)- 1 
            i2 = i2 - i
            temp = ca[i2]
            ca[i2] = ca[i2-1]
            ca[i2-1]=temp
    alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alph = alph.split(" ")
    nmes = []
    for i in range(len(m)):
        if m[i] in a:
            count=0
            while alph[count] != m[i]:
                count = count+1
            nmes.append(ca[count])
        else:
            nmes.append(m[i])
    for i in range(len(alph)):
        alph[i]=alph[i].upper()
        ca[i]=ca[i].upper()
        a[i]=a[i].upper()
    
    for i in range(len(nmes)):
        if nmes[i] in a:
            count=0
            while alph[count] != nmes[i]:
                count = count+1
            nmes[i]=ca[count]
        else:
            nmes[i] = nmes[i]
    strmes = ""
    for i in range (len(nmes)):
        strmes = strmes+str(nmes[i])

    return strmes

def decrypt(m):
    a = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    a = a.split(" ")
    n = 26-7
    ca = a
    for i in range(n):
        for i in range(len(ca)-1):
            i2 = len(ca)- 1 
            i2 = i2 - i
            temp = ca[i2]
            ca[i2] = ca[i2-1]
            ca[i2-1]=temp
    alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alph = alph.split(" ")
    nmes = []
    for i in range(len(m)):
        if m[i] in a:
            count=0
            while alph[count] != m[i]:
                count = count+1
            nmes.append(ca[count])
        else:
            nmes.append(m[i])
            
    for i in range(len(alph)):
        alph[i]=alph[i].upper()
        ca[i]=ca[i].upper()
        a[i]=a[i].upper()


    for i in range(len(nmes)):
        if nmes[i] in a:
            count=0
            while alph[count] != nmes[i]:
                count = count+1
            nmes[i]=ca[count]
        else:
            nmes[i] = nmes[i]
    
    strmes = ""
    for i in range (len(nmes)):
        strmes = strmes+str(nmes[i])

    return strmes