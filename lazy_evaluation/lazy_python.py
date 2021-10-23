def condition1() -> False:
    print("condición 1 devuelve False")
    return False

def condition2() -> True:
    print("condición 2 devuelve true")
    return True

print("\nEvaluación perezosa or lazy evaluation en Python\n")

condition1() and condition2()

print("\n")

condition2() and condition1()

print("\nFin del código en Python\n")