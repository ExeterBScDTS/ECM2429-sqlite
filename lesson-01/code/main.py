# This example taken from the sqlite3 documentation at https://docs.python.org/3/library/sqlite3.html
#

import sqlite3

# Create a temporary database in memory.
conn = sqlite3.connect(':memory:')
# More usual is to have a database file, e.g.
# conn = sqlite3.connect('stocks.db')

c = conn.cursor()

# Create table
c.execute('''create table stocks
(date text, trans text, symbol text,
 qty real, price real)''')

# Insert a row of data
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")

# Larger example
for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
         ]:
    c.execute('insert into stocks values (?,?,?,?,?)', t)

# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()

# Now retreive the data
c = conn.cursor()
c.execute('select * from stocks order by price')
for row in c:
    print(row)

c.close()
conn.close()
