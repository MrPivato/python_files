x = 3
y = 5

for i in range(0, 100):

    word = ""

    if (i%x == 0): word += "Fizz"
    if (i%y == 0): word += "Buzz"
    if (word == ""): word = i

    print(word)
