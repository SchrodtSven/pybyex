# lambda.py
# Anonymous (without name) functions
#
# AUTHOR Sven Schrodt <sven@schrodt.club>
# SINCE 2025-01-29


"""Lambda
An anonymous inline function consisting of a *single expression* which is 
evaluated when the function is called. The syntax to create a lambda function
is lambda [parameters]: expression"""


words = ['Awk,', 'Alle', 'meine', 'Entchen', 'schwimmen', 'auf', 'dem ','Sed']

upper_words = [x.upper() for x in words]
foo = [(lambda x: x*x)(x) for x in range(10)]
print(foo)
# or simply:

bar = [x*x for x in range(10)]
 
print(bar)

print(foo == bar)
# dotted = [(lambda x: x+'.') (x) for x in words]#


#exit(233)

dotted = [ x+'.' for x in words]
print(upper_words) 
print(dotted)

def lambda_me(*my_list, callable):
    new_list = []
    print(my_list)
    print(type(my_list))
    for x in my_list:
        print(x)
        #new_list.append(callable(x))
    #return new_list

doubled = lambda_me([2,3,4,55], callable=lambda x: 2*x)
print(doubled)

titles = ("Dr.", "Duke of Neverland", "Freiherr von Pappel", "Madame", "Sir", "Queen", "Chancelor")
names = ("Maier", "Müller", "Schmitt", "Doro", "Kolp", "Prime", "Palpatine")

my_lambda = lambda a,b: a + ' ' + b

print(my_lambda(titles[1], names[1]))


# lamda as parameter of map 
new = map(lambda x, y: x + ' ' + y, titles, names)
print(new) # map object
#print(list(new)) # list
print(tuple(new)) # list
# with comprehension
comp_lis = [' '.join(both) for both in zip(titles, names)] 
print(comp_lis)



class frog:
    pos = (0, 0)
    def __init__(self, **kwargs):
        self.kw = kwargs
    
    