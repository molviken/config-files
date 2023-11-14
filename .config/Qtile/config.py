import os
import subprocess

from libqtile.log_utils import logger
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from libqtile.core.manager import Qtile
from libqtile.backend.base import Window
from libqtile.group import _Group

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration

import colors

sup = "mod4" # super key
alt = "mod1" # alt key

terminal = "gnome-terminal"
browser = "brave"

home = os.path.expanduser("~")
config = f"{home}/.config"
scripts = f"{config}/qtile/scripts"

qtile_script=f"{scripts}/qtile_commands.sh "

@lazy.function
def spawn_or_focus(qtile: Qtile, app: str) -> None:
    """Check if the app being launched is already running, if so focus it"""
    window = None
    for win in qtile.windows_map.values():
        if isinstance(win, Window):
            wm_class: list | None = win.get_wm_class()
            if wm_class is None or win.group is None:
                return
            if any(item.lower() in app for item in wm_class) or any(app in item.lower() for item in wm_class): # Added OR part to catch ex. 'brave in Brave-browser'
                window = win
                group = win.group
                group.toscreen()
                break
    if window is None:
        qtile.spawn(app)

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
                group.toscreen()
                break

    if window is None:
        qtile.spawn(qtile_script + app)

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

keys = [
    # Switch between windows
    Key([sup], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([sup], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([sup], "j", lazy.layout.down(), desc="Move focus down"),
    Key([sup], "k", lazy.layout.up(), desc="Move focus up"),
    Key([sup], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([sup, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([sup, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([sup, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([sup, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([sup, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([sup, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([sup, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([sup, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([sup], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([sup], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([sup], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([sup], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([sup], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    Key([sup, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([sup, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    ############### My keybindings ##############
    Key([sup], "z", lazy.spawn(qtile_script + "config"), desc="Open config"),
    Key([sup], "f", lazy.spawn('nautilus'), desc="Open file manager"),
    Key([sup], "r", lazy.spawn(f'rofi -show drun')),

    # Layout flipping??
    Key([sup, alt], "j", lazy.layout.flip_down()),
    Key([sup, alt], "k", lazy.layout.flip_up()),
    Key([sup, alt], "h", lazy.layout.flip_left()),
    Key([sup, alt], "l", lazy.layout.flip_right()),
    Key([sup, "shift"], "space", lazy.layout.flip()),

    # Spotify control
    Key([sup], "KP_Begin", lazy.spawn(qtile_script + "spotify_pause_play"), desc="Toggle play/pause spotify"),
    Key([sup], "KP_Right", lazy.spawn(qtile_script + "spotify_next"), desc="Next track spotify"),
    Key([sup], "KP_Left", lazy.spawn(qtile_script + "spotify_prev"), desc="Previous track spotify"),

    # Navigate groups
    Key(['control', alt], "l", lazy.screen.next_group(skip_empty=False), desc="Switch to group to the right"),
    Key(['control', alt], "h", lazy.screen.prev_group(skip_empty=False), desc="Switch to group to the left"),
    Key(['control', alt], "c", lazy.spawn(f"{scripts}/clipboard_menu.sh"), desc="Copy cmds to clipboard"),

    # Open shit
    Key([sup], "m", spawn_or_focus("spotify")),
    Key([sup], "b", spawn_or_focus(browser)),
    Key([sup, "control"], "b", lazy.spawn(browser)),

    # Key bindings relating to screen manipulation (xrandr)
    Key([sup, 'control'], "1", lazy.spawn(qtile_script + "display_external"), desc="Set DP-1 as primary and turn off eDP-1-1"),
    Key([sup, 'control'], "2", lazy.spawn(qtile_script + "display_internal"), desc="Set eDP-1-1 as primary and turn off DP-1"),
    Key([sup, 'control'], "3", lazy.spawn(qtile_script + "display_dual"), desc="Set DP-1 as primary and eDP-1-1 as non-primary"),
]

groups = [
    Group("1", layout="bsp"),
    Group("2", layout="bsp"),
    Group("3", layout="bsp"),
    Group("4", layout="bsp"),
    Group("5", layout="bsp", matches=[Match(wm_class=["brave-browser"])]),
    Group("6", layout="bsp"),
    Group("7", layout="bsp", matches=[Match(wm_class=["Spotify"])]),
]

for i, g in zip(["1", "2", "3", "4", "5", "6", "7"], groups):
    keys.append(Key([sup], i, lazy.group[g.name].toscreen(), desc=f"Switch to group {g.name}"))
    keys.append(Key([sup, "shift"], i, lazy.window.togroup(g.name, switch_group=True), desc=f"Switch to & move focused window to group {g.name}"))

colors = colors.DoomOne

### LAYOUTS ###
layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[8],
                "border_normal": colors[0]
                }


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_theme),
    layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Spiral(),
]

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 12,
    padding = 0,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

powerline = {
    "decorations": [
        PowerLineDecoration()
    ]
}

def init_widgets_list():
    widgets_list = [
        widget.Image(
                 filename = "~/.config/qtile/icons/gnome-terminal.ico",
                 scale = "False",
                 mouse_callbacks = {'Button1': lazy.spawn(terminal)},
                 ),
        widget.GroupBox(
                background = "444444",
                fontsize = 14,
                margin_y = 3,
                margin_x = 4,
                padding_y = 2,
                padding_x = 3,
                borderwidth = 3,
                active = colors[8],
                inactive = colors[1],
                rounded = False,
                highlight_color = colors[2],
                highlight_method = "line",
                this_current_screen_border = colors[7],
                this_screen_border = colors [4],
                other_current_screen_border = colors[7],
                other_screen_border = colors[4],
                **powerline,
                ),
        widget.CurrentLayoutIcon(
                background = "222222",
                foreground = colors[5],
                padding = 5,
                scale = 0.7
                ),
        widget.CurrentLayout(
                background = "222222",
                foreground = colors[5],
                padding = 5,
                fontsize = 14,
                **powerline,
                ),
        widget.Spacer(background = "000000", length = 1200, **powerline),
        widget.WindowName(
                background="444444",
                foreground = colors[7],
                fontsize = 16,
                padding = 5,
                **powerline,
                max_chars=70,
                ),
        widget.CPU(
                format = '▓  Cpu: {load_percent}%',
                background="222222",
                foreground = colors[4],
                fontsize = 14,
                **powerline,
                ),
        widget.Memory(
                background = "000000",
                foreground = colors[8],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal

                + ' -e htop')},
                format = '{MemUsed: .0f}{mm}',
                fmt = '🖥  Mem: {} used',
                fontsize = 14,
                **powerline,
                ),
        widget.DF(
                background = "444444",
                padding = 4,
                update_interval = 60,
                foreground = colors[5],
                # mouse_callbacks = {'Button1': lazy.spawn(terminal
                # + ' -e df')},
                partition = '/',
                #format = '[{p}] {uf}{m} ({r:.0f}%)',
                format = '{uf}{m} free',
                fmt = '  Disk: {}',
                visible_on_warn = False,
                fontsize = 14,
                **powerline,
                ),
        widget.Volume(
                background = "222222",
                foreground = colors[7],
                fmt = '  Vol: {}',
                padding = 5,
                fontsize = 14,
                **powerline,
                ),
        widget.KeyboardLayout(
                background = "000000",
                configured_keyboards=['no'],
                foreground = colors[4],
                fmt = '⌨  Kbd: {}',
                fontsize = 14,
                padding = 2,
                **powerline,
                ),
        widget.Clock(
                padding = 2,
                background = "444444",
                foreground = colors[8],
                format = "⏱  %a, %b %d - %H:%M",
                fontsize = 14,
                **powerline
                ),
        widget.QuickExit(background="222222", foreground=colors[3], fontsize = 14, padding = 5, **powerline),
        ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:24]
    return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

# Drag floating layouts.
mouse = [
    Drag([sup], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([sup], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([sup], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
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

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
