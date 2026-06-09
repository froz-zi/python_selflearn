for x in range(-10, 11):
    y = x**2 + 6*x + 9

    if y == 0:
        print("Nilai x:", x)
        print("Nilai y:", y)



jawaban = []

for x in range(-10, 11):
    y = x**2 + 6*x + 9

    if y == 0:
        jawaban.append(x)

print("Nilai x yang membuat y = 0 adalah:", jawaban)