An incomplete list of possible improvements and directions to take this project to -
* Daemonize the process
  1. Using python [`daemon`](https://pagure.io/python-daemon/)([docs](https://www.python.org/dev/peps/pep-3143/)) or inbuilt `subprocess` library
  2. Using Linux itself like `nohup`, `twisted`, `upstart`, [`daemonize`](http://manpages.ubuntu.com/manpages/bionic/man1/daemonize.1.html)
* Used [_acpid_](https://wiki.archlinux.org/index.php/acpid) instead of directly reading the `/sys` files
* Use [`netlink`](http://man7.org/linux/man-pages/man7/netlink.7.html) to achieve the aboce or maybe something else
* Optimize the [memory usage](https://virtualthreads.blogspot.com/2006/02/understanding-memory-usage-on-linux.html) of the application
* Optimize the CPU usage of the application
* Add it in _StartupApplications_
* Make an executable, perhaps something like _Caffeine_
* Make a portable app like _Postman_
* Supporting various distros
* Supporting various platforms

Immediate Attentions -
* Change the icon set. The icon is actually pretty large and it has details that aren't visible at all.
* Decouple the terminal that runs the python script from the process itself.

