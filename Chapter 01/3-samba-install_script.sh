# Install Samba file sharing service
sudo apt-get install samba samba-common-bin
sudo smbpasswd -a odoo

# Edit the configuration
# sudo nano /etc/samba/smb.conf  # if you prefer manually
sudo cp smb.conf /etc/samba/smb.conf  # if you prefer to use our conf file

# Restart the Samba service to relod the config
sudo /etc/init.d/smbd restart
