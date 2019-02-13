import sys
from collections import deque

# number, time_period, text, delimiter
Q = deque(maxlen=4) 


NUM = 'number'
DELIM = 'delimiter'
PERIOD = 'period'
TEXT = 'text'


def get_line_type(line):
    if line is None:
        return
    line = line.strip()
    if line == '':
        return DELIM
    if '-->' in line:
        return PERIOD
    if line.isdigit():
        return NUM

    #else
    return TEXT

def get_last_el(container):
    try:
        return container[-1]
    except IndexError:
        pass

    
lines = []

# number, time_period, text (exclude delimiter)
last_data_type = None
input_file = sys.argv[1]
output_file = sys.argv[2]


with open(input_file, 'r') as f:
    for line in f:
        line = line.decode('utf-8-sig').encode('utf-8')
        ltype = get_line_type(line)

        prev_val = get_last_el(lines)
        prev_ltype = get_line_type(prev_val)

#        print 'line', [line], ltype, Q


        if  ltype == TEXT and prev_ltype == DELIM:
            lines.pop()


        lines.append(line)

    



# for line in lines:
#     print 'l', line.strip()

with open(output_file, 'w') as f:
    for line in lines:
        f.write(line)
