> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> By a novice for the novice

# Part 5 - RL with MuJoCo 2.10

The following instructions are for macOS Big Sur (11.6.1) on a 2020 Intel MacBook Pro

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

## Download and install `mujoco210`

Download and install the latest release (also see [this page](https://mujoco.org/download))
```
cd ~
wget https://mujoco.org/download/mujoco210-macos-x86_64.tar.gz
tar -xf mujoco210-macos-x86_64.tar.gz
mkdir .mujoco
mv mujoco210 ~/.mujoco/
rm mujoco210-macos-x86_64.tar.gz
```
Run an simulation
```
cd ~/.mujoco/mujoco210/bin/
./simulate ../model/cloth.xml
```

## TBD

...

-------
> Work carried out @ University of Toronto's [Dynamic Systems Lab](https://github.com/utiasDSL) / [Vector Institute](https://github.com/VectorInstitute) / [Mitacs Elevate](https://www.mitacs.ca/en/projects/multi-agent-reinforcement-learning-decentralized-uavugv-cooperative-exploration)

