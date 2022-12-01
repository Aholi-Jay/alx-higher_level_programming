#!/usr/bin/python3
#3-infinite_add.py

if __name__ == '__main__':
    import sys

# index = len(sys.argv) - 1
Total = 0
for i in range(len(sys.argv) - 1):
    Total += int(sys.argv[i+1])
print("{}".format(Total))