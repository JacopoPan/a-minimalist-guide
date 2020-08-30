import time
import random
import airsim
import ray
import gym
import numpy as np

from ray import tune
from ray.tune import register_env

from ray.rllib.env.env_context import EnvContext
from ray.rllib.env.external_multi_agent_env import ExternalMultiAgentEnv

from ray.rllib.agents import ppo
from ray.rllib.models import ModelCatalog

class ExternalAirSimMultiAgent(ExternalMultiAgentEnv):

    def __init__(self, env_config: EnvContext, action_space: gym.Space, observation_space: gym.Space, max_concurrent: int):
       self.address = "127.0.0."+str(env_config.worker_index+1)
       print("Init of the environment that will connect to AirSim client", self.address)
       super().__init__(action_space, observation_space, max_concurrent)

    def run(self):
       self.airsimclient = airsim.MultirotorClient(self.address)
       self.airsimclient.confirmConnection()
       self.airsimclient.simPause(True)
       self.num_drones = 2
       for i in range(self.num_drones):
           v_str = "Drone"+str(i)
           self.airsimclient.enableApiControl(True, vehicle_name=v_str)
           self.airsimclient.armDisarm(True, vehicle_name=v_str)
           self.airsimclient.takeoffAsync(timeout_sec=2.0, vehicle_name=v_str)
       self.airsimclient.simContinueForTime(2.0)
       steps_counter = 0
       episode_id = self.start_episode()
       print("starting episode id:", episode_id, "with client", self.address)
       while True:
           steps_counter += 1
           obs = {}
           for i in range(self.num_drones):
               v_str = "Drone"+str(i)
               if self.airsimclient.getMultirotorState(vehicle_name=v_str).kinematics_estimated.position.y_val > 0:
                   obs[i] = 1
               else:
                   obs[i] = 0
           actions = self.get_action(episode_id, obs)                         # or self.log_action(episode_id, obs, action)
           for i in range(self.num_drones):
               v_str = "Drone"+str(i)
               if actions[i]==0:
                   self.airsimclient.moveToPositionAsync(0, -1, -2, 1.0, vehicle_name=v_str)
               if actions[i]==1:
                   self.airsimclient.moveToPositionAsync(0, 1, -2, 1.0, vehicle_name=v_str)
           self.airsimclient.simContinueForTime(1.0)
           rewards = {}
           for i in range(self.num_drones):
               v_str = "Drone"+str(i)
               rewards[i] = self.airsimclient.getMultirotorState(vehicle_name=v_str).kinematics_estimated.position.y_val
           self.log_returns(episode_id, rewards)
           if steps_counter > 4:
               steps_counter = 0
               print("ending episode id:", episode_id, "with client", self.address)
               self.end_episode(episode_id, obs)
               episode_id = self.start_episode()
               print("starting episode id:", episode_id, "with client", self.address)

if __name__ == "__main__":

    print("Initializing Ray")
    ray.shutdown()
    ray.init(ignore_reinit_error=True)
    print("Dashboard URL: http://{}".format(ray.get_webui_url()))

    print("Registering the environment")
    def env_creator(env_config):
        o = gym.spaces.Discrete(2)
        a = gym.spaces.Discrete(2)
        max_conc = 2
        return ExternalAirSimMultiAgent(env_config, o, a, max_conc)
    register_env("ext-ma-airsim", env_creator) #or tune.register_env("ext-ma-airsim", lambda env_config: ExternalAirSimMultiAgent(env_config,o,a,max_conc))

    print("Training")
    stop = {
        "episode_reward_mean": 100,
        "timesteps_total": 2,
    }

    obs_space_dict = {
        "agent_1": gym.spaces.Discrete(2),
        "agent_2": gym.spaces.Discrete(2),
    }
    act_space_dict = {
        "agent_1": gym.spaces.Discrete(2),
        "agent_2": gym.spaces.Discrete(2),
    }

    o_s = gym.spaces.Discrete(2)
    a_s = gym.spaces.Discrete(2)
    config = {
        "env": "ext-ma-airsim",
        "num_workers": 0,
        "env_config": {
            "actions_are_logits": True,
        },
        "multiagent": {
            "policies": {
                "pol1": (None, o_s, a_s, {"agent_id": 0,}),
                "pol2": (None, o_s, a_s, {"agent_id": 1,}),
            },
            "policy_mapping_fn": lambda agent_id: "pol1" if agent_id == 0 else "pol2",
        },
        "framework": "torch",
    }

    tune.run("PPO",stop=stop, config=config, verbose=1)
    ray.shutdown()

    # Alternatively
    #config = ppo.DEFAULT_CONFIG.copy()
    #config["num_workers"] = 0                                                 # only one AirSim Python client connected at a time
    #agent = ppo.PPOTrainer(config, env="ext-ma-airsim")
    #iterations = 2
    #for n in range(iterations):
    #    print(n)
    #    print(agent.train())
    #policy = agent.get_policy()
    #model = policy.model
    #print(model.base_model.summary())













