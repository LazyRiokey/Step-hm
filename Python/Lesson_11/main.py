# import openpyxl as xl
# from random import randint

# book = xl.Workbook()
# book.create_sheet('Sheet_2')
# book.remove(book['Sheet'])
# new_active = book.active

# for i in range(10):
#     new_active.cell(row=i + 1, column=1, value=randint(0, 100))

# book.save('new_file.xlsx')
# book.close()

# new_book = xl.load_workbook('new_file.xlsx')
# new_book_active = new_book.active

# new_book_active['B2'].value = '=SUM(A1:A10)'
# new_book.save('new_file_copy.xlsx')
# new_book.close()

# class Car:
    
#     def __init__(self):
#         print('Машина запустилась!')

# my_obj = Car()


class Stack:

    def __init__(self):
        self._stack_list = []
    
    def push(self, val):
        self._stack_list.append(val)
        return self._stack_list[-1]
    
    def pop(self):
        tmp = self._stack_list[-1]
        del self._stack_list[-1]
        return tmp

class Summa(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__result = 0
    
    def push(self, val):
        self.__result += Stack.push(self, val)
    
    def pop(self):
        self.__result -= Stack.pop(self)
    
    def getSum(self):
        return self.__result

# my_obj = Stack()
# print(my_obj.push(10))

obj = Summa()
obj.push(20)
obj.push(30)
obj.push(40)
print(obj.getSum())
obj.pop()
print(obj.getSum())
print(obj._stack_list)