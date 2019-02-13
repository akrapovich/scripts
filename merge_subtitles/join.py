#!/usr/bin/env python
import sys
import codecs
import re
import argparse

# types:
NUM = 'number'
DELIM = 'delimiter'
PERIOD = 'period'
TEXT = 'text'

def is_number(line):
    if line.isdigit():
        return 'number'

def is_time(line):
    """
       TODO: use regexp
    """
    if '-->' in line:
        return 'time'

def is_delimiter(line):
    if line.strip() == '':
        return 'delimiter'

def is_text(line):
    # TOOD: regexp
    if not is_delimiter(line) and not is_time(line) and not is_number(line):
        return 'text'


def next_line(gen):
    """
    return tuple (<type>, <line>)
    """
    line = gen.next()
    typ = None

    if line.isdigit():
        typ = NUM
    elif '-->' in line:
        typ = PERIOD
    elif line.strip() == '':
        typ = DELIM
    elif not is_delimiter(line) and not is_time(line) and not is_number(line):
        typ = TEXT
    else:
        raise Exception('unknown')

    return typ, line
    
def get_line_type(line):
    if line.isdigit():
        return NUM
    elif '-->' in line:
        return PERIOD
    elif line.strip() == '':
        return DELIM
    elif not is_delimiter(line) and not is_time(line) and not is_number(line):
        return TEXT
    
    else:
        raise Exception('unknown')



def read_file(file_name):
    with codecs.open(file_name, 'r', 'utf-8-sig') as f:
        for i, line in enumerate(f.readlines()):
            # if i == 40:
            #     break
            yield line.strip()


def get_text(gen):
    result = []
    ltype = None
    while ltype != DELIM:
        ltype, line = next_line(gen)
        if ltype == DELIM:
            continue
        assert ltype == TEXT, (ltype, line)
        result.append(line)

    return result
    
            

def next_frag(gen):
    for line in gen:
        ltype = get_line_type(line)
        if ltype == DELIM:
            continue
        assert ltype == NUM, (ltype, line)
        num = line
        ltype, line = next_line(gen)
        assert ltype == PERIOD, (ltype, line)
        period = line

        text_list = get_text(gen)
        yield num, period, text_list



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('en')
    parser.add_argument('ru')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-of', default=False, help='if not set, gen file name automatic')

    args = parser.parse_args()
    return args

ignore_num = True
if __name__ == '__main__':
    args = get_args()


    en_gen = read_file(args.en)
    ru_gen = read_file(args.ru)

    if args.of:
        of = args.of
    else:
        of = 'en-ru.str' # TODO: parse input files like: s02e02_en-ru.str

    with open(of, 'w') as f:
        for n, p, t in next_frag(en_gen):
            print 'd:', n,p,t
            nr, pr, tr = next_frag(ru_gen).next()
            print 'r:', nr,pr,tr

            if not ignore_num:
                assert n == nr, (n, nr)
            f.write(n)
            f.write('\n')
            f.write(p)
            f.write('\n')
            for en_text in t:
                f.write(en_text.encode('utf-8'))
                f.write(' ')
            f.write('\n')
            f.write('\n')

            for ru_text in tr:
                f.write(ru_text.encode('utf-8'))
                f.write(' ')
            f.write('\n')
            f.write('\n')

