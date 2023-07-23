import sys
import re
import pdfkit
from operator import itemgetter
from itertools import groupby

file = sys.argv[1]
file_handle = file.split('.')[0]
with open(file) as file:
    fc = file.read()
    bolds = [m.start() for m in re.finditer('\*\*', fc)]
    fc = list(fc)
    for i, b in enumerate(reversed(bolds)):
        if i%2 == 0:
            fc[b:b+2] = '</strong>'
        else:
            fc[b:b+2] = '<strong>'
    
    fc = ''.join(fc)
    italics = [m.start() for m in re.finditer('\*', fc)]
    fc = list(fc)
    for i, b in enumerate(reversed(italics)):
        if i%2 == 0:
            fc[b:b+1] = '</em>'
        else:
            fc[b:b+1] = '<em>'
    
    fc = ''.join(fc)
    header = [m.start() for m in re.finditer('=', fc)]
    print(header)
    fc = list(fc)

    ranges = []
    for k,g in groupby(enumerate(header),lambda x:x[0]-x[1]):
        group = (map(itemgetter(1),g))
        group = list(map(int,group))
        ranges.append((group[0],group[-1]))
    
    for i, b in enumerate(reversed(ranges)):
        fc[b[0]-1] = '</h1>' # replace break with h1
        fc.insert(b[0] - (b[-1]-b[0])-2, '<h1>')
    
    fc = [i for i in fc if i != '=']
    fc = ''.join(fc)

    linebreaks = [m.start() for m in re.finditer('\n', fc)]
    fc = list(fc)
    for i, b in enumerate(reversed(linebreaks)):
        fc[b:b+1] = '<br>'
    
    fc = ''.join(fc)
print(fc)
pdfkit.from_string(fc, file_handle + '.pdf')
        
