def problem2_7():
    a = input()
    b = input()
    c = input()
    a = float(a)
    b = float(b)
    c = float(c)
    s = ( a + b + c )/2
    area = (s*(s-a)*(s-b)*(s-c))**.5
    print("Area of a triangle with sides",float(a),float(b),float(c),"is",float(area))