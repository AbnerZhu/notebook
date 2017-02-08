#!/usr/bin/env python

# without context manager
f = open('new.txt', 'w')

print(f.closed) # whether the file is open

f.write("Hello World")
f.close()
print(f.closed)