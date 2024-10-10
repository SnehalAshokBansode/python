def Fibo(terms2):
    f1 = 0
    yield f1
    if terms2 > 1:
        f2 = 1
        yield f2
        
        for _ in range(2, terms2):
            f3 = f1 + f2
            yield f3
            f1 = f2
            f2 = f3

# Main body
terms1 = int(input("How many terms: "))
gen = Fibo(terms1)

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
