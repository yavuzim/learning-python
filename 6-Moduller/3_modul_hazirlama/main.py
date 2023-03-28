import mod

print(dir(mod))
print(help(mod))
print(help(mod.func))
print(mod.number)
print(mod.numbers)
print(mod.person["isim"])
print(mod.func(10))

p = mod.Person()
print(p.speak())