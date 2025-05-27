class Customer:

    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, i):
        if i < 0:
            raise ValueError("Invalid input")
        self.__id = i

    def __str__(self) -> str:
        return f"Customer <{self.name}> (ID: <{self.__id}>) - Email: <{self.email}>"

    def __repr__(self) -> str:
        return f"Customer(name='<{self.name}>', email='<{self.email}>', id=<{self.__id}>)"


c1 = Customer("Alice", "alice@example.com", 101)
c2 = Customer("Bob", "bob@example.com", 202)

print(c1)
print(repr(c2))

c1.id = -5
print(c1)
