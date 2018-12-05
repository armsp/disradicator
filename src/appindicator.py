import os
from collections import deque

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator

# Globals
APPINDICATOR_ID = 'myappindicator'
DEQUE_LEN = 5
circular_buf = deque(maxlen=DEQUE_LEN)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def change_label(ind_app):
    '''Update the label text of the appindicator.
    Also updates the icon color based on the mean power.'''
    power = find_power()
    if power in ('Charging', 'Unknown', 'Full', 'Undefined'):
        ind_app.set_label(power, '8.8')
        if power == 'Charging':
            ind_app.set_icon(os.path.join(ROOT_DIR, 'icons/charging.svg'))
        return True
    else:
        circular_buf.append(power)
        mean_power = sum(circular_buf)/len(circular_buf)
        ind_app.set_label('{:.1f}'.format(power), '8.8')
        #print("Power Drain {:.1f}".format(power))
        if mean_power <= 4.5:
            ind_app.set_icon(os.path.join(ROOT_DIR, 'icons/microchip_green.svg'))
        elif 6 >= mean_power > 4.5:
            ind_app.set_icon(os.path.join(ROOT_DIR, 'icons/microchip_yellow.svg'))
        elif 9 >= mean_power > 6:
            ind_app.set_icon(os.path.join(ROOT_DIR, 'icons/microchip_orange.svg'))
        else:
            ind_app.set_icon(os.path.join(ROOT_DIR, 'icons/microchip_red.svg'))
        return True

# Quit menu
def quit(source):
    Gtk.main_quit()

def get_readings():
    '''Reads the status, current_now and voltage_now files for their values and returns a tuple containing all three'''
    try:
        with open('/sys/class/power_supply/BAT0/status', 'r') as status_file:
            charging_status = status_file.read()
    except EnvironmentError:
        charging_status = None
    else:
        try:
            with open('/sys/class/power_supply/BAT0/current_now', 'r') as current_file:
                current = current_file.read()
        except EnvironmentError:
            current = None
        try:
            with open('/sys/class/power_supply/BAT0/voltage_now', 'r') as voltage_file:
                voltage = voltage_file.read()
        except EnvironmentError:
            voltage = None

    if charging_status != None:
        return charging_status, current, voltage
    else:
        return None, None, None

def find_power():
    '''Gets the readings from "get_readings" function and calculates the power consumption in SI units'''
    status, I, V = get_readings()
    if status == None or I == None or V == None:
        return 'Undefined'
    elif status.strip() in ('Charging', 'Unknown', 'Full'):
        return status.strip()
    else:
        power = (int(I)/1000000)*(int(V)/1000000)
        return power

#Define the indicator app
ind_app = appindicator.Indicator.new(APPINDICATOR_ID, os.path.join(ROOT_DIR, 'icons/microchip.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
ind_app.set_status(appindicator.IndicatorStatus.ACTIVE)

# Create a menu
menu = Gtk.Menu()
menu_items = Gtk.MenuItem("Exit") #Add Exit to the menu
menu.append(menu_items)
menu_items.connect("activate", quit)
menu_items.show_all()
ind_app.set_menu(menu)
GLib.timeout_add(3000, change_label, ind_app) #Call change_label function every 3 seconds
Gtk.main()
