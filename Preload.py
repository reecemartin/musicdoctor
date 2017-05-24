file = open('info.txt', 'r').readlines()

dict_ = {}

for line in file:
    temp = line.split(', ')

    dict_[temp[0].upper()] = {'NAME': temp[0], 'SAD': float(temp[1]), 'HEAVY': float(temp[2]), \
                      'ARTISTIC': float(temp[3]), 'POPULAR': float(temp[4]), 'ELECTRONIC': float(temp[5])}

file = open('data.dat', 'w')
file.write(str(dict_))
