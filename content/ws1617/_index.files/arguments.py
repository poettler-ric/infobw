import sys

for i in range(len(sys.argv)):
    print("argument at position {}: {} ({})".format(i, sys.argv[i], type(sys.argv[i]))) 
