import mysql.connector
  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "pranali" , 
  database = "record_db1"
)

mycursor = mydb.cursor()

def create_databases():
    mycursor.execute("CREATE DATABASE record_db1")
    mycursor.execute("SHOW DATABASES")

    


def create_table1():
   mycursor.execute(
   """CREATE TABLE Old_CUSTOMER1
   (id int,
    first_name varchar(255),    
   last_name varchar(255),
   age int,
   gender varchar(20),
   email varchar(255), 
   city varchar(50))"""
   )


def create_table2():
    mycursor.execute(
    """CREATE TABLE New_CUSTOMER1
    (id int,
    first_name varchar(255),    
    last_name varchar(255),
    age int,
    gender varchar(20),
    email varchar(255), 
    city varchar(50))"""
    )
    


def insert_record_O():
    sql = "INSERT INTO Old_customer1 (id, first_name, last_name, age, gender, email, city)  VALUES  (%s, %s, %s, %s, %s, %s, %s)"
    val = [
        (1,'Jay','Khurana',21,'M','jay@gmail.com','Indore' ),
        (2,'Abhay','Sharma',24,'M','abhay@gmail.com','Indore' ),
        (3,'Jiya','patel',26,'F','jiya@gmail.com','Pune' ),
        (4,'Manas','kumar',21,'M','manas@gmail.com','Kolhapur' ),
        (5,'Mayra','Khanna',24,'F','mayra@gmail.com','Indore' ),
        (6,'Rani','Mishra',21,'F','rani@gmail.com','Pune' ),
        (7,'Reshma','Mishra',22,'F','reshma@gmail.com','Jaipur' ),
        (8,'Poonam','Patil',26,'F','poonam@gmail.com','Satara' ),
        (9,'Rehansh','Khurana',24,'M','rehansh@gmail.com','Sangli' ),
        (10,'Sai','Patil',22,'F','sai@gmail.com','Pune' ),
        (11,'Rajesh','Patel',25,'M','rajesh@gmail.com','Indore' ),
        (12,'Priyaj','Sharma',23,'M','priyaj@gmail.com','Satara' ),
        (13,'Priya','Sharma',23,'F','priya@gmail.com','Satara' ),
        (14,'Sayali','Patil',24,'F','sayali@gmail.com','Ratnagiri' ),
        (15,'Mohan','Mulik',22,'M','mohan@gmail.com','Gargoti' ),
        (16,'Shamal','Naik',26,'M','shamal@gmail.com','Patan' ),
        (17,'Ruhi','Bhalla',25,'F','ruhi@gmail.com','Indore' ),
        (18,'Rohit','Jirage',21,'M','rohit@gmail.com','Karad' ),
        (19,'Alia','Khurana',24,'F','alia@gmail.com','Mumbai' ),
        (20,'Rohan','Mane',20,'M','rohan@gmail.com','Mumbai' )
        ]
      
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def insert_record_N():
    sql = "INSERT INTO New_customer1 (id, first_name, last_name, age, gender, email, city)  VALUES  (%s, %s, %s, %s, %s, %s, %s)"    
    val = []

    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


user_input = input("""\nPlease select your option -
                           \n1) age
                           \n2) city 
                           \n3) gender\n""")
print(user_input)
if user_input == "1":
        
    val_input=input("""\nEnter the age limit:- """)  
    val_name="age" 
elif user_input == "2":
        
    val_input=input("""\nEnter the city:- """) 
    val_name="city" 
elif user_input == "3":
       
    val_input=input("""\nEnter the gender as F or M:- """) 
    val_name="gender" 


def insert_record():
    if(user_input=="1"):
        sql = """INSERT INTO new_customer1 
        select * from old_customer1
        where %s >= '%s' """  
    else:
        sql = """INSERT INTO new_customer1 
        select * from old_customer1
        where %s = '%s' """  

    
    
      
    mycursor.execute(sql % (val_name,val_input))
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  


create_databases()
create_table1()
create_table2()
insert_record_O()
insert_record_N()
insert_record()
