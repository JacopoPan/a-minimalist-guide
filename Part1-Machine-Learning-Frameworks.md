> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 1 - Machine Learning Frameworks on Lenovo P52

The following instructions are for a fresh install of Ubuntu 16.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter
 
At startup, access the BIOS (on the P52, `Enter`, then `F1`) and, under "*Security*" -> "*Secure Boot*", disable "*Secure Boot*"

Verify the presence of an NVIDIA GPU
``` 
$ lspci | grep -i nvidia
```
Verify the use of an `x86_64` operating system
```
$ uname -m && cat /etc/*release
```
Verify the presence of the `gcc` GNU compiler collection—if missing, install it with `sudo apt-get install build-essential`
```
$ gcc --version
```
Install headers for the current kernel
```
$ sudo apt-get install linux-headers-$(uname -r)
```

## Install `conda`

Anaconda combines a package manager (like `pip`) with an environment manager (like `virtualenv`), called `conda`

Unlike `pip`, Anaconda is not limited to Python software

Nonetheless, the Pyhthon Package Index ([PyPI](pypi.org)) has more and more recent packages than Anaconda

Thus, the use of `pip` within a `conda` environment can be justified 

### Install Anaconda prerequisites

```
$ sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

### Install Anaconda with Python 3.7 and 64-bit (x86)

Download the installer (verify [here](https://docs.anaconda.com/anaconda/install/linux/) if a newer version was released)
```
$ wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
```
Verify the download integrity with SHA-256
```
$ sudo apt install hashalot
$ sha256sum ./Anaconda3-2020.02-Linux-x86_64.sh
```
This installer should return `2b9f088b2022edb474915d9f69a803d6449d5fdb4c303041f60ac4aefcc208bb`

Note: newer installers will have different hashes

Run the installer
```
$ bash Anaconda3-2020.02-Linux-x86_64.sh
```
Accept the terms and conditions

Press `Enter` to accept the default installation folder

When prompted to "*Do you wish the installer to initialize Anaconda3 by running conda init?*" answer "*yes*"

Finally, run 
```
$ source ~/.bashrc
```
Turn off the auto-activation of the `base` environment and exit it
```
$ conda config --set auto_activate_base False
$ conda deactivate
``` 
Create a new Python 3.7 environment called `learning`
```
$ conda create --name learning python=3.7
```
Enter and leave `learning` with
```
$ conda activate learning
$ conda deactivate
```
Review the installed packages in `learning` with
```
$ conda list -n learning
```
List your environments with
```
$ conda env list
```
Delete an environment (e.g. `learning`) with
```
$ conda remove --name learning --all
``` 
Share an environment using a YAML file 
```
$ conda activate learning
$ conda env export > learning.yml
```
Import an environment from a YAML file
```
$ conda env create -f learning.yml
```
To use `pip` within environment `learning` 
```
$ conda install -n learning pip
$ conda activate learning
$ pip install oct2py                                  # NOTE: package oct2py requires "$ sudo apt-get install octave"
```
To install new software in a `conda` environment

- Search for Anaconda packages first `conda search <pkg>`

- If they are not available, use `pip` within a `conda` environment

- Do NOT use `pip` with the `--user` argument

### (optional) Install Python 3.7 via PPA

Ubuntu 16.04 LTS comes with Pyhton 2.7 and 3.5

The procedure above lets you use Python 3.7 (as the default `python`) only within `conda`'s environment `learning`

To install and use Python 3.7 outside `conda`, follow these steps
```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.7                          # Python 3.7 is now your default "$ python"  
```

## Install TensorFlow 2

Note: TensorFlow [instructions](https://www.tensorflow.org/install/gpu) use `virtualenv` and `pip` but here we use `conda` and `pip` instead 

Activate `learning`—i.e. an environment with the appropriate versions of Python (>=3.5) and `pip` (>=19.0)
```
$ conda activate learning
$ python --version
$ pip --version
```
Install TensorFlow
```
$ pip install tensorflow
```

## Install CUDA support for TensorFlow

Add the NVIDIA package repositories and HTTPS support for `apt-key`
```
$ sudo apt-get install gnupg-curl
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_10.1.243-1_amd64.deb
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
$ sudo dpkg -i cuda-repo-ubuntu1604_10.1.243-1_amd64.deb
$ sudo apt-get update
$ wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
$ sudo apt install ./nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb
$ sudo apt-get update
```
Install NVIDIA driver `nvidia-418`
```
$ sudo mkdir /usr/lib/nvidia # (only if needed)
$ sudo apt-get install --no-install-recommends nvidia-418
```
Reboot, check that the GPU is visible using command `nvidia-smi`, it should report driver version 4.18 and no CUDA yet

Install development and runtime libraries (approx. 4GB)
```
$ sudo apt-get install --no-install-recommends cuda-10-1 libcudnn7=7.6.4.38-1+cuda10.1 libcudnn7-dev=7.6.4.38-1+cuda10.1
```
Install TensorRT (requires that `libcudnn7` is installed above)
```
$ sudo apt-get install -y --no-install-recommends libnvinfer6=6.0.1-1+cuda10.1 libnvinfer-dev=6.0.1-1+cuda10.1 libnvinfer-plugin6=6.0.1-1+cuda10.1
```
Reboot, note that [this procedure](https://www.tensorflow.org/install/gpu) was written for CUDA 10.1 and driver `nvidia-418` 

Yet, at the time of this writing (May 2020), it leads to the installation of CUDA 10.2 and driver `nvidia-440`

This can be verified using commands `$ nvidia-smi` and `$ cat /proc/driver/nvidia/version`

Verify the GPU is visible by TensorFlow
```
$ conda activate learning
$ python
```
Then, within the Python interpreter
```
>>> import tensorflow as tf
>>> physical_devices = tf.config.list_physical_devices('GPU') 
>>> print("Num GPUs:", len(physical_devices)) 
```

## Install PyTorch

Install [PyTorch](https://pytorch.org/get-started/locally/) 1.5 with support for CUDA 10.2 through Anaconda
```
$ conda activate learning
$ conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
```
To verify that the installation was successful
```
$ conda activate learning
$ python
```
Then, within the Python interpreter
```
>>> import torch
>>> x = torch.rand(5, 3)
>>> print(x)
>>> print(torch.cuda.is_available())
```

## Install Gym

Install OpenAI's [Gym](https://gym.openai.com/docs/)
```
$ conda activate learning
$ pip install gym
```
Verify Gym's installation
```
$ rm -f ~/test-gym.py
$ printf "import gym\nenv = gym.make('CartPole-v0')\nfor i_episode in range(20):\n    observation = env.reset()\n    for t in range(100):\n        env.render()\n        print(observation)\n        action = env.action_space.sample()\n        observation, reward, done, info = env.step(action)\n        if done:\n            print(\"Episode finished after {} timesteps\".format(t+1))\n            break\nenv.close()" >> ~/test-gym.py
$ conda activate learning
$ python ~/test-gym.py
```

## Install Ray (including Ray Core, Tune, and RLlib)

Install [Ray Core](https://docs.ray.io/en/latest/walkthrough.html)
```
$ conda activate learning
$ pip install ray
```
Verify Ray Core's installation
```
$ conda activate learning
$ python
```
Then, within the Python interpreter
```
>>> import ray
>>> ray.init()
```
Open a browser and navigate to `localhost:8265` to find Ray's dashboard

### Ray Tune (using Pandas and TensorBoard)

Install [Ray Tune](https://docs.ray.io/en/latest/tune.html) (includes Pandas, see this [10' introduction](https://pandas.pydata.org/docs/getting_started/10min.html))
```
$ conda activate learning
$ pip install ray[tune]
```
Save the following script as `~/test-tune.py`
```
import torch.optim as optim
from ray import tune
from ray.tune.examples.mnist_pytorch import get_data_loaders, ConvNet, train, test
def train_mnist(config):
    train_loader, test_loader = get_data_loaders()
    model = ConvNet()
    optimizer = optim.SGD(model.parameters(), lr=config["lr"])
    for i in range(10):
        train(model, optimizer, train_loader)
        acc = test(model, test_loader)
        tune.track.log(mean_accuracy=acc)
