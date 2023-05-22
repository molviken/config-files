alias yocto="cd /home/molviken/Documents/xcharge/clu-linux-mk3; source poky/oe-init-build-env"
alias yoctorole="terminator -r yocto_term -l yocto_layout -p hold"

alias bitbake="mv ~/.pyenv/ ~/pythondrit; pyenv global system; bitbake"
alias conan="mv ~/pythondrit ~/.pyenv/; pyenv global 3.10.0; conan"

alias apti="sudo apt-get install"

alias defavpn="/home/molviken/scripts/defa.exp"
alias fixmylife="/home/molviken/bin/set_up_workspaces.sh"

alias cleanbuild="cd ..; rm -rf build; mkdir build; cd build"
alias cb="cleanbuild"

alias appbun="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/mf-application-bundle"
alias util="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/utility-library/build"
alias csc="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/charging-station-controller/build"
alias zyre="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/zyre-messaging/build"
alias nfc="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/nfc-transceiver/build"
alias mlib="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/messaging-library/build"
alias events="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/events/build"
alias diag="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/diagnostics/build"
alias fake="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/fake-commands"
alias pers="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/persistentstorage/build"
alias prot="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/protobuf-library/build"
alias wst="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/websocket-transceiver/build"
alias codeall="(cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/ && code .)"
alias nrfbtc="cd /home/molviken/Documents/xcharge/manifest/btc/build"
alias evse="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/evse-controller/build"
alias clib="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/chargecontroller_lib/build"
alias btc="cd /home/molviken/Documents/xcharge/APP_BUNDLE_CX/btc/build"
alias cdsimu="cd /home/molviken/Documents/xcharge/linux-apps_1/simu_cmd/build"

# CONAN aliases
alias cor="conan remove '*' -f"
alias coi="conan install .. --profile=linux_x86_64_gcc11"
alias coid="conan install .. --profile=linux_x86_64_gcc11 -s build_type=Debug"
alias coib="conan install .. --build=missing --profile=linux_x86_64_gcc11"
alias coit="conan install .. --profile=mf-honister-cross"
alias coitb="conan install .. --build=missing --profile=mf-honister-cross"
alias coim="conan install .. --profile:host=mf-honister-cross --profile:build=linux_x86_64_gcc11"
alias coimd="conan install .. --profile:host=mf-honister-cross --profile:build=linux_x86_64_gcc11 -s build_type=Debug"
alias coimb="conan install .. --build=missing --profile:host=mf-honister-cross --profile:build=linux_x86_64_gcc11"
alias coimold="conan install .. --profile:host=x86_64_to_aarch64-poky-linux --profile:build=linux_x86_64_gcc9"
alias cob="conan build .."
alias coe="conan export-pkg --force --ignore-dirty .. defa/stable"
alias cop="conan package .."
alias rbm="cb; coim; cob; coe;"
alias rbt="cb; coit; cob; coe;"
alias rb="cb; coi; cob; coe;"

alias oba="gedit ~/.bashrc"
alias ola='gedit ~/.bash_aliases'
alias logic="/home/molviken/Downloads/Logic-2.3.10-master.AppImage"
alias soyo="source /opt/millennium-falcon-fb/5.4-honister/environment-setup-cortexa53-crypto-poky-linux"
alias soba="source ~/.bashrc"
alias soze="source ~/Documents/xcharge/btc-firmware/include/zephyr/zephyr-env.sh"

# BITBAKE/YOCTO aliases
alias cdapp="cd ~/Documents/xcharge/clu-linux-mk3/meta-mk3/recipes-millennium-falcon/application-bundle/"
alias bbapp="bitbake application-bundle"
alias bbcapp="bitbake -f -c cleanall application-bundle"
alias bbc="bitbake -f -c cleanall"
alias bbccomps="bitbake -f -c cleanall btc-daemon charging-station-controller diagnostics display-backlight-controller display-composer evse-controller firmware-update-notifier mid-proxy nfc-transceiver nrf-fw-upg-tool persistent-storage websocket-transceiver zyre-messaging data-collector"
alias bbclibs="bitbake -f -c cleanall messaging-library protobuf-library"
alias bbpm="bitbake power-meter-daemon"
#alias bbfull="bitbake clu-base-image partition-image imx-boot"
alias bbfull="bitbake imx-boot defa-power-image partition-image"
alias bbfull2="bbfull"

#alias bbflash="sudo uuu  -b ${BBPATH}/../meta-mk3/conf/emmc_burn_and_resize.lst ${BBPATH}/tmp/deploy/images/millennium-falcon/imx-boot  ${BBPATH}/tmp/deploy/images/millennium-falcon/clu-base-#image-millennium-falcon.wic.bz2 ${BBPATH}/tmp/deploy/images/millennium-falcon/Image ${BBPATH}/tmp/deploy/images/millennium-falcon/imx8mn-millennium-falcon-rev-a.dtb ${BBPATH}/tmp/deploy/images/#millennium-falcon/partition-image &&  sudo uuu  -b ${BBPATH}/../meta-mk3/conf/wait-for-reboot.lst"

alias bbflash="uuu  -b ${BBPATH}/../meta-mk3/conf/emmc_burn_and_resize.lst ${BBPATH}/tmp/deploy/images/millennium-falcon/imx-boot  ${BBPATH}/tmp/deploy/images/millennium-falcon/defa-power-image-millennium-falcon.wic.zst ${BBPATH}/tmp/deploy/images/millennium-falcon/Image ${BBPATH}/tmp/deploy/images/millennium-falcon/imx8mn-millennium-falcon-rev-a.dtb ${BBPATH}/tmp/deploy/images/millennium-falcon/partition-image && uuu  -b ${BBPATH}/../meta-mk3/conf/wait-for-reboot.lst"
alias bbflash2="uuu  -b ${BBPATH}/../meta-mk3/conf/emmc_burn_and_resize.lst ${BBPATH}/tmp/deploy/images/millennium-falcon/imx-boot  ${BBPATH}/tmp/deploy/images/millennium-falcon/defa-power-image-millennium-falcon.wic.bz2 ${BBPATH}/tmp/deploy/images/millennium-falcon/Image ${BBPATH}/tmp/deploy/images/millennium-falcon/imx8mn-millennium-falcon-rev-a.dtb ${BBPATH}/tmp/deploy/images/millennium-falcon/partition-image && uuu  -b ${BBPATH}/../meta-mk3/conf/wait-for-reboot.lst"

