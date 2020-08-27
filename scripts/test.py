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