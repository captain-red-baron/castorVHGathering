import pymssql

server = 'localhost'
user = 'SA'
password = '<CastorVH!Passw0rd>'
dbname = 'CastorVH'

conn = pymssql.connect(server, user, password, dbname)
cursor = conn.cursor()

print('aaa')

conn.close()