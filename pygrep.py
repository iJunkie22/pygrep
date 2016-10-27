#!/opt/local/bin/python2.7
import colorama
import sys
import re

colorama.init()

USAGE = """USAGE:
pygrep [options] pattern

options can be --color, --color=BLUE, etc
"""


def print_usage(iserror=True):
    sys.stderr.write(USAGE)
    exit(int(iserror))

ARGV_LEN = len(sys.argv)

if ARGV_LEN == 1:
    print_usage()

elif ARGV_LEN == 2:
    pat = re.compile(sys.argv[1])
    for line in sys.stdin:
        m = pat.search(line)
        if m:
            sys.stdout.write(line)

elif ARGV_LEN == 3 and sys.argv[1].startswith('--color'):
    flag, sep, fval = sys.argv[1].partition('=')
    if sep == '=':
        try:
            fval = fval.upper()
            hcolor = object.__getattribute__(colorama.Fore, fval)
        except AttributeError:
            hcolor = colorama.Fore.BLUE
    else:
        hcolor = colorama.Fore.BLUE

    pat = re.compile(sys.argv[2])
    for line in sys.stdin:
        ms = pat.split(line)
        if len(ms) > 1:
            res = ''
            for m in ms:
                if not m:
                    m = ''
                if pat.match(m):
                    res += hcolor
                else:
                    res += colorama.Fore.RESET
                res += m
            res += colorama.Fore.RESET
            sys.stdout.write(res)

else:
    print_usage()
