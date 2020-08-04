# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# open up the config for our file
Vagrant.configure("2") do |config| # wrapper required for all vagrant files
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/xenial64"

 # network configuration
 # out computer == host; create a guest os
  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8080, host: 8080

# provisioning script
# runs on the server the first time you start it
# sets up server to support application
  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade the server packages.
    sudo apt-get update
    sudo apt-get -y upgrade
    # Set Ubuntu Language
    sudo locale-gen en_GB.UTF-8
    # Install Python, SQLite and pip
    sudo apt-get install -y python3-dev sqlite python-pip
    # Upgrade pip to the latest version.
    sudo pip install --upgrade pip
    # Install and configure python virtualenvwrapper.
    sudo pip install virtualenvwrapper
    if ! grep -q VIRTUALENV_ALREADY_ADDED /home/vagrant/.bashrc; then
        echo "# VIRTUALENV_ALREADY_ADDED" >> /home/vagrant/.bashrc
        echo "WORKON_HOME=~/.virtualenvs" >> /home/vagrant/.bashrc
        echo "PROJECT_HOME=/vagrant" >> /home/vagrant/.bashrc
        echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
    fi
  SHELL

end
