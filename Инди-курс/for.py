
z = set()
for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            for d in range(1, 50):
                if (a ** 3 + c ** 3) == (b ** 3 + d ** 3) and b != a and b != c and d != a and d != c:
                    z.add(a**3+c**3)
print(sorted(z)[0:5])

