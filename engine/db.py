import sqlite3

conn = sqlite3.connect("vai.db")

cursor = conn.cursor()

# Create table for opening system application which can not be opened directly.
# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'MS WORD', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word.exe')"
# cursor.execute(query)
# conn.commit()

# Create table for opening web commands
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'CODECHEF', 'https://www.codechef.com/users/paridhi28')"
# cursor.execute(query)
# conn.commit()

# testing module
app_name = "notepad"
cursor.execute("SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
results = cursor.fetchall()
print(results[0][0])