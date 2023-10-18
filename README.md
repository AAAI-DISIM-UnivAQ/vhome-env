# vhome-env
VirtualHome Python programming environment, with examples and tests.

We would like to have a working environment woth the [VirtualHome](http://virtual-home.org) simulator for our students in which they could experiment with virtual cognitive robotics experiments indoor.

# Installation

inimal installation and test of the [VirtualHome](http://virtual-home.org) simulator

## Conda ENV

To install a Python3.11 interpreter in a GNU/Linux box

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
```
conda create -n python311 python=3.11
conda activate python311
```
## Repos and Downloads

get the modified virtual home repo:

```
git clone https://github.com/AAAI-DISIM-UnivAQ/virtualhome
cd virtualhome
```

get the right simulator according to your OS.
This is for GNU/Linux:

```
wget http://virtual-home.org//release/simulator/v2.0/v2.3.0/linux_exec.zip
unzip linux_exec.zip -d linux_exec
```

for macos, replace `linux_exec` with `macos_exec`

# Installation
```
pip install -e .
```
# Testing
```
python test.py
```
