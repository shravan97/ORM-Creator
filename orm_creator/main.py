from argparse import ArgumentParser as ap
from ormCreator import OrmCreator
import sys
import getpass


def arg_parser():
    parser = ap()

    parser.add_argument('-db',
                        dest='db',
                        help='The name of database'
                        ' from which tables will'
                        ' have to mapped ')

    parser.add_argument('-t',
                        dest='tables',
                        nargs='+',
                        help='List of table names '
                        'each separated by one or '
                        'more space')

    parser.add_argument('-host',
                        dest="host",
                        help="Name of the MySql host\n"
                        " For Eg., localhost , "
                        "mysql.mydomain.com ,....etc")

    parser.add_argument('-u',
                        dest="uname",
                        help="Your Mysql username")

    parser.add_argument('-o',
                        dest="outfile",
                        help="Output file name ,"
                        "along with its extension and "
                        "absolute path\n For Eg. , /home"
                        "/shravan97/Desktop/out.py")

    args = parser.parse_args()

    if args.uname is None:
        print "Please enter"\
            " your MySql username"
        sys.exit(0)
    elif args.db is None:
        print "Please enter"\
            " the required database name"
        sys.exit(0)
    elif args.host is None:
        print "Please enter in the "\
            " MySql host"
        sys.exit(0)
    else:
        values = {}
        values['uname'] = args.uname
        values['db'] = args.db
        values['host'] = args.host

        if args.tables is None:
            values['tables'] = '*'
        else:
            values['tables'] = args.tables

        if args.outfile is None:
            values['out'] = 'db.py'
        else:
            values['out'] = args.outfile

        return values


def main():
    options = arg_parser()
    pwd = getpass.getpass("Your "
                          " MySql Password : ")

    config = {}
    config['password'] = pwd
    config['username'] = options['uname']
    config['host'] = options['host']

    orm = OrmCreator(config, options['db'],
                     options['tables'], options['out'])
    orm.generate_file()

if __name__ == "__main__":
    main()
