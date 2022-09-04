#в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print('I')
elif x<0 and y>0:
    print('II')
elif x<0 and y<0:
    print('III')
elif x>0 and y<0:
    print('IV')

    #Найти расстояние между двумя точками пространства
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)