# Expression Engine:

### References:
 - https://www.youtube.com/watch?v=7sOcCssha_k&list=PL-rC5ii3XtN6iooGsUttWSoVm2SUyoMaM&index=7
 - https://www.linode.com/docs/guides/how-to-install-a-lamp-stack-on-ubuntu-18-04/
 - https://www.linode.com/docs/guides/how-to-install-and-configure-fastcgi-and-php-fpm-on-ubuntu-18-04/
 - https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
 - https://www.linuxbabe.com/ubuntu/install-lamp-stack-ubuntu-20-04-server-desktop
 - https://upcloud.com/community/tutorials/installing-lamp-stack-ubuntu/


## Before you begin:
1. VM on the correct network with latest Ubuntu image to install from vCloud DHCP doesn't usually work with the Linux VMs out of the box so I need a Static IP/Subnetmask & Default Gateway IP/Subnetmask Server name?
2. Domain to be connected to? if none given localhost will be used as a default. 
3. Linux User and Password??
4. SQL root password? (for security)
5. SQL user (for ExpressionEngine to use) and password?
6. SQL database name (for ExpressionEngine to use)?
7. ExpressionEngine Admin panel username and password?


## 1. Install Linux
```
Download and install latest Ubuntu 
Configure Networking (on vcloud it sometimes has issues with DHCP. Click on the Networking icon in the top right > Select Connector > Select Connector Settings > Click Gear next to Connector > IPv4 Tab > IPv4 Method: Manual > Set the IP address, subnet, the Gateway, and the DNS settings > click Apply)
Verify that Networking/DNS is working: 
ping -c 1 8.8.8.8
ping -c 1 google.com
if both pings are successful then you can move on. 

## update system:
sudo apt update && sudo apt upgrade -y && sudo apt install -y tasksel php-curl php-json php-cgi php-fpm php-zip git wget ufw htop curl 
sudo tasksel install lamp-server 
sudo apt install -y apache2-utils libapache2-mod-fcgidn
```

## 2. SETUP LAMP
## ufw: (firewall)
```
sudo ufw allow in "Apache Full"  
sudo ufw status
sudo ufw enable

optionally if needed:
sudo ufw allow ssh
sudo ufw allow ftp
```

## Apache: (web server)
```
systemctl status apache2
sudo systemctl start apache2
sudo systemctl enable apache2
systemctl status apache2
apache2 -v
browse to: localhost or 127.0.0.1

# edit: /etc/apache2/apache2.conf (default should be good)

KeepAlive On
MaxKeepAliveRequests 50
KeepAliveTimeout 5


# edit: /etc/apache2/mods-available/mpm_prefork.conf 

<IfModule mpm_prefork_module>
        StartServers            4
        MinSpareServers         3
        MaxSpareServers         40
        MaxRequestWorkers       200
        MaxConnectionsPerChild  10000
</IfModule>


Disable the event module and enable prefork:
sudo a2dismod mpm_event
sudo a2enmod mpm_prefork
sudo systemctl restart apache2
```

## MySQL: must be 5.6 or Higher
```
make mysql secure: 
sudo mysql_secure_installation
enter 2 for the strongest level, you will receive errors when attempting to set any password which does not contain numbers, upper and lowercase letters, and special characters, or which is based on common dictionary words.

Create First Database for Expression Engine to use:
sudo mysql 

CREATE DATABASE <database-name>;
CREATE USER '<user-name>'@'%' IDENTIFIED WITH mysql_native_password BY '<password>';
GRANT ALL ON <database-name>.* TO '<user-name>'@'%';

exit or quit
```

## FOR EXAMPLE:
```
sudo mysql 

CREATE DATABASE ee_database;
CREATE USER 'ee_user'@'%' IDENTIFIED WITH mysql_native_password BY 'Password1!';
GRANT ALL ON ee_database.* TO 'ee_user'@'%';

exit or quit
```

## Php: php 7 or newer required
```
php -v
edit: /etc/php/7.4/apache2/php.ini

error_reporting = E_COMPILE_ERROR | E_RECOVERABLE_ERROR | E_ERROR | E_CORE_ERROR
max_input_time = 30
error_log = /var/log/php/error.log

sudo mkdir /var/log/php
sudo chown www-data /var/log/php
sudo systemctl restart apache2
```

## php-fpm:
```
add the following lines to /etc/apache2/apache2.conf:

LoadModule proxy_module /usr/lib/apache2/modules/mod_proxy.so
LoadModule proxy_fcgi_module /usr/lib/apache2/modules/mod_proxy_fcgi.so


verify the php-fpm config:
sudo apache2ctl configtest
sudo systemctl restart apache2

congif appache to use fastCGI:
#sudo grep -E '^\s*listen\s*=\s*[a-zA-Z/]+' /etc/php/7.4/fpm/pool.d/www.conf
sudo grep 'listen = /run/php/php7' /etc/php/7.4/fpm/pool.d/www.conf
looking for: listen = /run/php/php7.4-fpm.sock

if not showing up: https://www.linode.com/docs/guides/how-to-install-and-configure-fastcgi-and-php-fpm-on-ubuntu-18-04/
test for config errors:
sudo apache2ctl configtest
sudo systemctl restart apache2


Edit: /etc/apache2/mods-available/fcgid.conf

<IfModule mod_fcgid.c>
  FcgidConnectTimeout 20
  AddType  application/x-httpd-php .php
  AddHandler application/x-httpd-php .php
  Alias /php7-fcgi /usr/lib/cgi-bin/php7-fcgi
  <IfModule mod_mime.c>
    AddHandler fcgid-script .fcgi
  </IfModule>
</IfModule>

sudo apache2ctl configtest
sudo systemctl restart apache2
```

