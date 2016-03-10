#!/bin/bash
sudo service mysql start
mysql -uroot -e "CREATE USER 'mysql_user'@'localhost' IDENTIFIED BY 'Qa4kT2e4XC'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'mysql_user'@'localhost'"
mysql -uroot -e "FLUSH PRIVILEGES;"
mysql -umysql_user -pQa4kT2e4XC -e "create database django_ask"


python manage.py syncdb