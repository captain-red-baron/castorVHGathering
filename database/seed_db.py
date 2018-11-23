import os
import pymssql

server = 'localhost'
user = 'SA'
password = '<CastorVH!Passw0rd>'
dbname = 'castor'

conn = pymssql.connect(server, user, password, dbname)
cursor = conn.cursor()

# Execute the provided statements
with open("database/dll_statements.sql", "r") as inp:
    for section in inp.read().split("GO"):
        #print(section)
        cursor.execute(section)

with open("database/college_seed.sql", "r", encoding="utf-8") as inp:
    cursor.execute(inp.read().replace("\uFEFF", ""))

with open("database/immunization_seed.sql", "r", encoding="utf-8") as inp:
    cursor.execute(inp.read().replace("\uFEFF", ""))

# Make a new table where the scraping results will be stored.

TABLE_GEN_STATEMENT = """
    CREATE TABLE castor.dbo.ImmunizationInformation (
        Id int NOT NULL IDENTITY(1,1),
        CollegeId int NOT NULL,
        Information varchar NOT NULL,
        CONSTRAINT PK_ImmunizationInformation_1 PRIMARY KEY (Id),
        CONSTRAINT FK_ImmunizationInformation_1 FOREIGN KEY (CollegeId) REFERENCES castor.dbo.College(Id)
    )
"""

cursor.execute(TABLE_GEN_STATEMENT)

conn.commit()

conn.close()