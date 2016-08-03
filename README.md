# ORM - Creator

### Description
Map SQL (MySQl) table(s) and generate ORM classes for them automatically !!  
This proves to be very useful especially in cases where the number of tables is huge 

### Demo
##### From command line
![cli_demo](https://cloud.githubusercontent.com/assets/10980285/17341384/f58637a4-5911-11e6-9309-deb9c4ae3dd8.gif)  

##### As a python module 
![module_demo](https://cloud.githubusercontent.com/assets/10980285/17342191/a87677f4-5915-11e6-8cd1-7060eead65b3.gif)

### Installation
##### Using this repository 
```sh
git clone http://github.com/shravan97/ORM-Creator

```  

```sh
cd ORM-Creator

```  

```sh
python setup.py install

```  
##### Using pip

```sh
pip install orm-creator

```  


### Usage
```sh

usage: orm-creator [-h] [-db DB] [-t TABLES [TABLES ...]] [-host HOST]
                   [-u UNAME] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -db DB                The name of database from which tables will have to
                        mapped
  -t TABLES [TABLES ...]
                        List of table names each separated by one or more
                        space
  -host HOST            Name of the MySql host For Eg., localhost ,
                        mysql.mydomain.com ,....etc
  -u UNAME              Your Mysql username
  -o OUTFILE            Output file name ,along with its extension and
                        absolute path For Eg. , /home/shravan97/Desktop/out.py  

```  

### Sample
##### As a command line app
```sh
orm-creator -u root -db demo -t users migrations -o /var/www/flaskApp/db.py

# The above statement maps `users` and `migrations` tables  

```  

##### As a module
```python

from orm_creator import ormCreator
oc = ormCreator(config,'demo',['users','migrations'],'/var/www/flaskApp/db.py')

# config is stored as a dict . For eg. , config = {'uname':'root','password':'**','host':'localhost'}

oc.generate_file()

```  

Please check [here](https://github.com/shravan97/ORM-Creator/tree/master/demo/) for demo files  


### Contributions
Found any cool idea that could be implemented here ? Go ahead and give a pull request :smile: !  
You may as well put it up as an issue [here](https://github.com/ORM-Creator/issues)  

### Contributors
- [shravan97](https://github.com/shravan97)

### License 
GNU General Public License v3 (GPLv3)  

![gpl](https://cloud.githubusercontent.com/assets/10980285/16361582/a40f472a-3bb2-11e6-80c4-dd633af6c284.png) 