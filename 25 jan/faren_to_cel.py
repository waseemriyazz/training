def fahrenheit_to_celsius_table(start, end, step):
    print("Fahrenheit\tCelsius")
    
    current_temp = start
    while current_temp <= end:
        celsius = (current_temp - 32) * 5.0/9.0
        print(f"{current_temp}\t\t{celsius:.2f}")
        current_temp += step

fahrenheit_to_celsius_table(0, 100, 20)