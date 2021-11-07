> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Appendix A - Ubuntu 18.04 and NVIDIA drivers on Lenovo P52

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

Download Ubuntu 18.04 LTS's 64-bit ISO image
```
$ wget https://releases.ubuntu.com/18.04/ubuntu-18.04.4-desktop-amd64.iso
```
And create a bootable USB stick—e.g., on Ubuntu, using [Startup Disk Creator](https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu#4-iso-and-usb-selection)

**Important**: at boot time, enter the Lenovo P52's BIOS pressing `Enter`, then `F1`

**NOTE 1:** These instructions were tested on a machine with UEFI BIOS Version 1.37, if you have an older BIOS, **update it** [(link)](https://pcsupport.lenovo.com/hn/en/products/laptops-and-netbooks/thinkpad-p-series-laptops/thinkpad-p52-type-20m9-20ma/downloads/ds504024-bios-update-utility-bootable-cd-for-windows-10-64-bit-linux-thinkpad-p52-p72) before changing any of the settings: black screen problems have been fixed up to version 1.18 [(changelog)](https://download.lenovo.com/pccbbs/mobiles/n2cuj11w.txt)

1. Under the `Config` menu, enter the `Display` submenu
- Set `Graphic Device` to `Discrete Graphics` (and not `Hybrid Graphics`)⁠—this will prevent crashes during the installation
2. Under the `Security` menu, enter the `Secure Boot` submenu
- Set `Secure Boot` to `Disabled`⁠—this will let you install NVIDIA graphic drivers

Install Ubuntu 18 (if possible, use Wi-Fi to "download updates and install 3rd party software" during the process)

**NOTE 2 [2021 Update]:** If you are installing Ubuntu 20.04 instead, ignore the next 2 lines and ski to "Software & Updates" -> "Additional Drivers" to install the newest proprietary driver 

At the time of the **first login**, click the gear icon besides "Sign in"; choose "Ubuntu on [Wayland](https://wiki.ubuntu.com/Wayland)"

The graphical interface will be very slow⁠—this is expected, the system is not using the GPU nor the CPU integrated graphics

If prompted, install updates from "Software Updater" 

Open the "Software & Updates" application: **NVIDIA's proprietary driver** `nvidia-driver-440` should be available

Select it, click apply, and reboot: this time around, the graphical interface will be running smoothly

Open a terminal (`Ctrl`+`Alt`+`t`) and run command `$ nvidia-smi`: it will report the use of driver 440 and CUDA 10.2

-------
> Work carried out @ University of Toronto's [Dynamic Systems Lab](https://github.com/utiasDSL) / [Vector Institute](https://github.com/VectorInstitute) / [Mitacs Elevate](https://www.mitacs.ca/en/projects/multi-agent-reinforcement-learning-decentralized-uavugv-cooperative-exploration)


