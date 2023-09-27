# scope variable
a = 5


def f1():
    a = 2
    print(a)


print(a)  # Will print 5
f1()  # Will print 2

# Global Variables
a = "Hello"


def prints_a():
    print(a)


# will print "Hello"
prints_a()
