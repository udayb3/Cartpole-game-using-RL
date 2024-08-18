# CartPole Game using Reinforcement Learning

### Hello, This project uses Reinforcement Learning to train the classic CartPole Game. The aim was to make the Pole balance for a longer period of time. 

### Table of Contents
<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText="Click to expand") -->
<details>
<summary>Index</summary>

- [Overview](#overview)
- [Set-up and Files information](#setup)
- [Environment](#environment)
- [Q-Learning Algorithm](#algorithm)
- [Final Results](#results)
- [References](#references)
- [License](#license)
</details>
<!-- AUTO-GENERATED-CONTENT:END -->

### Overview

- #### We have used [Gymnasium](https://gymnasium.farama.org/) which is a maintained fork of OpenAI's gym. This was done by understanding the environment and actions which were provided by the library.

- #### We used Q learning to train the model and test it using the Q-table values. The results were that we could make the pole stay in position for about 60 steps. Here is the video which shows 58 steps taken by the CartPole.

  https://github.com/udayb3/Cartpole-game-using-RL/assets/148479732/9ec96e5a-9c38-4350-8f93-bd2c1a7ce10f

### Setup

- #### All the requirements for the code to run are provided in the `requirements.txt` file.

- #### You can install the libraries directly by running the following command locally/globally.
  > pip install -r requirements.txt

- #### You can run the `Q_learning_based` file in the python_files directory. Modify the code depending upon the episodes number, video path, result file path, etc.

- #### File descriptions:
  - _Python-Files_:  It consists of `Q_learning_based.py` file for the Q_learning algorithm.
  -  _Collab_Notebooks_: It consists of `Q_learning_based.ipynb` file for running in collab without any dependencies. All the dependencies are already set-up in the Notebook.
  - _results_: It consists of the `Q\_learning.txt` file which contain the result of the Q_learning algorithm.
  - _video_: It consists of the video results obtained from the Q_learning algorithm with the help of `Imageio` library.
  - requirements.txt consists of the libraries required to run the `Q_learning` file.

### Environment

- #### `CartPole-v_1` is used for the Reinforcement Learning algorithms.

- #### The _Observation Space_ consists of four Continuous features:
  1. Position (-0.5 to 0.5)
  2. Velocity ( -inf to inf )
  3. Angle ( -0.24 to 0.24 )
  4. Angular Velocity ( -inf to inf )

- #### The _Action Space_ consists of 2 Discrete states:
  1. 0: Pushing the cart to the left.
  2. 1: Pushing the card to the right.

- #### Reward was given everytime whenever a step was taken by the agent.

- #### There were 3 termination conditions for ending an episode
  1. Pole angle becomes greater than 12 degree.
  2. Position is not in the region of 2.4 units.
  3. The total number of steps become more than 500 in an episode.

- #### We have diminished the observation space:
  1. Velocity ( -50000 to +50000 )
  2. Angular Velocity ( -50000 to +50000 )

- #### The API of `Gymnasium` enabled us to use their methods and the above description of the environment is also explained in the detailed manner [here](https://gymnasium.farama.org/environments/classic_control/cart_pole/).

### Algorithm

- #### We have used Q-Learning algorithm for the task with the ε-greedy Exploration policy.

- #### For this, we created a class for the Q_learning algorithm. This consists of the methods for _training_, _testing_, _Saving video_, _Exploration Policy_, _Discretizing function_.

- #### When we initialize the Q_learning class, it setups the Environment from _Gymnasium_ and initializes any additional data structure required for frames, statistics related to Environment.

- #### The major methods used are:

  - `Discretize`: This is a function which is used to discretize the observation space provided and remove the convert the velocity and angular velocity to a lower speed since their range included infinity.

  - `Training`: This is a method which consists of training the agent using the Q-learning algorithm. The exact formula used for the Q-learning is as follows:
    Q(s,a) = Q(s,a) + α( reward + γ(Q(s',a')) - Q(s,a) )

  - `Stats_train`: This method prints the Statistics obtained after training the agent.

  - `Testing`: This method test the Agent on the different starting states. It also takes the hyperparameter which signifies the number of times of testing. 

  - `Save_video`: This saves the video in the directory specified with respect to the local path.

### Results

- #### Finally, the agent could stay balanced upto 60-80 steps.

- #### Some of the selected videos are shown here. Others can be seen in the video directory.

- #### 46 Steps

https://github.com/udayb3/Cartpole-game-using-RL/assets/148479732/b219d3b6-7d61-423d-b2f0-765ddb87ce02

- #### 44 Steps

https://github.com/udayb3/Cartpole-game-using-RL/assets/148479732/e9664323-db0c-4392-9dc0-8055dfcef6c1

### References

- #### [Gymnasium](https://gymnasium.farama.org/)
- #### [Imageio](https://imageio.readthedocs.io/en/stable/)
- #### [Matplotlib](https://matplotlib.org/stable/index.html)

### License
- ### This project is licensed under © [Uday Bhardwaj](https://github.com/udayb3) and [Vedansh Sharma](https://github.com/Vedanshbvb).