analysis = tune.run(
    train_mnist, config={"lr": tune.grid_search([0.001, 0.01, 0.1])})
print("Best config: ", analysis.get_best_config(metric="mean_accuracy"))
df = analysis.dataframe()
```
Verify Tune's installation
```
$ conda activate learning
$ python ~/test-tune.py
```
To visualize the results in [TensorBoard](https://www.tensorflow.org/tensorboard/get_started), open a new terminal (`Ctrl`+`Alt`+`t`) and type
```
$ conda activate learning
$ tensorboard --logdir ~/ray_results
```
Open a browser and navigate to `localhost:6006` to find TensorBoard

### Ray RLlib

Install [RLlib](https://docs.ray.io/en/latest/rllib.html)
```
$ conda activate learning
$ pip install ray[rllib] ray[debug]
```
Save the following script as `~/test-rllib.py`
```
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
tune.run(PPOTrainer, config={"env": "CartPole-v0"}) 
```
Verify RLlib's installation
```
$ conda activate learning
$ python ~/test-rllib.py
```
Use `Ctrl`+`c` to interrupt the training

## Install Keras (and Keras-RL)

Install [Keras](https://keras.io/#installation)
```
$ conda activate learning
$ pip install keras                                   # optional dependencies: h5py, graphviz, and pydot 
```
Save the following script as `~/test-keras.py`
```
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20, batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
```
Verify Keras' installation
```
$ conda activate learning
$ python ~/test-keras.py
```

### Keras-RL 

Install [Keras-RL](https://github.com/keras-rl/keras-rl)
```
$ conda activate learning
$ pip install keras-rl h5py Pillow gym[atari]
```
Save the following script as `~/test-keras-rl.py`
```
import numpy as np
import gym
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from rl.agents.cem import CEMAgent
from rl.memory import EpisodeParameterMemory
ENV_NAME = 'CartPole-v0'
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n
obs_dim = env.observation_space.shape[0]
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(nb_actions))
model.add(Activation('softmax'))
print(model.summary())
memory = EpisodeParameterMemory(limit=1000, window_length=1)
cem = CEMAgent(model=model, nb_actions=nb_actions, memory=memory, batch_size=50, nb_steps_warmup=2000, train_interval=50, elite_frac=0.05)
cem.compile()
cem.fit(env, nb_steps=100000, visualize=False, verbose=2)
cem.save_weights('cem_{}_params.h5f'.format(ENV_NAME), overwrite=True)
cem.test(env, nb_episodes=5, visualize=True)
```
Verify Keras-RL installation
```
$ conda activate learning
$ python ~/test-keras-rl.py
```
Note: Keras-RL is not frequently maintained, many of the [examples](https://github.com/keras-rl/keras-rl/tree/master/examples) debugging/tweaks

## (deprecated) Install unofficial NVIDIA drivers via PPA

Follow these steps only if 
- You did NOT install the NVIDIA driver and CUDA with TensorFlow
- You do NOT plan on using CUDA acceleration 
- You only want to install a driver for your graphics

Remember to disable "*Secure Boot*" in the BIOS (see the top of this page)

Unofficial binary drivers for NVIDIA graphics can be added using
```
$ sudo add-apt-repository ppa:graphics-drivers/ppa
$ sudo apt-get update
```
These can then be found under Ubuntu's "*Software & Updates*" -> "*Additional Drivers*"



-------
> Work carried out @ University of Toronto's [Dynamic Systems Lab](https://github.com/utiasDSL) / [Vector Institute](https://github.com/VectorInstitute) / [Mitacs Elevate](https://www.mitacs.ca/en/projects/multi-agent-reinforcement-learning-decentralized-uavugv-cooperative-exploration)