alias bbflashlocal="uuu -b emmc_burn_and_resize.lst imx-boot defa-power-image-millennium-falcon.wic.zst Image imx8mn-millennium-falcon-rev-a.dtb partition-image && uuu -b wait-for-reboot.lst"

alias scpall="scpccu ${BBPATH}/../meta-mk3/conf/emmc_burn_and_resize.lst ${BBPATH}/tmp/deploy/images/millennium-falcon/imx-boot ${BBPATH}/tmp/deploy/images/millennium-falcon/defa-power-image-millennium-falcon.wic.bz2 ${BBPATH}/tmp/deploy/images/millennium-falcon/Image ${BBPATH}/tmp/deploy/images/millennium-falcon/imx8mn-millennium-falcon-rev-c.dtb ${BBPATH}/tmp/deploy/images/millennium-falcon/partition-image ${BBPATH}/../meta-mk3/conf/wait-for-reboot.lst lab:/home/mf-user/bughunt-molvik/ccu_image/"

alias scpall2="scpccu emmc_burn_and_resize.lst imx-boot defa-power-image-millennium-falcon.wic.bz2 Image imx8mn-millennium-falcon-rev-c.dtb partition-image wait-for-reboot.lst lab:/home/mf-user/bughunt-molvik/ccu_image/"

alias scprauc="scp /home/molviken/Documents/xcharge/clu-linux-mk3/build/tmp/deploy/images/millennium-falcon/update-bundle-millennium-falcon.raucb ccu:/home/root/"

alias bbrf="uuu -b emmc_burn_and_resize.lst imx-boot clu-base-image-millennium-falcon.wic.bz2 Image imx8mn-millennium-falcon-rev-a.dtb partition-image && uuu -b wait-for-reboot.lst"
alias bbbundle="bitbake update-bundle"
alias cpbundle="scpccu tmp/deploy/images/millennium-falcon/update-bundle-millennium-falcon.raucb"

# PICOCOM aliases
alias picoccu="picocom -b 115200 /dev/ttyUSB0 -d 8 -p 1"
alias piconrf="picocom -b 115200 /dev/ttyACM0 -d 8 -p 1"
alias piconrf1="picocom -b 115200 /dev/ttyACM1 -d 8 -p 1"

alias memcheck='ctest --overwrite MemoryCheckCommandOptions="--leak-check=full --show-leak-kinds=all" -T memcheck'

alias scpccu="scp -i ~/.ssh/mk3_rsa"
alias sshccu="ssh -i ~/.ssh/mk3_rsa"
alias sshvault="ssh -i ~/Downloads/mf-id_rsa-cert.pub -i ~/Download/mf-id_rsa.pub"
alias scpevse="scp ~/Documents/xcharge/APP_BUNDLE_CX/evse-controller/build/bin/evse-controller ccu:/appbundle/usr/bin/"
alias scpsimu="scp ~/Documents/xcharge/linux-apps_1/simu_cmd/build/bin/simulator ccu:/appbundle/usr/bin/"
alias scpprot="scp ~/Documents/xcharge/APP_BUNDLE_CX/protobuf-library/build/lib/* ccu:/appbundle/usr/lib/"

alias scpmerged="scp ~/Documents/xcharge/btc-firmware/build/zephyr/merged.hex lab:/home/mf-user/bughunt-molvik/"
alias scpblinky="scp ~/Documents/xcharge/blinky_mod/build/zephyr/merged.hex lab:/home/mf-user/bughunt-molvik/"
alias sshconf="gedit ~/.ssh/config"

alias oca="code ../conanfile.py"

alias cmds="gedit ~/Documents/xcharge/management_console_commands.txt"

# GIT aliases
alias gitamend="git add -A; git commit --amend --no-edit"
alias gs="git status"
alias gc="git commit"
alias gcm="git commit -m"
alias gps="git push"
alias gck="git checkout"
alias gckd="git checkout develop"
alias gl="git log"
alias gd="git diff"
alias gds="git diff --staged"
alias gbdel="git branch -d"
alias gbDEL="git branch -D"
alias gba="git branch -a"
alias gbl="git branch -l"
alias gbr="git branch -r"
alias gfp="git fetch --prune"
alias gp="git pull"
alias gbdlocal="git fetch -p ; git branch -r | awk '{print $1}' | egrep -v -f /dev/fd/0 <(git branch -vv | grep origin) | awk '{print $1}' | xargs git branch -d"

alias getperf="~/scripts/getPerf.sh"
alias cleanips="~/scripts/clean_known_hosts.sh"
alias getpw="echo 'K65das88\$5' | xclip -selection clipboard"
alias checkjira="cat /etc/resolv.conf"
alias fixjira="sudo echo 'nameserver 172.24.2.2' | cat - /etc/resolv.conf > temp && sudo mv temp /etc/resolv.conf && sudo service resolvconf restart && checkjira"
alias revertjira="sudo echo '$(tail -n +2 /etc/resolv.conf)' > /etc/resolv.conf && sudo service resolvconf restart && checkjira"

alias qlog="cat ~/.local/share/qtile/qtile.log"

