a, b, c = map(int,input("Введите величины сторон треугольника через пробел").split())
p = a + b + c
if a > b + c or b > a + c or c > a + b :
    print ("Периметр треугольника невозможно вычислить - задан несуществующий треугольник")
if a < b + c and b < a + c and c < a + b :
    print ("Периметр треугольника равен", p)