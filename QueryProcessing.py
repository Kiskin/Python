'''
Created on Mar 10, 2018
This module handles all the query processing 

@author: Kisife Giles
COMP 348 Assignment 2.
ID: 40001926
''' 
dbData =None
dbDictionary = {}

# Method initializes the server and reads input data file into the database.
def initializeDB():
    global reportError
    contentList =[]
    try:
        with open("data.txt","r") as fn:
            contentLines = fn.readlines()
            contentLines = [x.strip() for x in contentLines]
            for item in contentLines:
                tokens = item.split("|")
                if len(tokens[0])>0:#        Check if entry had a name value
                    contentList.append(item)
            fn.close()
                #else:
                    #reportError="Incomplete record found: "+ item
                
            return contentList
    except:
        print("Data file can not be read!")
        pass
        
dbData= initializeDB()
    
    #return the record matching the passed key name
def retriveEntry(name):
    global dbData
    for entry in dbData:
        x = entry.split("|") 
        if x[0]==name:
            return x[0]+" "+ x[1]+" "+x[2]+" "+x[3]
            
    # Add a new customer to the database
def addEntry(entry):
    dbData.append(entry)
    dd = entry.split("|")
    dbDictionary[dd[0]]=entry
    try:
        fn= open("data.txt","a")
        fn.write("{}\n".format(entry))
        status =0
    except:
        status =-1
    return status

#Method updates database.
def updateDatabase(category,name,newData=None):
    try:
        with open("data.txt","r+") as fn:
            if category=="DELETE":
                contentLines = fn.readlines()
                contentLines = [x.strip() for x in contentLines]
                fn.seek(0)
                for item in contentLines:
                    tokens = item.split("|")
                    if tokens[0] !=name and len(tokens[0])>1:
                        fn.writelines("{}\n".format(item))
                        
            elif category=="AGE" or category== "ADDRESS" or category=="PHONE":
                contentLines = fn.readlines()
                contentLines = [x.strip() for x in contentLines]
                fn.seek(0)
                for item in contentLines:
                    tokens = item.split("|")
                    if tokens[0] ==name:
                        item = newData
                    fn.writelines("{}\n".format(item))
                
                
    except:
        #print("Data file can not be read!")
        pass
    finally:
        fn.close()
    

# This method updates customer information
def updateCustomerInfo(category,name,correctData=""):
    global dbDictionary
    if category=="AGE":
        if name in dbDictionary:
            customerList = dbDictionary[name]
            customerList = customerList.split("|")
            customerList[1]=correctData
            newData =customerList[0]+"|"+customerList[1]+"|"+customerList[2]+"|"+customerList[3]
            dbDictionary[name]=newData
            updateDatabase("AGE", name, newData)
            return 0
        else:
            return -1
        
    elif category=="ADDRESS":
        if name in dbDictionary:
            customerList = dbDictionary[name]
            customerList = customerList.split("|")
            customerList[2]= correctData
            newData =customerList[0]+"|"+customerList[1]+"|"+customerList[2]+"|"+customerList[3]
            dbDictionary[name]=newData
            updateDatabase("ADDRESS", name, newData)
            return 0
        else:
            return -1
        
    elif category=="PHONE":
        if name in dbDictionary:
            customerList=dbDictionary[name]
            customerList = customerList.split("|")
            customerList[3] = correctData
            newData =customerList[0]+"|"+customerList[1]+"|"+customerList[2]+"|"+customerList[3]
            dbDictionary[name]=newData
            updateDatabase("PHONE", name, newData)
            return 0
        else:
            return -1
    
    elif category =="DELETE":
        if name in dbDictionary:
            del(dbDictionary[name])
            editDBList(name)
            updateDatabase("DELETE",name)
            return 0
        else:
            return -1
 # This methods prints the contents of the database, sorted in ascending order of name.
def printReport():
    global dbDictionary
    list =[]
    #dbData.sort()
    reportString =""
    for aKey in dbDictionary:
        list.append(dbDictionary[aKey])
    list.sort()
    for item in list:
        reportString =reportString+"\n"+ item
    return reportString

# This method edits the list containing the database information. 
def editDBList(name):
    global dbData
    for entry in dbData:
        x = entry.split("|") 
        if x[0]==name:
            dbData.remove(entry)
           
       
    # Method connects and respond to query
def serverReply(category,qtype):
    'Send the correct query to database'
    infoList = qtype.split("|")
    global dbDictionary
    global dbData
        #category =socket.recv(1024)
    if category=='1' or category==1:
        if qtype in dbDictionary:
            foundItem =dbDictionary[qtype]
        else:
            foundItem= qtype+" not found in database"
        return foundItem
        
    elif category== '2'or category==2:
        split = qtype.split("|")
        if split[0] in dbDictionary:
            return "Customer already exist!!"
        else:
            addEntry(qtype)
            return "Customer added!"
        
    elif category== '3'or category==3:
        deleteStatus = updateCustomerInfo("DELETE", infoList[0])
        if deleteStatus ==0:
            return "Customer "+infoList[0]+" deleted!"
        else:
            return "Customer "+infoList[0]+" not found in database!!"
    
    elif category=='4'or category==4:
        updateStatus = updateCustomerInfo("AGE", infoList[0], infoList[1])
        if updateStatus==0: 
            return infoList[0]+" 's age has been updated!"
        else:
            return "Customer "+infoList[0]+" not found in database!!"
            
    
    elif category== '5' or category==5:
        updateStatus = updateCustomerInfo("ADDRESS", infoList[0], infoList[1])
        if updateStatus==0:
            return infoList[0]+" 's address has been updated!"
        else:
            return "Customer "+infoList[0]+" not found in database!!"
    
    elif category=='6' or category==6:
        updateStatus = updateCustomerInfo("PHONE", infoList[0], infoList[1])
        if updateStatus==0:
            return infoList[0]+" 's telephone number has been updated!"
        else:
            return "Customer "+infoList[0]+" not found in database!!"
    
    elif category=='7'or category==7:
        return "**** Python DB Contents **** "+"\n"+ printReport() + "\n"
    
    elif category=='8'or category==8:
        return "Exiting..."
    
    else:return "INVALID QUERY! PLEASE, CHECK AND TRY AGAIN!!!"

#Convert a list into a dictionary
def listToDictionary():
    global dbDictionary
    global dbData
    for item in dbData:
        dd=item.split("|")
        length_name =len(dd[0])
        length_split = len(dd)
        if length_name >0 and length_split<5:
            if dd[0] in dbDictionary:
                pass
            else:
                dbDictionary[dd[0]]=item
#Convert the database list into a dictionary
listToDictionary()
'''
print(dbData)
print(len(dbData))
print(dbDictionary)
print(len(dbDictionary))
'''

    