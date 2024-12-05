def weathering_model():
    a = 0.1
    b = 0.5
    c = 2
    x = 3 
    W = a * x**2 + b * x + c
    
    print(f"Weathering index (W): {W}")

weathering_model()
