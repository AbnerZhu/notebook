#! /usr/bin/env python

# with context manager

with open('new.txt', 'w') as f:
	print(f.closed)
	f.write("Hello World")
print(f.closed)