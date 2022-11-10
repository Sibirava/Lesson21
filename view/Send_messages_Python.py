# Send messages
#1) methods (object methods)
# point = Point2D()
# point.method()
# Point2D.method() <-- Type error

#2) functions
# point = Point2D()
# point.function <-- Type error()
# Point2D.fuction()

#3)staticmethods(functions)
# point = Point2D()
# point.some() ---> Point2D.some()  <-- It's work
# Point2D.some()                    <-- It's work

#4) classmethods                     только тот код, который завязан на самих классах или для контроля экз класса
                                    # например, посчитать количество объектов класса
# point = Point2D()
# point.some() ---> Point2D.some() <-- It's work
# Point2D.some()                   <-- It's work


########################################################################
   #3 EXAMPLE
# class Point2D:
#
#     @staticmethod   # самодостаточный код, аналог наших функций
#     def sum(a, b):
#         return a + b
#
#     #выведут одинаковое, эта функция не требует состояние экз класса
#     print(Point2D.sum(5, 6))
#     print(Point2D().sum(5, 6))

########################################################################
#     4 EXAMPLE  только на имени класса!

# class Point2D:
#
#     @classmethod
#     def just_do_it(cls):
#         pass
