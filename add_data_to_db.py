import psycopg2
import json

user = 'postgres'
pwd = '123456'
port = 5438
host = '127.0.0.1'
db_name = 'engilsh_thesaurus_db'

con = psycopg2.connect(
    database=db_name,
    user=user,
    password=pwd,
    host=host,
    port=port
)
data = json.load(open('data.json'))
cursor = con.cursor()
for key, value in data.items():
    key = key.replace("\'", "\'\'")
    if type(value) == list:
        for i in value:
            i = i.replace("\'", "\'\'")
            sql = '''
            insert into dictionary (expression, definition) values (\'%s\',\'%s\')
            ''' % (key, i)
            cursor.execute(sql)
    else:
        value = value.replace("\'", "\'\'")
        sql = '''
                    insert into dictionary (expression, definition) values (\'%s\',\'%s\')
                    ''' % (key, value)
        cursor.execute(sql)

con.commit()

print('success')
