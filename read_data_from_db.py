import psycopg2
from difflib import get_close_matches

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
def get_definition(word):
    cursor = con.cursor()
    query = cursor.execute('''
    SELECT * FROM Dictionary WHERE Expression = '%s'
    ''' % word)
    results = cursor.fetchall()
    return results

cursor = con.cursor()
query = cursor.execute('''
SELECT Expression FROM Dictionary''')
dictionary = [res[0] for res in cursor.fetchall()]

def translate(word):
    word = word.lower()
    if get_definition(word):
        return get_definition(word)
    elif get_definition(word.title()):
        return get_definition(word.title())
    elif get_definition(word.upper()):
        return get_definition(word.upper())
    elif len(get_close_matches(word,dictionary)) > 0:
        best_match = get_close_matches(word, dictionary)[0]
        answer = input("Did you mean %s instead? Enter Y if yes, or N if no: " % best_match)
        if answer == "Y":
            return get_definition(best_match)
        elif answer == "N":
            return "The word doesn't exist, Please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist, Please double check it"


word = input("Enter word: ")

output = translate(word)
if type(output) == list and len(output)!=0:
    for item in output:
        print(item[1])
else:
    print(output)
