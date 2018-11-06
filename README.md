# Discharge Rate Indicator

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://www.python.org/) 
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/armsp/disradicator/issues) 
[![platform](https://img.shields.io/badge/platform-linux64-lightgrey.svg)] 
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/armsp/disradicator/graphs/commit-activity) 
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 



Welcome to the README of **Discharge Rate Indicator** for Ubuntu Unity desktop environment.  

This application indicator resides in the Applicaton/Top bar and displays the instantaneous power usage a.k.a discharge rate of the battery every 3 seconds. There is a visual indicator too that averages the instantaneous values for 5 measurements. 

#### Name
**dis-ra-dicator** : discharge-rate-indicator  
Has a dinosaury 🦖 vibe to it.....velociraptor, disradicator......maybe more of a Terminator vibe !  
Or, as pointed out by [Raghu](https://github.com/krishraghuram)  
**dis-radicator** : discharge-eradicator  
Which is also accurate as it keeps you aware of your discharge rate thereby helping you slow it down.

## Dependencies
[Needs citation]
* python3-gi
* python3-gi-cairo
* gir1.2-gtk-3.0
* gir1.2-appindicator3-0.1
* Not sure about these but might help-
  - gobject-introspection
  - libgtk-3-dev
  - libgirepository1.0-dev
  - python3-pyside

Resources to help after the above fails-
- [PyGObject Env Setup](https://pygobject.readthedocs.io/en/latest/devguide/dev_environ.html)  
- [PyGObject Quickstart](https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started)

## Usage
1. Clone the repository
2. Open a terminal inside the `src` folder
3. Execute the python script `start.py`
4. Watch the magic unfold on your Top/Activity bar, right-hand side most probably.

## Proof of Concept
![Appindicator](https://github.com/armsp/disradicator/blob/master/docs/movie.gif)
