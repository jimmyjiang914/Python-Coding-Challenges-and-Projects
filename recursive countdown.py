def countDown(num):
    if num <= 0:
        print("All done!")
        return
    print(num)
    num -= 1
    countDown(num)

print(countDown(100))