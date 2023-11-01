
                      ##    Database Crud App Using Xampp

import pymysql as p

def getconnect():
    return p.connect(host="localhost", user="root", password="", database="pyafsept")

def insertrec(data):
    db = getconnect()
    cr = db.cursor()
    sql = "insert into students values(%s, %s, %s, %s)"
    cr.execute(sql, data)
    db.commit()
    db.close()
    print("Data Inserted Successfully...")

def update(data):
    db = getconnect()
    cr = db.cursor()
    sql = "update students set name = %s, address = %s, email = %s where id = %s"
    cr.execute(sql, data)
    db.commit()
    db.close()
    print("Data Updated Successfully")

def delete(ids):
    db = getconnect()
    cr = db.cursor()
    sql = "delete from students where id = %s"
    cr.execute(sql, ids)
    db.commit()
    db.close()
    print("Data Deleted Successfully....")

def readdata():
    db = getconnect()
    cr = db.cursor()
    sql = "select * from students"
    cr.execute(sql)
    data = cr.fetchall()

    for i, n, e, a in data:
        print(f"{i:^5} {n:^15} {e:^20} {a:<25}")
        
    db.commit
    db.close()

while True:
    print("Menu:")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Read Data")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        id = input("Enter Id: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        
        data = [id, name, email, address]
        insertrec(data)
    elif choice == '2':
        id = input("Enter ID to update: ")
        name = input("Enter new Name: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")
        
        data = [name, email, address, id]
        update(data)
    elif choice == '3':
        id = input("Enter ID to delete: ")
        delete([id])
    elif choice == '4':
        readdata()
    elif choice == '5':
        break
    else:
        print("Invalid Key")

print("Exiting the program...")



















