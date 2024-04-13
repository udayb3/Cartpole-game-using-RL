import gymnasium as gym
import imageio as img
from time import sleep
import numpy as np

# Defining the Parameters and Initialising the Q-table
Learning_rate= 0.001
Discount= 0.98
Total_episodes= 50000
range_v= 50000

# Defining epsilon
Epsilon = 1
start_decay = 1
end_decay = Total_episodes / 5
Eps_decay_value = Epsilon / (end_decay - start_decay)

class Q_learning():
  
  def __init__(self, LR, discount, num_episodes, range_velocity, epsilon, ep_decay):

    # Initializing the arguements
    self.LR= LR; self.discount= discount; self.num_episodes= num_episodes; 
    self.vrange= range_velocity; self.epsilon= epsilon; self.ep_decay= ep_decay

    # Initializing the environment
    self.env= gym.make('CartPole-v1', render_mode='rgb_array')

    # Defining the changed observation
    self.LOW= self.env.observation_space.low
    self.LOW[1]= -range_v; self.LOW[3]= -range_v
    self.HIGH= self.env.observation_space.high
    self.HIGH[1]= range_v; self.LOW[3]= range_v

    self.SIZE_Q= np.array( ( [20] * len( self.HIGH ) ) )
    self.obs_range = ( self.HIGH - self.LOW ) / self.SIZE_Q

    # Initializing the Q-table
    self.Q_tb= np.random.uniform( low= -1, high=0, size= np.append( self.SIZE_Q, self.env.action_space.n ) )

    # Initializing the Reward_list for training
    self.reward_train= []; self.reward_test= []
    self.result_train= []; self.result_test= []
    
    # Initializing the frames for the Imageio module
    self.frames= []

  def Limit(self, value, cmp):
    
    if(value>cmp):
      return cmp
    elif(value<0-cmp):
      return 0-cmp
    else:
      return value

  def Discretize(self, obs: np.array, limiting):

    obs[3]= self.Limit( obs[3]/ 10e15, 50000 )
    obs[1]= self.Limit( obs[1]/10e15, 50000 )

    discrete= obs/limiting
    return tuple( discrete.astype(np.int32) )


  def training(self):

    for ep in range( self.num_episodes ):

      obs_temp, info_temp= self.env.reset(); 
      state_ini= self.Discretize(obs_temp, self.obs_range)

      term= False; trun= False
      reward_ep= 0
      temp_epsilon= self.epsilon

      while(  not (term or trun)):

        # Using epsilong-greedy policy
        if( np.random.random() < temp_epsilon ):
          action= np.random.randint(0, self.env.action_space.n)
        else:
          action= np.argmax( self.Q_tb[state_ini] )
          
        new_state, reward, term, trun, info_= self.env.step( action )
        discrete_state= self.Discretize( new_state, self.obs_range )
        
        # Updating Q-table
        next_value= np.max( self.Q_tb[discrete_state] )
        self.Q_tb[ discrete_state + (action, ) ] = (1- self.LR ) * self.Q_tb[ discrete_state + (action, ) ]
        self.Q_tb[ discrete_state + (action, ) ] = self.Q_tb[ discrete_state + (action, ) ] + self.LR*(reward + self.discount * next_value )
        
        state_ini= discrete_state
        reward_ep += reward
        
      self.reward_train.append( reward_ep )

      print(f"Episode number: {ep + 1}, Steps: {reward_ep}, Epsilon value: {temp_epsilon}", end="\n" )
      ep_result= {'Episode number': ep + 1, 'Steps': reward_ep, 'Epsilon value': temp_epsilon}
      self.result_train.append( ep_result )


      if( ep <= end_decay ) and (ep >= start_decay) and (temp_epsilon - self.ep_decay > 0):
        temp_epsilon -= self.ep_decay
      else:
        self.epsilon= 0
      
  def stats_train(self):
    
    # Print out results
    print(f"Number of episodes: { len( self.reward_train ) }")
    print(f"Max steps per episode: { np.max(self.reward_train  ) }")
    print(f"Avg steps per episode: { np.mean(self.reward_train ) }")
    print(f"Min steps per episode: { np.min(self.reward_train  ) }")


Agent= Q_learning(Learning_rate, Discount, Total_episodes, range_v, Epsilon, Eps_decay_value)
Agent.training()
Agent.stats_train()
