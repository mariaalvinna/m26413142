#!/usr/bin/python
list=["ftp",21,"http",80,"ssh",22]
del list[0:2]
print(list)
list.remove("http")
print(list)
