
def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def gange(x, y):
    return x * y
def dele(x, y):
    return x / y
    
print("1.Plus")
print("2.Minus")
print("3.Gange")
print("4.Dele")

while True: 
    choice = input("Skriv(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Første nummer: "))
        num2 = float(input("Andre rummer: "))
        if choice == '1':
            print(num1, "+", num2, "=", plus(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", minus(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", gange(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", dele(num1, num2))
        next_calculation = input("bruk igjen (ja/nei): ")
        if next_calculation == "nei":
          break

