#!/usr/bin/env python3

#############################################
## main menu of the instantOS settings app ##
#############################################

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
import pathlib
import subprocess
import webbrowser

# won't show icons otherwise
settings = Gtk.Settings.get_default()
settings.props.gtk_button_images = True


class Handler:
    def mainwindow_destroy_cb(self, *args):
        Gtk.main_quit()

    def displaybutton_clicked_cb(self, button):
        popover = builder.get_object('displaypopover')
        popover.popup()

    def mousebutton_clicked_cb(self, button):
        mousewin = builder.get_object('mousewindow')
        mousewin.show_all()

    def mousecancel_clicked_cb(self, button):
        builder.get_object('mousewindow').destroy()

    def networkbutton_clicked_cb(self, button):
        popover = builder.get_object('networkpopover')
        popover.popup()

    def appearancebutton_clicked_cb(self, button):
        subprocess.Popen(["lxappearance"])

    def displaychange_clicked_cb(self, button):
        subprocess.Popen(['arandr'])


builder = Gtk.Builder()

if pathlib.Path('./mainsettings.glade').exists():
    builder.add_from_file("./mainsettings.glade")
else:
    builder.add_from_file("/usr/share/instantsettings/mainsettings.glade")

builder.connect_signals(Handler())

window = builder.get_object('mainwindow')
window.show_all()

Gtk.main()
