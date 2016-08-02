from sqlalchemy import *
from sqlalchemy.orm import *
import sys
import os
import re


class OrmCreator(object):
    """
    Class to map the given list of tables ,
    in the given database and write it 
    onto the given file  

    """

    def __init__(self, config, db, tables='*', out='db.py'):
        self.config = config
        self.db = db
        self.tables = tables
        self.outfile = out
        self.sqla_engine = create_engine('mysql://' + config['username'] +
                                         ':' + config['password'] +
                                         '@' + config['host'] + 
                                         '/' + db)

    def fetch_tables(self):
        """
        Function to fetch the details of all tables 
        effectively as a dictionary of lists

        """
        session = scoped_session(sessionmaker(bind=self.sqla_engine))
        curr_session = session()
        mdata = MetaData()
        mdata.reflect(self.sqla_engine)
        if self.tables == '*':
            tables_list = mdata.tables.keys()
        else:
            tables_list = self.tables

        tables = {}

        for table in tables_list:
            desc = curr_session.execute("DESCRIBE " + table).fetchall()
            tables[table] = desc

        return tables

    def generate_file(self):
        """
        Function to generate/update the required file 

        """

        tables = self.fetch_tables()  # Fetch all table info from DB

        # Check if the file exists
        try:
            file = open(self.outfile, 'rw+')
        except:
            # Open a file in writing mode to create it first
            file = open(self.outfile, 'w+')
            file.close()
            file = open(self.outfile, 'rw+')

        file.seek(os.stat(file.name).st_size)  # Seek the end of file

        if os.stat(file.name).st_size is not 0:
            file.write('\n')

        file.write('from sqlalchemy import *\n')
        file.write('from sqlalchemy.orm import *\n')
        file.write('from sqlalchemy.dialects.mysql import *\n')
        file.write('from sqlalchemy.ext.declarative import declarative_base \n\n')
        file.write('base = declarative_base()\n')
        # file.close() # File has to be closed frequently for the file size to
        # get updated

        # file=open(self.outfile , 'rw+')

        for table in tables:
            # file.seek(os.stat(file.name).st_size)
            file.write('\n')
            file.write('class ' + table + '(base):\n')
            file.write('    __tablename__ = \"' + table + '\"\n')

            for attr in tables[table]:
                file.write('    ' + attr[0] + ' = Column(\'' + attr[0] + '\'')

                # Finding out the datatype
                datatypes = ['int', 'varchar', 'timestamp', 'text',
                             'bigint', 'mediumint', 'smallint',
                             'tinyint', 'decimal', 'float', 'datetime',
                             'enum', 'tinytext', 'mediumtext',
                             'longtext', 'date']

                # Loop through each datatype and check if any of those matches
                for dtype in datatypes:
                    if re.match(dtype, attr[1]) is not None:
                        file.write(',' + str.upper(dtype) + '(')

                        if dtype in ['text', 'timestamp', 'datetime',
                                     'tinytext', 'mediumtext',
                                     'longtext', 'date', 'float',
                                     'bigint', 'int']:
                            file.write(')')
                        elif dtype == 'enum':
                            file.write(re.split('[()]', attr[1])[1] + ')')
                        else:
                            file.write(re.findall('[0-9]+', attr[1])[0] + ')')
                        break

                if attr[2] == 'NO':
                    file.write(', nullable=False')

                if attr[3] == 'PRI':
                    file.write(', primary_key=True')
                elif attr[3] == 'UNI':
                    file.write(', unique=True')

                file.write(')\n')
        file.close()
