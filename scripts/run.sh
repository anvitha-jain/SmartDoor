!/bin/sh
aws s3 cp s3://smartdoor-logo1/index.html /var/www/html/index.html
service httpd restart
