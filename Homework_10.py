class Book:
    def __init__(self, title, author, is_borrowed = False):
        self._title = title
        self._author = author

        self._is_borrowed = is_borrowed


    def borrow_book(self):
        self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False

    def get_status(self):
        if self._is_borrowed is True:
            return 'Взята'
        else:
            return 'Доступна'


qa_theory = Book(title='Теория тестирования', author= 'Пупкин')
qa_theory1 = Book(title='Теория тестирования1', author= 'Пупкин')

print(qa_theory1.get_status())

qa_theory1.borrow_book()
print(qa_theory1.get_status())

qa_theory1.return_book()
print(qa_theory1.get_status())