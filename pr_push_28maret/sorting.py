#!/usr/bin/python
i = 0
d = []
n = raw_input("Masukkan banyak data: ")
while i < n:
        a = raw_input("Masukkan data ke ",)
        d.append(a)
        i = i + 1
d.sort()
j = n - 1
while j >= 0:
        print d[j]
        j = j - 1
