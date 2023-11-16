#!/bin/bash

if [ $? -eq 1 ]; then
    echo "Missing argument, exiting..."
    exit 1
fi

function set_display_output {
    setting=$1

    monitors=($(xrandr | grep " connected " | awk '{ print$1 }'))
    num_monitors_detected=${#monitors[@]}

    if [[ num_monitors_detected -eq 1 ]]; then
        echo "Only internal monitor detected, exiting..."
        xrandr --output ${monitors[0]} --primary --auto
        exit 0
    fi

    case $setting in
    "display_external")
    echo "external"
    xrandr --output ${monitors[1]} --primary --auto --output ${monitors[0]} --off
    ;;
    "display_internal")
    xrandr --output ${monitors[0]} --primary --auto --output ${monitors[1]} --off
    echo "internal"
    ;;
    "display_dual")
    xrandr --output ${monitors[1]} --primary --auto --output ${monitors[0]} --auto
    echo "dual"
    ;;
    *)
    zenity --info --text="In ${FUNCNAME[0]}, unknown command: $cmd"
    ;;
    esac
}

function spotify_control {
    cmd=$1

    case $cmd in
    "spotify_next")
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next
    ;;
    "spotify_prev")
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous
    ;;
    "spotify_pause_play")
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause
    ;;
    *)
    zenity --info --text="In ${FUNCNAME[0]}, unknown command: $cmd"
    ;;
    esac
}

######## Main switch case for commands #########
echo "cmd: $1"
case $1 in
    "config")
    code ~/.config/qtile/config.py
    ;;
    "display_"*)
    set_display_output $1
    ;;
    "spotify_"*)
    spotify_control $1
    ;;
    "lock")
    picture_path=$2
    -i ${picture_path}default_lockscreen.png
    ;;
    *)
    zenity --info --text="In ${FUNCNAME[0]}, unknown command: $cmd"
    ;;
esac
