#!/bin/bash

### Brave browser
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg

sudo apt update
sudo apt install -y rofi
sudo apt install -y zenity
sudo apt install -y python3-pip
sudo apt install -y brave-browser


### Install qtile-extras
# temp_dir="/tmp/"
# wget https://github.com/elParaguayo/qtile-extras/archive/refs/tags/v0.23.0.tar.gz -P $temp_dir
# cd $temp_dir
# tar -xf v0.23.0.tar.gz
# cd qtile-extras-0.23.0/

pip3 install xcffib
pip3 install qtile

qtile_cfg_dir="~/.config/qtile/"
scripts_dir="${qtile_cfg_dir}scripts/"
mkdir ${scripts_dir} && cp qtile_commands.sh ${scripts_dir} && cp default_wallpaper.jpg $qtile_cfg_dir
