> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Appendix A - Ubuntu 18.04 and NVIDIA proprietary drivers on Lenovo P52

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

Download Ubuntu 18.04 LTS's 64-bit ISO image
```
$ wget https://releases.ubuntu.com/18.04/ubuntu-18.04.4-desktop-amd64.iso
```
And create a bootable USB stick—e.g., on Ubuntu, using [Startup Disk Creator](https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu#4-iso-and-usb-selection)

**Important**: at boot time, enter the Lenovo P52's BIOS pressing `Enter`, then `F1`

1. Under the `Config` menu, enter the `Display` submenu
- Set `Graphic Device` to `Discrete Graphics` (and not `Hybrid Graphics`)⁠—this will prevent crashes during the installation
2. Under the `Security` menu, enter the `Secure Boot` submenu
- Set `Secure Boot` to `Disabled`⁠—this will let you install NVIDIA graphic drivers

Install Ubuntu 18 (if possible, use Wi-Fi to "download updates and install 3rd party software" during the process)

At the time of the **first login**, click the gear icon besides "Sign in"; choose "Ubuntu on [Wayland](https://wiki.ubuntu.com/Wayland)"

The graphical interface will be very slow⁠—this is expected, the system is not using the GPU nor the CPU integrated graphics

If prompted, install updates from "Software Updater" 

Open the "Software & Updates" application: **NVIDIA's proprietary driver** `nvidia-driver-440` should be available

Select it, click apply, and reboot: this time around, the graphical interface will be running smoothly

Open a terminal (`Ctrl`+`Alt`+`t`) and run command `$ nvidia-smi`: it will report the use of driver 440 and CUDA 10.2
