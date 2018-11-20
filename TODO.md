### An incomplete list of possible improvements and directions to take this project to -
* Daemonize the process
  1. Using python [`daemon`](https://pagure.io/python-daemon/)([docs](https://www.python.org/dev/peps/pep-3143/)) or inbuilt `subprocess` library
  2. Using Linux itself like `nohup`, `twisted`, `upstart`, [`daemonize`](http://manpages.ubuntu.com/manpages/bionic/man1/daemonize.1.html)
* Used [_acpid_](https://wiki.archlinux.org/index.php/acpid) instead of directly reading the `/sys` files
* Use [`netlink`](http://man7.org/linux/man-pages/man7/netlink.7.html) to achieve the aboce or maybe something else
* Optimize the [memory usage](https://virtualthreads.blogspot.com/2006/02/understanding-memory-usage-on-linux.html) of the application
* Optimize the CPU usage of the application
* Add it in _StartupApplications_
  - [Possible solution](https://stackoverflow.com/questions/501597/how-to-distribute-desktop-files-and-icons-for-a-python-package-in-gnome-with?noredirect=1&lq=1)
* Make an executable, perhaps something like _Caffeine_
  - Same possible solution as above
* Make a portable app like _Postman_
* Supporting various distros
  1. **Ubuntu Gnome**
     - Temporary Workaround for using this app-indicator is to use an [extension](https://extensions.gnome.org/extension/615/appindicator-support/). This [article](https://www.omgubuntu.co.uk/2017/03/use-indicator-applets-gnome-shell) would be a good starting point to resolve this issue without having to install a third party extension.
  2. **Arch**
  3. **Fedora**
  4. **Debian**
  5. **openSUSE**
  6. **CentOS**
  7. **Gentoo**
* Supporting various platforms
  1. Linux
  2. macOS
  3. Windows

#### Immediate Attentions -
* Change the icon set. The icon is actually pretty large and it has details that aren't visible at all.
* Decouple the terminal that runs the python script from the process itself.

### Should we add the following?
- Travis Continuous Integration
- Pyup
- Coverage
------------------------------------------------
### Updates on decoupling the terminal that spawns the process

| **COMMAND** | **TERMINAL OUTPUT** | **GUI WORKS or NOT** | **ISSUE** |
| :--- | :--- | --- | ---: |
| `python3 appindicator.py &` |  |YES| Killing the terminal terminates the proceses |
| `sudo nohup python3 appindicator.py &` |  |NO||
| `nohup python3 appindicator.py &` | $ nohup python3 appindicator.py & <br>  [2] 5635 <br> $ nohup: ignoring input and appending output to 'nohup.out' Exitng from GUI doesn't show a new prompt. Have to do Ctrl+C to get new line at terminal |YES|Not decoupled from terminal|
| `subprocess.Popen` | |YES| Don't want a new file to start the process.|
| `chmod +x doesn't work` | |NO||

