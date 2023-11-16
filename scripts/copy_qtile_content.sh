#!/bin/bash

while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
        echo "This script copies the qtile content from current dotfiles repository into ~/.config/qtile/"
        exit 0
        ;;
    *)
        echo "Only -h|--help or ZERO arguments supported!"
        exit 1
        ;;
  esac
done

### Copy qtile configuration, scripts and wallpapers
repo_root=$(git rev-parse --show-toplevel)
repo_config=$repo_root/.config
repo_config_qtile=$repo_config/qtile
repo_config_qtile_wallpapers=$repo_config_qtile/wallpapers
repo_config_qtile_scripts=$repo_config_qtile/scripts
repo_config_qtile_icons=$repo_config_qtile/icons

config=~/.config
config_qtile=$config/qtile

cp $repo_config_qtile/config.py $config_qtile/
cp $repo_config_qtile/colors.py $config_qtile/
cp $repo_config_qtile_wallpapers/* $config_qtile/
cp $repo_config_qtile_scripts/* $config_qtile/
cp $repo_config_qtile_icons/* $config_qtile/
