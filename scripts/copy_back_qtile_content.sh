#!/bin/bash

repo_root=$(git rev-parse --show-toplevel)
qtile_dir=~/.config/qtile

while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
        echo "This script copies the qtile content from '$qtile_dir' into '$repo_root'."
        exit 0
        ;;
    *)
        echo "Only -h|--help or ZERO arguments supported!"
        exit 1
        ;;
  esac
done

### Copy qtile configuration, scripts and wallpapers back to dotfiles repo
cp $qtile_dir/config.py $repo_root/.config/qtile/
cp $qtile_dir/colors.py $repo_root/.config/qtile/
cp $qtile_dir/wallpapers/* $repo_root/.config/qtile/wallpapers/
cp $qtile_dir/scripts/* $repo_root/.config/qtile/scripts/
cp $qtile_dir/icons/* $repo_root/.config/qtile/icons/
