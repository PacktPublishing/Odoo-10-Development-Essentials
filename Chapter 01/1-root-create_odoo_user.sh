# If running plain Debian, a new system has only root
# We need to create an Odoo user to work with:

apt-get update && apt-get upgrade # Install system updates
apt-get install sudo # Make sure 'sudo' is installed

useradd -m -g sudo -s /bin/bash odoo  # Create an 'odoo' user with sudo powers
passwd odoo  # Ask and set a password for the new user