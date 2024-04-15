# CartPole Game using Reinforcement Learning

### Hello, This project uses Reinforcement Learning to train the classic CartPole Game. The aim was to make the Pole balance for a longer period of time. 

### Table of Contents
<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText="Click to expand") -->
<details>
<summary>Index</summary>

- [Set-up](#set-up)
- [Description](#description)
- [Environment](#environment)
- [References](#references)
</details>
<!-- AUTO-GENERATED-CONTENT:END -->

### Set-up

- #### All the requirements for the code to run are provided in the `requirements.txt` file.

- #### You can install the libraries directly by running the following command locally/globally.
  > pip install -r requirements.txt

- #### You can run the `Q_learning_based` file in the python_files directory. Modify the code depending upon the episodes number, video path, result file path, etc.

### Description

- #### We have used [Gymnasium](https://gymnasium.farama.org/) which is a maintained fork of OpenAI's gym. This was done by understanding the environment and actions which were provided by the library.

- #### First, We used Q learning to train the model and test it using the Q-table values. The results were that we could make the pole stay in position for duration of 100 seconds. Here is the video which shows 58 steps taken by the CartPole.

  https://github.com/udayb3/Cartpole-game-using-RL/assets/148479732/9ec96e5a-9c38-4350-8f93-bd2c1a7ce10f


### Environment

- #### `CartPole-v_1` is used for the Reinforcement Learning algorithms.

- #### The _Observation Space_ consists of four Continuous eatures:
  1. Position (-0.5 to 0.5)
  2. Velocity ( -$\inf \; to \; \inf $ )
  3. Angle ( -0.24 to 0.24 )
  4. Angular Velocity ( -$\inf \; to \; \inf $ )

- #### The _Action Space_ consists of 2 Discrete states:
  1. 0: Pushing the cart to the left.
  2. 1: Pushing the card to the right.

- #### Reward was given everytime whenever a step was taken by the agent.

- #### There were 3 termination conditions for ending an episode
  1. Pole angle becomes greater than $ \pm12 $ degree.
  2. Position is not in the region of $\pm2.4 $.
  3. The total number of steps become more than 500 in an episode.

- #### The API of `Gymnasium` enabled us to use their methods and the above description of the environment is also explained in the detailed manner [here](https://gymnasium.farama.org/environments/classic_control/cart_pole/).

### Algorithm

### References
