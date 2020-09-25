
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
Step 7 : Install WordPress

This file and the httpd.conf file are 
available on github:

https://githib.com/semirworkuaman/termux-demos/termux-wordpress

Thank You for watching 

/data/data/com.termux/files/usr/etc/apache2
nano httpd.conf
Listen {{port}}
DocumentRoot "/sdcard/htdocs"
<Directory "/sdcard/htdocs">
...
 </Directory>
LoadModule php7_module libexec/apache2/libphp7.so


<IfModule mod_dir.c>
DirectoryIndex index.php index.html index.cgi index>

</IfModule>

<FilesMatch ".+\.ph(p[345]?|t|tml)$">
    SetHandler application/x-httpd-php
</FilesMatch>

mysqld_safe --skip-grant-tables&
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'pass';


wget https://wordpress.org/latest.tar.gz
