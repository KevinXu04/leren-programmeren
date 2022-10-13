currentDay = input("What day is it? ")

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
x = 0
while True:
    print(week[x])
    if week[x] == currentDay:
        break
    x += 1