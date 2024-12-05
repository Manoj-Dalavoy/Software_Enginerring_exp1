def weathering_model():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    x = float(input("Enter value of x: "))
    W = a * x**2 + b * x + c
    
    print(f"Weathering index (W): {W}")

weathering_model()
