import mysql.connector
mydb=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="123456789",
                database="suresh"
                )

mycursor=mydb.cursor()
no=input("enter your id no:")
data=(no,)
q="select  bal from banking where id1=%s"
mycursor.execute(q,data)
a=[]
for i in mycursor:
    a.append(list(i))
aa=22
b=(a[0][0])+aa
bal1=str(b)
sql2 = "update banking set bal = "+bal1+"  where id1 ="+no
mycursor.execute(sql2,{'bal1':20})
mycursor.execute("select*from banking")
for i in mycursor:
    print(i)
print(bal1)
print(type(bal1))

ch=input("enter1")
if ch=="1":
    mycursor.execute("select*from banking")
    for i in mycursor:
        print(i)
else:
    print("ok")

"""
  s = dt.strftime('%Y-%m-%d %H:%M:%S')
    sql2 = "UPDATE accelerometer SET test = "+ s +"WHERE _id="+i
    cursor.execute(sql2)
    data = cursor.fetchall()



class banking:
    def creating(self):
        mycursor=mydb.cursor()
        a=eval(input("enter"))
        mycursor.execute("select id1 from bank")
        accounts=[]
        for i in mycursor:
            accounts.append(list(i))
        l=len(accounts)
        acc={''}
        for j in range(l):
            acc.add(accounts[j][0])
        if a in acc:
            print("Account already exixts")
        else:
            print("you can create account on this number")

    def created(self):
        mycursor=mydb.cursor()
        id1=input("enter your id")
        name=input("enter your name")
        bal=input("enter balence of first deposited ")
        s="insert into bank values(%s,%s,%s)"
        t=(id1,name,bal)
        mycursor.execute(s,t)
        mydb.commit()

        print ( 'Data entered successfully.' )
    def depositing(self):
        print("hai")
bank=banking()

while True:
    ch=input("select your choice:\n1:for creating id:\n2:for creating account\n3:for depositing\n4:for crediting\nenter:")
    
    if ch=="1":
            bank.creating()
    elif ch=="2":
        bank.created()
    elif ch=="3":
        bank.depositing()
    else:
        print("enter correct option")
    



 

"""
