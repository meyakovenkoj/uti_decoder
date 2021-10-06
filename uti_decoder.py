import argparse
import sys

vector = "abcdefghkmnpqrstuvwxyz0123456789"


def parse_arguments(parser):
    parser.add_argument('-d', '--decode', help='decode UTI file type',
                        required=False, dest='uti_type', type=str, default='')
    parser.add_argument('-e', '--encode', help='encode UTI file type',
                        required=False, dest='mime_type', type=str, default='')
    return parser.parse_args()


def base32decode(char):
    pos = vector.find(char)
    if pos == -1:
        print("Invaild char in base32 string")
        exit(1)
    res = str("{0:b}".format(pos)).zfill(5)
    return res


def base32encode(bitstr):
    pos = int(bitstr, 2)
    if pos < 0 or pos > 31:
        print("Invaild char in base32 string")
        exit(1)
    res = vector[pos]
    return res


def decode(string):
    clear_str = string[5:]
    bindata = ''
    res = ''
    for each in clear_str:
        bindata += base32decode(each)
    for i in range(0, len(bindata), 8):
        res += chr(int(bindata[i:i+8], 2))
    return res


def encode(string):
    addition = "dyn.a"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert UTI file type to MIME vice versa', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parse_arguments(parser)
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.uti_type == '' and args.mime_type != '':
        encode(args.mime_type)
    elif args.uti_type != '' and args.mime_type == '':
        print(decode(args.uti_type))
    else:
        print("Can't do both at the same time")
        parser.print_help(sys.stderr)
        sys.exit(1)