## PHP TESTING:
```
testing: 
sudo nano /var/www/your_domain/info.php

<?php
phpinfo();

Navigate to your_domain/info.php to verify it works then remove it
sudo rm /var/www/your_domain/info.php


3. Test LAMP for server compatibility 
https://expressionengine.com/asset/file/ee_server_wizard.zip
unzip and move into /var/www/your_domain/
browse to it and run the test


4. Install Expresion Engine:
Create new database
https://www.youtube.com/watch?v=7sOcCssha_k&list=PL-rC5ii3XtN6iooGsUttWSoVm2SUyoMaM&index=7

Clone repo into your site's root directory or clone locally and upload files.
git clone https://github.com/ExpressionEngine/ExpressionEngine.git

add an empty config file: 
touch system/user/config/config.php

Verify file permissions: https://docs.expressionengine.com/latest/installation/installation.html#3-set-file-permissions
For Apache, that would be 666 for files and 777 for directories
setting all directories in system/ee to 777 and all files therein to 666, recursively:
find system/ee \( -type d -exec chmod 777 {} \; \) -o \( -type f -exec chmod 666 {} \; \)
find system/user \( -type d -exec chmod 777 {} \; \) 
find themes/user \( -type d -exec chmod 777 {} \; \) 
sudo chmod 666 system/user/config/config.php

route requests to the installer app instead of the main app by changing EE_INSTALL_MODE to TRUE in .env.php:
sudo nano /var/www/html/.env.php 
You can change this back when you're done.

Point your browser to /admin.php and run the Installation Wizard.
will need to know: 
Domain to be connected to? if none given localhost will be used as a default. 
SQL user (for ExpressionEngine to use) and password?
SQL database name (for ExpressionEngine to use)?
Table Prefix: exp (per Web Dev)
DO NOT "Install default theme" (per Web Dev)
ExpressionEngine Admin panel email, username, and password?
```

## SSL Setup: https://www.youtube.com/watch?v=Tka-0Tlr4N0
```
Get certs from company as a pfx file
https://www.ibm.com/docs/en/arl/9.7?topic=certification-extracting-certificate-keys-from-pfx-file
***NOTE this will require password to extract***

# Extracted encrypted key
openssl pkcs12 -in techready_wildcard.pfx -nocerts -out my.key

# Extract crt
openssl pkcs12 -in techready_wildcard.pfx -clcerts -nokeys -out my.crt

# Create unencrypted key 
openssl rsa -in my.key -out my-new.key


save files to:
/etc/ssl/certs/my.crt
/etc/ssl/private/my.key
/etc/ssl/private/my-new.key


copy the default config to make edits to it.
sudo cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/ExpressionEngine-ssl.conf

edit the config file:
sudo nano /etc/apache2/sites-available/ExpressionEngine-ssl.conf

look through the file and make the following changes. 

</VirtualHosts *:443>
DocumentRoot /var/www/html 					# (/var/www/website)
SSLEngine on 							# (must be on to for SSL to work)
SSLCertificateFile /etc/ssl/certs/my.crt  			# (/path/to/example_your_domain.crt)
SSLCertificateKeyFile /etc/ssl/private/my-new.key      		# (/path/to/your_private.key) if you use the encrypted key you will be asked for a password when restarting apache2
# SSLCertificateChainFile /path/to/CertificateAuthority.crt 	# (not needed) hashed to prevent feature from being used
# servername							# (not needed: domain) hashed to prevent feature from being used
</VirtualHosts>


# enable new SSL config
sudo a2ensite ExpressionEngine-ssl.conf

# disable default SSL config (not safe to use)
sudo a2dissite default-ssl.conf

# enable SSL Moodule 
sudo a2enmod ssl

# restart apache2
sudo systemctl restart apache2


Broswe to site to accept the SSL certificate:
https://127.0.0.1/index.php
click advanced and accept the cert

should now be able to browse the site in HTTPS
```


## HTACCESS redirect port 80 to 443:
```
https://www.freecodecamp.org/news/how-to-redirect-http-to-https-using-htaccess/

1. Redirect All Web Traffic
If you have existing code in your .htaccess, add the following:

RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]


2. Redirect Only a Specific Domain
For redirecting a specific domain to use HTTPS, add the following:

RewriteEngine On
RewriteCond %{HTTP_HOST} ^yourdomain\.com [NC]
RewriteCond %{SERVER_PORT} 80
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R,L]


3. Redirect Only a Specific Folder
Redirecting to HTTPS on a specific folder, add the following:

RewriteEngine On
RewriteCond %{SERVER_PORT} 80
RewriteCond %{REQUEST_URI} folder
RewriteRule ^(.*)$ https://www.yourdomain.com/folder/$1 [R,L]
```


































## Extra notes:
```
SQL: https://www.w3schools.com/sql/default.asp
check users:
SELECT user FROM mysql.user;

remove user:
DROP user <user-name>;

show databases:
SHOW DATABASES;

create a new database:
CREATE DATABASE <db-name>;

create user:
CREATE USER '<user-name>'@'%' IDENTIFIED WITH mysql_native_password BY '<password>';

grant access to db to user:
GRANT ALL ON <db-name>.* TO '<user-name>'@'%';

login as user:
mysql -u <user-name> -p
```
