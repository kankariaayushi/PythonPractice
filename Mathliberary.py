# # import src.math1 as math1
# #from src import math1
#
# from src.math1 import sumofvar, subofvar
#
# if __name__ == '__main__':
#     #print("sum== + {}" .format(math1.sumofvar(2,3)))
#     print("sum== + {}".format(sumofvar(2, 3)))
#     print("sum== + {}".format(subofvar(2, 3)))
#
#

from src.mathclass import MathClass

if __name__ == '__main__':
    obj1= MathClass(2,3)
    print("sum=+ {}".format(obj1.sumofvar()))
    print("Current file=={}".format(__name__))

