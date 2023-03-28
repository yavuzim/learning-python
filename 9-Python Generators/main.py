def kub():
    for i in range(51):
        yield i**2

generator = kub()
iterator = iter(generator)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
#########################################################
        
generator = (i**2 for i in range(5))
print(next(generator))
