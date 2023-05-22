import os
import shutil
import subprocess

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from libqtile.core.manager import Qtile
from libqtile.backend.base import Window
from libqtile.group import _Group

# from colors import colors

mod = "mod4"
terminal = "terminator"
browser = "google-chrome"
qtile_script="/home/molviken/.local/bin/qtile_commands.sh "

home = os.path.expanduser("~")
config = f"{home}/.config"
scripts = f"{config}/qtile/scripts"

@lazy.function
def spawn_or_focus(qtile: Qtile, app: str) -> None:
    """Check if the app being launched is already running, if so focus it"""
    window = None
    for win in qtile.windows_map.values():
        if isinstance(win, Window):
            wm_class: list | None = win.get_wm_class()
            if wm_class is None or win.group is None:
                return
            if any(item.lower() in app for item in wm_class):
                window = win
                group = win.group
                group.cmd_toscreen()
                break
    if window is None:
        qtile.cmd_spawn(app)

    elif window == qtile.current_window:
        try:
            assert (
                qtile.current_layout.swap_main is not None
            ), "The current layout should have swap_main"
            qtile.current_layout.swap_main()
        except AttributeError:
            return
    else:
        qtile.current_group.focus(window)

@lazy.function
def spawn_or_focus_role(qtile: Qtile, app: str) -> None:
    """Check if the app being launched is already running, if so focus it"""
    window = None
    for win in qtile.windows_map.values():
        if isinstance(win, Window):
            wm_role: list | None = win.get_wm_role()
            if wm_role is None or win.group is None:
                continue
            if (app in wm_role):
                window = win
                group = win.group
                group.cmd_toscreen()
                break

    if window is None:
        qtile.cmd_spawn(qtile_script + app)

    elif window == qtile.current_window:
        try:
            assert (
                qtile.current_layout.swap_main is not None
            ), "The current layout should have swap_main"
            qtile.current_layout.swap_main()
        except AttributeError:
            return
    else:
        qtile.current_group.focus(window)

class PasSwitch(widget.TextBox):
    name = "PasSwitch"
    # def __init__(self, **config):
        # super().__init__("", **config)
        # My widget's initialisation code here
        # lazy.spawn("/home/molviken/scripts/switchmon.sh DP1")

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "f", lazy.spawn('nautilus'), desc="Open file manager"),
    Key([mod], "z", lazy.spawn(qtile_script + "CONFIG"), desc="Open config"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), lazy.layout.shrink_main(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), lazy.layout.grow_main(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(["mod1", "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn(f'rofi -show drun')),
    Key([mod], "q", lazy.spawn(f"{scripts}/power_menu.sh"), desc="Power menu"),

    # Be able to spawn a new browser window by force (mod + ctrl), or spawn or focus (mod)
    Key([mod], "b", spawn_or_focus(browser)),
    Key([mod, "control"], "b", lazy.spawn(browser)),

    Key([mod], "t", spawn_or_focus("teams"), spawn_or_focus("microsoft teams - preview")),
    Key([mod], "m", spawn_or_focus("spotify")),
    Key(['control', 'mod1'], "l", lazy.screen.next_group(skip_empty=False), desc="Switch to group to the right"),
    Key(['control', 'mod1'], "h", lazy.screen.prev_group(skip_empty=False), desc="Switch to group to the left"),
    Key(['control', 'mod1'], "c", lazy.spawn(f"{scripts}/clipboard_menu.sh"), desc="Copy cmds to clipboard"),

    # Key bindings relating to screen manipulation (xrandr)
    Key([mod, 'control'], "1", lazy.spawn(qtile_script + "DP1"), desc="Set DP-1 as primary and turn off eDP-1-1"),
    Key([mod, 'control'], "2", lazy.spawn(qtile_script + "eDP1"), desc="Set eDP-1-1 as primary and turn off DP-1"),
    Key([mod, 'control'], "3", lazy.spawn(qtile_script + "DUAL"), desc="Set DP-1 as primary and eDP-1-1 as non-primary"),
    #Key([mod, 'control'], "4", lazy.spawn("/home/molviken/scripts/qtile_commands.sh"), desc="Menu monitor"),

    # Key bindings for applications
    Key([mod], "KP_Begin", lazy.spawn(qtile_script + "toggle"), desc="Toggle play/pause spotify"),
    Key([mod], "KP_Right", lazy.spawn(qtile_script + "next"), desc="Next track spotify"),
    Key([mod], "KP_Left", lazy.spawn(qtile_script + "prev"), desc="Previous track spotify"),

    Key(["mod1", "shift"], "y", spawn_or_focus_role("yocto_term")),
    Key(["mod1", "shift"], "e", spawn_or_focus_role("evse_term")),
    Key(["mod1", "shift"], "p", spawn_or_focus_role("prot_term")),
]

groups = [
    Group("1", layout="bsp"),
    Group("2", layout="bsp", matches=[Match(role=["evse_term"])]),
    Group("3", layout="bsp", matches=[Match(role=["yocto_term"])]),
    Group("4", layout="bsp"),
    Group("5", layout="bsp", matches=[Match(wm_class=[browser])]),
    Group("6", layout="bsp", matches=[Match(wm_class=["Microsoft Teams - Preview"])]),
    Group("7", layout="bsp", matches=[Match(wm_class=["Spotify"])]),
]

for i, g in zip(["1", "2", "3", "4", "5", "6", "7"], groups):
    keys.append(Key(["mod1", "control"], i, lazy.group[g.name].toscreen(), desc=f"Switch to group {g.name}"))
    keys.append(Key([mod, "shift"], i, lazy.window.togroup(g.name, switch_group=True), desc=f"Switch to & move focused window to group {g.name}"))

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Spiral(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="/usr/share/backgrounds/hardy_wallpaper_uhd.png",
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.Sep(linewidth=5,),
                widget.GroupBox(),
                widget.Sep(linewidth=5,),
                widget.Prompt(),
                widget.Sep(linewidth=5,),
                widget.WindowName(),
                widget.Sep(linewidth=5,),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.PulseVolume(),
                widget.Sep(linewidth=5,),
                # widget.Mpris2(),
                widget.Sep(linewidth=5,),
                widget.Battery(
                    format="{char} {percent:2.0%}",
                ),
                widget.Sep(linewidth=5,),
                widget.CPU(
                    format="{load_percent}%",
                    update_interval=2,
                ),
                widget.Sep(linewidth=5,),
                widget.Memory(
                    format="{MemPercent}%",
                    update_interval=2,
                ),
                widget.Sep(linewidth=5,),
                PasSwitch(
                    "TOGGLE | Laptop",
                    mouse_callbacks={
                        "Button1": lazy.spawn("/home/molviken/scripts/toggle_audio_cards.sh toggle"),
                    },
                ),
                widget.Sep(linewidth=5,),
                widget.TextBox("default config", name="default"),
                widget.Sep(linewidth=5,),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Sep(linewidth=5,),
                widget.Systray(),
                widget.Sep(linewidth=5,),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Sep(linewidth=5,),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
