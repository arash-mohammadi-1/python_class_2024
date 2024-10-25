

#class MyClass:
#    x = 5

#کامند اینیت چیز هایی که برای به وجود اوردن یک اب جکت نیاز داشته باشیم تعریف میکنه
class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.soul = True

    def show_name(self):
        print(f"My name is {self.name}")


if __name__ == "__main__" :
#    p = MyClass()
#    print(p.x)
    p1 = person("Ali", 15)
    print(p1.name)
    print(p1.soul)
    print(p1.age)
    
    p2 = person("zahra", 17)
    print(p2.name)
    print(f"before death {p2.soul}")
    print(p2.age)
    p2.soul = False
    print(f"after death {p2.soul}")
    print(p2.show_name())
