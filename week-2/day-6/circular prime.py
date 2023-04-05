'''The number, 197, is called a circular prime because all
 rotations of the digits: 197, 971, and 719, are themselves
 prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11,
13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of
circular primes less than the given limit.'''


'''here i have done the '''

final_l=[]
for i in range(1,100+1):
    if i >1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i not in final_l:
                a = str(i)
                a = a[::-1]
                a = int(a)
                for j in range(2, i):
                    if a % j == 0:
                        break
                else:
                    final_l.append(i)
                    if a not in final_l:
                        final_l.append(a)
print(sorted(final_l))

