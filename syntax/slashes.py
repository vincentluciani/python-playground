import json

mystring = 'test " '


mystringtransformed = mystring.replace('"','\"')
print(mystring)
print(mystringtransformed)


mydictionnary = {'abc':mystringtransformed}

mydictionarystring = json.dumps(mydictionnary)

myseconddictionnarystring = '{"abc": "test \\\\\\" "}'



test2 = json.loads(myseconddictionnarystring)
test1 = json.loads(mydictionarystring)

print(test1)

mystring = "test '"


mystringtransformed = mystring.replace("'","\\'")
print(mystring)
print(mystringtransformed)


# currently we are replacing ' by " unfortunately
# we should do json.dump instead of str() !!!!