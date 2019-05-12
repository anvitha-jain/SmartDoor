!/bin/sh
aws s3 cp s3://doorwatch-bucket-smart/index.html /var/www/html/index.html
service httpd restart
