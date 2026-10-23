guess = input("At n = 1000, O(n^2) takes how many steps?")

input("watch O(n) and O(n^2) grow. press enter")
for n in [10, 100, 1000]:
    input("n =", + str(n) +" press enter")
    print(" O(n) =", n, " O(n^2) =", n * n)

print(" your guess:", guess)
input("full ladder at n = 1000. press enter")
print(" O(1) = 1 O(log n)= 10 O(n)=1000 O(n^2)= 1,000,000")
