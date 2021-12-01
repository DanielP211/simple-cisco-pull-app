import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test",
  database="cisco-devices"
)
