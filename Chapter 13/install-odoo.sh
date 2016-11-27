


----------------
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install postgresql -y
sudo su -c "createuser -s $(whoami)" postgres

sudo apt-get install git python-pip python2.7-dev -y
sudo apt-get install libxml2-dev libxslt1-dev \
	libevent-dev libsasl2-dev libldap2-dev libpq-dev \
	libpng12-dev libjpeg-dev poppler-utils \
	node-less node-clean-css -y

wget http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb
sudo dpkg -i wkhtmltox-0.12.1.2_linux-jessie-amd64.deb
sudo apt-get -fy install 

wget https://raw.githubusercontent.com/odoo/odoo/9.0/requirements.txt
sudo -H pip install --upgrade pip
sudo -H pip install -r requirements.txt


-----------------

sudo adduser --disabled-password --gecos "Odoo" odoo
sudo su -c "createuser odoo" postgres
createdb --owner=odoo odoo-prod

sudo su odoo
git clone https://github.com/odoo/odoo.git /home/odoo/odoo-9.0 -b 9.0 --depth=1
~/odoo-master/odoo.py -d odoo-prod --save --stop-after-init
exit

------------------


sudo mkdir /etc/odoo
sudo cp /home/odoo/.openerp_serverrc /etc/odoo/openerp-server.conf
sudo chown -R odoo /etc/odoo

sudo mkdir /var/log/odoo
sudo chown odoo /var/log/odoo




/lib/systemd/system/odoo.service:

[Unit]
Description=Odoo
After=postgresql.service

[Service]
Type=simple
User=odoo
Group=odoo
ExecStart=/home/odoo/odoo-master/odoo.py -c /etc/odoo/openerp-server.conf

[Install]
WantedBy=multi-user.target

----
sysinit

$ sudo ln -s /home/odoo/odoo-10.0/odoo.py /usr/bin/odoo.py
$ sudo -h chown odoo /usr/bin/odoo.py



----
# sudo -u postgres createdb -O odoo odoo-project
4 As odoo, clone the project repository :
$ git clone https://github.com/login/project.git project
$ mkdir -p project/src
5 As the odoo user, clone the Odoo source code
$ cd project/src
$ git clone -b 9.0 https://github.com/odoo/odoo.git odoo-9.0
6 Create a virtualenv and install the dependencies
$ virtualenv ~/env-odoo-9.0
$ source ~/env-odoo-9.0/bin/activate
$ pip install -r odoo-9.0/requirements.txt
7 Clone all 3rd party addon repositories in the project/src subdirectory
$ git clone -b 9.0 https://github.com/OCA/partner-contact.git 
8 As root, uninstall gcc
# apt-get remove gcc

