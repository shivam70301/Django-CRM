import mysql.connector
print("MySQL Connector is working!")

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    auth_plugin='mysql_native_password'  # Add this line
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
