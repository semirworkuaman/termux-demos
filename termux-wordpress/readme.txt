
Installing WordPress on Termux

Step 1 : Install apache2 php and
php-apache

Step 2 : Configure apache
- Set listening port
- Set DocumentRoot and Directory
- Load php module
- Set DirectoryIndex
- Set php file handler

Step 3 : Restart apache2 and test php

Step 4 : Install mariadb 

Step 5 : Reset root password
- Start mysqld in safe mode with skip
grant tables
- Connect to mysql and reset root 
password

Step 6 : Download and Extract WordPress
I have a wp already under /sdcard/htdocs/
wp-termux

Step 7 : Install WordPress

This file and the httpd.conf file are 
available on github:

https://github.com/semirworkuaman/termux-demos/termux-wordpress



