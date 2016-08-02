try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

req_list = ['sqlalchemy']

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='orm-creator',

    packages=['orm_creator'],

    version='1.0.0',

    description='Automatically maps sql tables'
    ' and generates classes for ORM manipulation',

    author='Shravan Murali',

    author_email='shravanmurali@gmail.com',

    install_requires=req_list,

    entry_points={
        'console_scripts': ['orm-creator = orm_creator:'
                            'main']
    },

    url='https://github.com/shravan97/ORM-Creator',

    keywords=['sqlalchemy', 'automate', 'ORM', 'MySql'],

    classifiers=['Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Education'],

    license='MIT License'
)
