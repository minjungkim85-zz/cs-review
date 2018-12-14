# This is Python 2
import sys

line = sys.stdin.readline()
line = int(line)
string = "Hello\r\n"*line
string = string[:-1]

print string
