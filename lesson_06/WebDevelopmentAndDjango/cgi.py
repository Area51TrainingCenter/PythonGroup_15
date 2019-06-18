import sqlite3


print("<html><head><title>Books</title></head>")
print("<body>")
print("<h1>Books</h1>")
print("<ol>")

connection = sqlite3.connect("library.db")
cursor = connection.cursor()
cursor.execute("SELECT author FROM book ORDER BY price")

for row in cursor.fetchall():
    print("<li>{}</li>".format(row[0]))

print("</ol>")
print("</body></html>")

connection.close()

