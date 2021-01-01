import threading 
from threading import*
import time

dic={} #'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dic:
        print("This key already exists") 
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=l
            else:
                print("Memory limit exceeded!! ")
        else:
            print("Invalind key_name || key_name must contain only alphabets and no special characters or numbers")

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dic:
        print("Given key does not exist in database. Please enter a valid key") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("Time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dic:
        print("The key does not exist in database. Please enter a valid key") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dic[key]
                print(" The key is successfully deleted")
            else:
                print("Time-to-live of",key,"has expired") 
        else:
            del dic[key]
            print("The Key is successfully deleted")

#An additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    b=dic[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dic:
                print("Given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dic[key]=l
        else:
            print("Time-to-live of",key,"has expired") 
    else:
        if key not in dic:
            print("Given key does not exist in database. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dic[key]=l
