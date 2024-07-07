import mysqldb

def main():
    print("1. Register new student details")
    print("2. delete student  details")
    print("3. update student details")
    option=int(input("enter the option"))
    if option==1:
        name=input("enter name")
        age=int(input("enter age"))
        obj=mysqldb.connectDb()
        obj.insert(name,age)
        print("registered new details")
	
    elif option==2:
        sid=int(input('enter student id'))
        obj=mysqldb.connectDb()
        obj.deleteRecord(sid)
        print(f"student id {sid} row deleted")
    elif option==3:
        print("1.update student name")
        print("2.update student age")
        opt=int(input("enter option"))
        if opt==1:
            sid=int(input("enter the id to change name"))
            newname=input("enter the name to change")
            obj=mysqldb.connectDb()
            obj.updatestudentname(sid,newname)
            print(f"name got updated into {newname}")
        elif opt==2:
            sid=int(input("enter the sid"))
            newage=int(input("enter the age to change"))
            obj=mysqldb.connectDb()
            obj.updatestudentage(sid,newage)
            print(f"student age got updated into {newage}")
    else:
        print("invalid option")
main()