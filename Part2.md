> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 2 - Port your `conda` and codebase to Vector's cluster

Credentials (username and password) for the cluster and the [Wiki](https://support.vectorinstitute.ai/Computing) are issued by ops@vectorinstitute.ai

## Login using `ssh`

Note: in what follows, remember to always replace `username` with your username—both in `ssh` logins and folder paths

Connect to one of Vector's locations—this is an example of sequential connections (and disconnections) to all locations
```
$ ssh username@vremote.[omitted domain]    # for the Vaughan location
$ exit                                     # close the connection
$ ssh username@vremote1.[omitted domain]   # alternative login for the Vaughan location
$ exit
$ ssh username@v.[omitted domain]          # for the Vaughan2 location
$ exit
$ ssh username@q.[omitted domain]          # for the MaRS location
$ exit
$ ssh username@m.[omitted domain]          # alternative login for the MaRS location
$ exit
```
For your first logins, answer "*yes*" to question "*Are you sure you want to continue connecting (yes/no)?*"

For an overview of the CPUs and GPUs at these locations, refer to slides 5 and 6 of [this presentation](https://support.vectorinstitute.ai/Computing?action=AttachFile&do=view&target=Research_computing_orientation_presentation.pdf)

Remember: you should not run intense computing when you simply login via `ssh`

Instruction on how to use `slurm` for heavy workloads are given later in this guide

### `ssh` login from your workstation without a password

Assuming you do NOT already have files `id_rsa` and `id_rsa.pub` in folder `~/.ssh` of your local machine
- (If you do, skip the next 3 lines)

On your local machine, run
```
$ ssh-keygen -t rsa
```
Do not enter a filename or a passphrase, just press `Enter` 3 times

Your identification `id_rsa` and public key `id_rsa.pub` will be created in `~/.ssh`

Login to the remote machines (`m` and `v`)⁠—with password⁠—and created directory `~/.ssh`
```
$ ssh username@m.[omitted domain]
$ mkdir -p ~/.ssh                        # this happens on MaRS (where you land either using m.[omitted domain] or q.[omitted domain])
$ exit
$ ssh username@v.[omitted domain]
$ mkdir -p ~/.ssh                        # this happens on Vaughan (where you land either using vremote.[omitted domain], vremote1.[omitted domain], or v.[omitted domain])
$ exit
```
From your local machine run this command to copy the public key to the remote machines (replace `username` with your username)
```
$ cat ~/.ssh/id_rsa.pub | ssh username@m.[omitted domain] 'cat >> ~/.ssh/authorized_keys'
$ cat ~/.ssh/id_rsa.pub | ssh username@v.[omitted domain] 'cat >> ~/.ssh/authorized_keys'
```
You can now `ssh` to all locations without entering your password (note: [you might still, occasionally, be asked](http://www.linuxproblem.org/art_9.html))
```
$ ssh username@m.[omitted domain]        # the same as q.[omitted domain]
$ exit
$ ssh username@v.[omitted domain]        # the same as vremote.[omitted domain], vremote1.[omitted domain]
$ exit
```

## Reminder of a few useful commands and shortcuts

Access a login server (e.g. `m.[omitted domain]`)
```
$ ssh username@m.[omitted domain]        # change "username" and server "m" as appropriate
```
Try the following
```
$ echo $USER                             # your username
$ echo $HOME                             # the absolute path to your home directory, also called "~", i.e. "/h/username"
$ pwd                                    # the absolute path of your current location in the file system
$ printenv                               # show all the environmental variables
                                         # e.g., $PATH: the directories where your system searches for executables
```
Additional extreme Unix basics are on this [cheatsheet](https://files.fosswire.com/2007/08/fwunixref.pdf)

## File system differences across Vector's locations

Note: there minor differences in the file system organization of your home `~` and `scratch` folders across Vector's location

MaRS (login using `q.[omitted domain]`, `m.[omitted domain]`)
```
/h/$USER                                # your home directory
/scratch/gobi1/$USER                    # your fast disk space
/scratch/gobi2/$USER                    # your large disk space
/scratch/gobi1/datasets                 # fast shared space for datasets
/scratch/gobi2/datasets                 # large shared space for datasets
```
Vaughan/Vaughan2 (login using `vremote.[omitted domain]`, `vremote1.[omitted domain]`, `v.[omitted domain]`)
```
/h/$USER                                # your home directory
                                        # NOTE: "/h/username/" is another name for "/scratch/ssd001/home/username" 
/scratch/ssd001/home/$USER              # your fast disk space
/scratch/hdd001/home/$USER              # your large disk space
/scratch/ssd001/datasets                # fast shared space for datasets
/scratch/hdd001/datasets                # large shared space for datasets
```

## Pre-installed software

Double check what software is already installed 
```
$ ssh username@m.[omitted domain]       # change "username" and server "m" as appropriate
$ cd /pkgs
$ ls
```
The list should include 
- Anaconda (3.7)
- CUDA (10.1)
- PyTorch (1.4 for CUDA 10.1 Python 3.6)
- TensorFlow 2 (for CUDA 10.1 and Python 3.6)
- MuJoCo
- R, etc.

You can ask ops@vectorinstitute.ai to install new packages using the following command
```
$ echo "octave" >> /tmp/packages        # to ask for the installation of "octave"
```

## Create your environment on Vector's locations

Note: the instructions below are for the MaRS location; they can be used on Vaughan/Vaughan2 replacing 
- `m.[omitted domain]` with `v.[omitted domain]`
- `gobi1` with `ssd001/home`

If you are familiar with `conda` (or read `README.md` in this repository), you might want to enter and leave `conda` environments using `$ conda activate environmentname` and `$ conda deactivate`

While this is technically possible it requires to modify
- Your `~/.bash_profile` file (for `ssh` sessions)
- Your `~/.bashrc` file (for `bash`, e.g., in `slurm` interactive and batch sessions)

**THIS IS BAD PRACTICE: modifying your `.bashrc` and `.bash_profile` files makes it difficult to port your project from one location to the other and/or merging configurations across locations**

Instead, you should stick to
```
$ source activate name-or-path-to-the-conda-environment
$ source deactivate 
```
For certain `conda` versions, `source deactivate` might trigger a deprecation warning that one can ignore

### Select your preferred version of Anaconda (and Python)

Login via `ssh`
```
$ ssh username@m.[omitted domain]       # change "username" and server "m" as appropriate
```
Choose your preferred version of `conda`

This can be done by adding, to environmental variable `PATH`, the location of the binaries of the corresponding, preinstalled version of Anaconda
- `/pkgs/anaconda2/bin` uses `conda` 4.4.10 and Python 2.7.15
- `/pkgs/anaconda3/bin` uses `conda` 4.7.12 and Python 3.6.10
- `/pkgs/anaconda37/bin` uses `conda` 4.5.11 and  Python 3.7.3
For example, for the newest `conda` 4.7.12 (with Python 3.6)
```
$ export PATH=/pkgs/anaconda37/bin:$PATH
```
(Note: there is also a `/pkgs/anaconda27/bin` installation using Python 3.7.3 but I was not able to run `conda` when exporting these binaries)

Verify `conda`'s version with `$ conda --version` 

Running command `$ python` should start the corresponding version

### Install Python, `pip`, and your project's packages

Create a `conda` environment **with Python 3.7** in your fast disk space (i.e. `/scratch/gobi1/username/`) 
- Option `-p /scratch/gobi1/username/learning` creates and sets the folder location of your environment
- String `/scratch/gobi1/username/learning` will be used in all `conda` commands to refer to it
```
$ conda create -p /scratch/gobi1/$USER/learning python=3.7  # change disk "gobi1" and Python version 3.7 as appropriate
```
When asked to "*Proceed ([y]/n)?*" answer "*y*"

Activate the environment using `source`
```
$ source activate /scratch/gobi1/$USER/learning
```
Note: since the environment was created using `-p`, the steps to remove it (if necessary) are now the following
```
$ conda remove -p /scratch/gobi1/$USER/learning --all
$ conda env remove -p /scratch/gobi1/$USER/learning
```
Use `$ which pip` to verify that it is currently pointing to the local `/scratch/gobi1/username/learning/bin/pip`

Note: if you omitted option `python=X.Y` when creating the environment, `$ which pip` will return the central `/pkgs/anacondaXX/bin/pip`

To address this, install `pip` within the environment using
```
$ source activate /scratch/gobi1/$USER/learning
$ conda install pip
```
When asked to "*Proceed ([y]/n)?*" answer "*y*"

List the packages installed in environment `/scratch/gobi1/username/learning`
```
$ conda list -p /scratch/gobi1/$USER/learning
```
List your environments
```
$ conda env list
```
Install TensorFlow and PyTorch in environment `/scratch/gobi1/username/learning`
```
$ source activate /scratch/gobi1/$USER/learning
$ pip install tensorflow
$ conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
```
When asked to "*Proceed ([y]/n)?*" answer "*y*"

To install the other packages at once, save them in a file, e.g. `requirements.txt` containing text
```
keras
ray
ray[tune]
ray[rllib]
ray[debug]
keras-rl
h5py
Pillow
gym[atari]
```
And run
```
$ pip install -r requirements.txt
```
Verify all packages can be correctly imported in Python 3.7
```
$ python
>>> import tensorflow as tf
>>> import keras
>>> import torch
>>> import ray
>>> from ray import tune
>>> from ray.rllib.agents.ppo import PPOTrainer
>>> from rl.agents.cem import CEMAgent
>>> import gym
```
Repeat this procedure for `v.[omitted domain]`, using `ssd001/home` in place of  `gobi1`

### Debug in shell using a `slurm` interactive session

Remember: one is not supposed to run heavy workloads just by logging in through `ssh` 

Intense CPU and GPU computing is managed by the `slurm` manager in two ways

- Interactively, e.g. creating a `bash` shell session with command `srun`
- Asynchronously, submitting a `.slurm` script with command `sbatch`

Check the available partitions (CPUs, GPUs, interactive, etc.) and the queued jobs at a location (e.g. MaRS)
```
$ ssh username@m.[omitted domain]     # change "username" and server "m" as appropriate
$ sinfo
$ squeue                              # use "$ squeue -u username" to only see jobs belonging to user "username"
```
Start a `bash` shell in an interactive session (for up to 3 hours) with a GPU (to test its support)
```
$ srun --mem=4GB --gres=gpu:1 --pty /bin/bash
```
Note: you can only start an interactive session on a location with interactive partitions

Verify the presence of a GPU and the version of CUDA
```
$ nvidia-smi
```
Select `conda` environment `/scratch/gobi1/username/learning`
```
$ source activate /scratch/gobi1/$USER/learning
```
Export the paths towards the latest CUDA shared libraries 
```
export LD_LIBRARY_PATH=/pkgs/cuda-10.1/lib64:/pkgs/cudnn-10.1-v7.6.3.30/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
Verify that TensorFlow can see the GPU
```
$ python
```
In the interpreter, type
```
>>> import tensorflow as tf
>>> physical_devices = tf.config.list_physical_devices('GPU') 
>>> print("Num GPUs:", len(physical_devices)) 
```
Verify that PyTorch can use CUDA
```
$ python
```
In the interpreter, type
``` 
>>> import torch
>>> print(torch.cuda.is_available())
```
Note: this second test might not succeed in an interactive session (e.g. if `nvidia-smi` reported CUDA 10.0) but still work when you submit your job with `sbatch` to a different partition

### Submit your script for execution using `slurm` batch sessions

This section verifies the correct use of your `conda` environment, CUDA, and packages in `slurm`'s batch mode

In your local machine's home directory (`$ cd ~`), save the following lines as `test.py`
```
import tensorflow as tf
import keras
import torch
import ray
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
from rl.agents.cem import CEMAgent
import gym

# Check GPU and CUDA availability
physical_devices = tf.config.list_physical_devices('GPU') 
print("TF Num GPUs:", len(physical_devices)) 
print("PyTorch CUDA", torch.cuda.is_available())
```
In your local machine's home directory (`$ cd ~`), save the following lines as `test.slrm`
```
#!/bin/bash

#SBATCH --job-name=test_job
#SBATCH --output=/h/YOURUSERNAME/output-%N-%j.out    # LINE 4 - NOTE: for output and error, use absolute paths that exists already
#SBATCH --error=/h/YOURUSERNAME/error-%N-%j.err      # LINE 5 - NOTE: %N and %j will be replaced by the host name and job id, respectively
#SBATCH --open-mode=append
#SBATCH --partition=gpu                              # self-explanatory, set to your preference (e.g. gpu or cpu on MaRS, p100 on Vaughan)
#SBATCH --cpus-per-task=1                            # self-explanatory, set to your preference
#SBATCH --ntasks-per-node=1
#SBATCH --mem=4G                                     # self-explanatory, set to your preference
#SBATCH --gres=gpu:1                                 # NOTE: you need a GPU for CUDA support; self-explanatory, set to your preference 
#SBATCH --nodes=1
#SBATCH --qos=normal

rm -f ~/test.log                                     # remove any previous copy of "test.log" which is used by "test.sh" to append its output

echo $SLURM_JOB_ID >> ~/test.log                     # log the job id
echo $SLURM_JOB_PARTITION >> ~/test.log              # log the job partition

export LD_LIBRARY_PATH=/pkgs/cuda-10.1/lib64:/pkgs/cudnn-10.1-v7.6.3.30/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}      # required for TensorFlow to see any GPU

source activate /scratch/gobi1/$USER/learning/       # LINE 22 - NOTE: set the path to your conda environment
echo $CONDA_PREFIX >> ~/test.log                     # log the active conda environment 

python --version >> ~/test.log                       # log Python version

python ~/test.py >> ~/test.log                       # the script above, with its standard output redirected to test.log

source deactivate
```
Note: in lines 4, 5, and 22
- Replace `YOURUSERNAME` with your username (required)
- Replace `/scratch/gobi1/$USER/learning/` with your `conda` environment

Copy these two files to your home directory on one of Vector's locations
```
$ scp ~/test.* username@m.[omitted domain]:~/        # change "username" and server "m" as appropriate
```
Login to the same location and submit the job for execution
```
$ ssh username@m.[omitted domain]                    # change "username" and server "m" as appropriate
$ sbatch ~/test.slrm
```
It will return `$ Submitted batch job 491956`, where 491956 is, for example, the id of your job

Once the job is queued, check for its status
```
$ scontrol -d show job 491956 | grep Reason          # change job id 491956 as appropriate
```
Once it returns `$ JobState=COMPLETED Reason=None Dependency=(null)`, use
```
$ cat ~/temp.log
```
Verify that your output looks similar to
```
491956                                               # this will be your job id
gpu                                                  # this will be the partition you chose
/scratch/gobi1/username/learning                     # this will be the path of your conda environment
Python 3.7.7
TF Num GPUs: 1
PyTorch CUDA True
```
`error-gruppy8-491956.err` should contain `Using TensorFlow backend.` (`gruppy8` might be replaced by another host name)

`output-gruppy8-491956.out` should be empty

To cancel a job with id `491956`
```
$ scancel 491956
```
To change the desired target partition of job with id `491956` to `gpu`
```
$ scontrol update jobid=491956 partition=gpu
```
Also check these `slurm` [cheatsheet](https://slurm.schedmd.com/pdfs/summary.pdf) and [tutorial](https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html)

## Transferring data between a local computer and Vector's locations 

Besides being good at [`vim`](https://www.tutorialspoint.com/vim/vim_quick_guide.htm), a few commands can speed-up the workflow between a local and a remote machine

### `wget`, `scp` and `rsync` to copy files 

From your `ssh` login, you can download files from the internet using `wget`
```
$ wget https://releases.ubuntu.com/16.04/ubuntu-16.04.6-desktop-amd64.iso
```
To re-start interrupted downloads use `-c`
```
$ wget -c https://releases.ubuntu.com/16.04/ubuntu-16.04.6-desktop-amd64.iso
```
On the terminal of a local machine, you can download files from the cluster with [`scp`](http://www.hypexr.org/linux_scp_help.php)
```
$ scp username@m.[omitted domain]:~/foo.txt ~/Downloads
```
Or entire folders (just be careful when using a command with option `-r`)
```
$ scp -r username@m.[omitted domain]:~/a-folder/ ~/Downloads
```
Vice versa, you can upload files and folders from your local machine to your cluster home folder using
```
$ scp ~/a-file.txt username@m.[omitted domain]:~/
$ scp -r ~/a-folder/ username@m.[omitted domain]:~/
```
For large folders, [`rsync`](https://www.linuxtechi.com/rsync-command-examples-linux/) is preferable
```
$ rsync -zarvh ~/a-folder/ username@m.[omitted domain]:~/                    # upload from local to remote
$ rsync -zarvh username@m.[omitted domain]:~/ ~/a-folder/                    # download from remote to local
```

### `git` and GitHub

To use your password but to avoid typing your username every time you `git push` or `git pull`

If you do NOT want to create a private `ssh` key on a shared machine, do this
```
$ git config --global user.name JacopoPan                                    # change JacopoPan to your GitHub username
$ git config --global user.email "jacopo.panerati@utoronto.ca"               # change the address to your GitHub e-mail
$ git clone https://JacopoPan@github.com/JacopoPan/a-minimalist-guide.git    # change to the desired repository
```
Note: in the 3rd line, you should use `https` and add `YourGitHubUsername@` before `github.com`

To push changes to GitHub
```
$ git add -u
$ git add name-of-new-file1 name-of-new-file2
$ git commit -m "commit message"
$ git status                                                                 # verify the status of the repo
$ git push
```
You will only be prompted for your password

### `bash` scripts

Finally, note that almost everything that appears after a `$` in this document can be automated using `bash` scripts

For example, save these lines as `push-existing-file-changes.sh`
```
#!/bin/bash

git add -u
git commit -m "changes made on $HOSTNAME"
git push
```
Make the script executable and move it to your git repository folder
```
$ chmod +x push-existing-file-changes.sh
$ mv push-existing-file-changes.sh ~/git-repo/
```
Now, modified files in the repo can be pushed by running a single script
```
$ cd ~/git-repo/
$ ./push-existing-file-changes.sh
```
The commit message will state the name of the machine where the commit originated
 
[Nathan's GitHub examples](https://github.com/nng555/cluster_examples) show how to use [`bash`](https://www.gnu.org/software/bash/manual/html_node/index.html) to automate a hyperparameters sweep with `slurm`

### `crontab` for periodic tasks

As pointed out [here](https://support.vectorinstitute.ai/Computing/CronRsync), one can use `crontab` to periodically execute a script

For example, to synchronize the content of folder `send` on MaRS to folder `deliver` on Vaughan every 15'

First setup `ssh` access via key from `m` to `v`

On MaRS, create a private-public key pair
```
$ ssh-keygen -t rsa
```
Do not enter a filename or a passphrase, just press `Enter` 3 times

Add the public key to the authorized keys on Vaughan 
```
$ cat ~/.ssh/id_rsa.pub | ssh username@v.[omitted domain] 'cat >> ~/.ssh/authorized_keys'
```
Still on MaRS, create script `repeat.sh` with content
```
#!/bin/bash

rsync -zarvh ~/send/ username@v.[omitted domain]:~/deliver/ --delete
```
Make it executable and create directory `send` on MaRS
```
$ chmod +x ~/repeat.sh
$ mkdir ~/send
```
Run `crontab -e` to edit `crontab`s tasks

The first time, you will be asked for your favourite editor (`vim`)

Append this line (and an empty one) to the file to run `repeat.sh` every 15'
```
*/15 * * * * ~/repeat.sh
```
Save and close (`:wq`)

See `crontab`'s tasks with `crontab -l`

The creation and removal of documents from `~/send` (on MaRS) will be reflected in `~/deliver` (on Vaughan) within 15'

Note: [as explained by George](https://support.vectorinstitute.ai/Computing/CronRsync) add option
- `-e "ssh -i /h/$USER/.ssh/rsync -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"`
to use `rsync` over `ssh` (safer and more reliable)
