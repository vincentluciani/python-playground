from collections import defaultdict


class MyData():
    def __init__(self):
        self.data = defaultdict(dict)

    def add(self,level1,level2,value):
        self.data[level1][level2]=value

# works only with 2 levels
my_data = MyData()
my_data.add("level1","level2","value")

my_dictionnary={}



from collections import defaultdict

nested_dict = lambda: defaultdict(nested_dict)
nest = nested_dict()

nest[0][1][2][3][4][5] = 6
nest[0][1][22][3][4][5] = 7


print(nest)
my_dictionnary={"level1":{}}

my_dictionnary={"level1":{"level2":{"level3":"3"}}}


my_dictionnary = {"level1":{"level2":{"level3":"3","level3b":"3b"}}}



from collections import defaultdict
class Tree(defaultdict):
    def __init__(self):
        super(Tree, self).__init__(Tree)

root = Tree()
root[0][1][2][3][4][5] = 7
root[0][1][22][3][4][5] = 8

print(root[0][1][2][3][4][5])
print(root[0][1][22][3][4][5])


class NestedDict(dict):
    def __missing__(self, key):
        self[key] = NestedDict()
        return self[key]

root2 = NestedDict()
root2[0][1][2][3][4][5] = 7
root2[0][1][22][3][4][5] = 8

print(root2[0][1][2][3][4][5])
print(root2[0][1][22][3][4][5])

# root.value = 1
# root['a']['b'].value = 3
#
#
#
# print root['a']['b'].value
# print root['c']['d']['f'].value

