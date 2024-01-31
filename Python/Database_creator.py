import mysql.connector
connect=mysql.connector.connect(host="localhost",user="root",passwd="abc123")

mycursor=connect.cursor()

mycursor.execute("drop database if exists restaurant")

mycursor.execute("CREATE database restaurant")
mycursor.execute("use restaurant")
    

mycursor.execute("create table table1( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table2( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table3( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table4( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table5( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table6( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table7( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table8( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table9( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table10( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table11( item varchar(100) , quantity int(3), total_cost int(8));")
mycursor.execute("create table table12( item varchar(100) , quantity int(3), total_cost int(8));")



mycursor.execute("create table menu( item varchar(100) , cost int(10) , time varchar(24));")


mycursor.execute("insert into menu values('Rice Idli',81,'Lunch'),('Sambhar Vada',85,'Lunch'),('Dahi Vada',81,'Lunch'),('Dosa (Butter)',125,'Lunch'),('Onion Dosa (Butter)',136,'Lunch'),('Paper Dosa',130,'Lunch'),('Mysore Dosa',123,'Lunch'),('Rawa Dosa',119,'Lunch'),('Onion Rawa Dosa',136,'Lunch'),('Onion Uttapam',155,'Lunch'),('Tomato Uttapam',155,'Lunch'),('Mix Veg Uttapam',155,'Lunch'),('Pav Bhaji',120,'Breakfast'),('Chole Bhature',110,'Breakfast'),('Chole  Kulche',100,'Breakfast'),('French Fries',106,'Breakfast'),('Chilli Cheese Toast',115,'Breakfast'),('Chilli Cheese Gralic Toast',115,'Breakfast'),('Garlic Bread',98,'Breakfast'),('Garlic Bread with Cheese',119,'Breakfast'),('Plain Sandwich',175,'Breakfast'),('Grilled Sandwich',175,'Breakfast'),('Club Sandwich',175,'Breakfast'),('Plain Cheese Pizza',190,'Breakfast'),('Capsicum, Onion Pizza',210,'Breakfast'),('Tomato, Onion Pizza',210,'Breakfast'),('Capsicum, Onion, Mushroom Pizza',250,'Breakfast'),('Jain Spl. Pizza',250,'Breakfast'),('Tandoori Pizza',250,'Breakfast'),('Super Veggie Pizza(Double Cheese)',210,'Breakfast'),('Shahi Paneer',210,'Dinner'),('Kadhai Paneer',210,'Dinner'), ('Paneer Butter Masala',210,'Dinner'),('Mushroom Masala',215,'Dinner'),('Malai Kofta',210,'Dinner'),('Dal Makhani',192,'Dinner'),('Yellow Dal',141,'Dinner'),('Rajma',141,'Dinner'),('Chole',141,'Dinner'),('Steam Rice',161,'Dinner'),('Soya Dum Biryani',220,'Dinner'),('Veg. Pulao',161,'Dinner'),('Mix Veg. Pulao',161,'Dinner'),('Jeera Pulao',161,'Dinner'),('Matka Biryani With Raita',220,'Dinner'),('Hyderabadi Biryani',220,'Dinner'),('Plain Raita',102,'Dinner'),('Boondi Raita',108,'Dinner'),('Mix Veg. Raita',110,'Dinner'),('Jeera Raita',115,'Dinner'),('Pineapple Raita',130,'Dinner'),('Gulab Jamun',60,'Extras'),('Halwa (Seasonal)',60,'Extras'),('Fruit Punch',150,'Extras'),('Red Sea',150,'Extras'),('Love Valley',150,'Extras'),('Pomi Twist',150,'Extras'),('Fresh Juices Seasonal/Mix',160,'Extras')");

connect.commit()


print("Database created successfully now you can work")
