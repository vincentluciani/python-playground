import re

my_list = [1, 2, 3, 4, 5]

transformed_list = [2 * i for i in my_list]

print(transformed_list)

my_object = {"a":2,"b":3}

transformed_object = { k:v*2 for k,v in my_object.items() }

print(transformed_object)



#
my_string="<str>Architecture</str>/n<str>Racks & Physical Structures</str><str>Architecture 2</str>"
list_of_values=[]
matching_results = re.findall(r'<str>(.*?)</str>', my_string)
for matching_tuple in matching_results:
    list_of_values.append(matching_tuple)

print(list_of_values)



