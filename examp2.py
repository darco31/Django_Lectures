# class Book():

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"{self.title} written by {self.author}"

#     def __len__(self):  # Len has to return an integer
#         return self.pages


# mybook = Book("Python ROCKS!", "Stephen", 200)

# print(mybook)
# print(len(mybook))


class Students():

    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)

    def __str__(self):
        return f"{self.names}"


student1 = Students(['Stephen', 'Lisa', 'Mark', 'Peter'])

print(len(student1))
print(student1)
