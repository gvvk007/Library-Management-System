import mysql.connector as ms

db=ms.connect(
    host="127.0.0.1",
    user="root",
    password="gvvk@007",
    database='library',
    autocommit=True
)

cursor=db.cursor()

sql="describe books"
cursor.execute(sql)

for x in cursor:
    print(x)

print("================================ LIBRARY MANAGEMENT SYSTEM ================================")
print("WELCOME!")
print("Select User:")
print("\t\t 1.ADMIN \t\t 2.USER")
n=int(input())
if n==1:
    u=input("Username:")
    p=input("Password:")
else:
    print("Please Choose your service,")
    print()
