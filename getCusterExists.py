import sys
def exists():
    inputValue =  sys.argv[1]
    exists = inputValue.find('not found')
    f = open("clusterExistsValue", "w")
    f.write(str(exists))
    f.close
    return str(exists)

if __name__ == '__main__':
    sys.stdout.write(exists())