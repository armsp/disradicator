# **Discharge Rate Indicator**

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://www.python.org/) 
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/armsp/disradicator/issues) 
[![platform](https://img.shields.io/badge/platform-linux64-lightgrey.svg)] 
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/armsp/disradicator/graphs/commit-activity) 
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
<!---[![wheel:yes](https://img.shields.io/pypi/wheel/requests.svg)]() --->
<!--- [![python](https://img.shields.io/pypi/pyversions/requests.svg)]()--->

Welcome to the README of **Discharge Rate Indicator** for Ubuntu Unity desktop environment.  

This application indicator resides in the Applicaton/Top bar and displays the instantaneous power usage a.k.a discharge rate of the battery every 3 seconds. There is a visual indicator too that averages the instantaneous values for 5 measurements. 

### Name
**dis-ra-dicator** : discharge-rate-indicator  
Has a dinosaury 🦖 vibe to it.....velociraptor, disradicator......maybe more of a Terminator vibe !  
Or, as pointed out by [Raghu](https://github.com/krishraghuram)  
**dis-radicator** : discharge-eradicator  
Which is also accurate as it keeps you aware of your discharge rate thereby helping you slow it down.

## Dependencies Installation
Refer [this gist](https://gist.github.com/armsp/f8ebd071741a60b3cf20c809310170e7) for a docker image that can run any python3 gobject script. You can also try to understand the dependencies from there.

| PACKAGE | Installation |
| :--- | :--- |
| python3-gi | apt-get install python3-gi |
| python3-gi-cairo | apt-get install python3-gi-cairo |
| gir1.2-gtk-3.0 | apt-get install gir1.2-gtk-3.0 |
| gir1.2-appindicator3-0.1 | apt-get install gir1.2-appindicator3-0.1 |
| libgirepository1.0-dev | apt-get install libgirepository1.0-dev |
| pygobject | pip3 install pygobject |

Not sure about these but might help -
  - python3-gi-cairo
  - gobject-introspection
  - libgtk-3-dev
  - python3-pyside

Resources to help after the above fails -
- [PyGObject Env Setup](https://pygobject.readthedocs.io/en/latest/devguide/dev_environ.html)  
- [PyGObject Quickstart](https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started)
- [Gobject Introspection](https://stackoverflow.com/questions/18025730/pygobject-2-28-6-wont-configure-no-package-gobject-introspection-1-0-found/18027346)

## Usage
1. Clone the repository
2. Extract and go inside the root folder
3. Execute `pip3 install -e .` ( It installs it in development mode. This way you can keep pulling changes from my repository and the changes would be reflected immediately in your environment )
4. Open your terminal and type **disradicator** and press enter.
5. Watch the magic unfold on your Top/Activity bar, right-hand side most probably.

## Proof of Concept
![Appindicator](https://github.com/armsp/disradicator/blob/first_release/docs/movie.gif)

#### COPYRIGHT and LICENSE
All the source files are licensed under GNU GLPv3 license. Refer [LICENSE](https://github.com/armsp/gifc/blob/master/LICENSE) for more details.  

    Discharge Rate Indicator is an appindicator that shows your laptop's discharge rate.
    Copyright (C) 2018  Shantam Raj
    This code is licensed under GNU GPLv3 license. See LICENSE for details

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
