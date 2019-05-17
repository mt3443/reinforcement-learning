## EECS 738 Project 4: Reinforcement Learning by Matthew Taylor

### Overview

The purpose of this project is to implement a reinforcement learning policy to model situational assessments, actions, and rewards programmatically. Multiple two-dimensional maze-like environments with goals/treasures (yellow squares), walls (black squares), and enemies (red squares) were created to test the agent (green square). Q-learning was implemented to teach the agent how to quickly obtain treasures and avoid enemies. The amount of time taken to collect all treasures and the number of enemies fought served as metrics to gauge the performance of the agent. GIFs were created for each environment to easily illustrate the agent's behavior and the efficacy of the training algorithm.

### Approach

First, the two-dimensional maze-like environments and visualization tools were created using NumPy arrays and a library called array2gif. As soon as GIFs could be created to show the movement of an agent on a two-dimensional plane, simple mazes were created with no obstacles or enemies. The initial mazes contained only the agent and a single treasure. Then, Q-learning was used to produce a path that would lead the agent directly to the treasure. This was accompmlished by giving the agent a small negative reward, or penalty, for every step taken. This was included to ensure that direct paths were taken to treasures. To indicate the yellow squares were desirable, a large positive reward was given to the agent whenever it moved to a cell containing a treasure.

Once this was accomplished, larger environments were created with walls and multiple treasures. Walls served as impassable boundaries preventing the agent from moving directly to a treasure. After the agent could avoid these obstacles and collect multiple treasures, enemies were introduced. Unlike walls, the agent could move into, or attack, these enemies. However, attacking enemies resulted in a moderate negative reward, or penalty. Doing this incentivized the agent to generally avoid enemies and attack if necessary. One can think of the agent as a pacifist. A notable test performed involved a long winding path to a treasure with no enemies and a short path directly to a treasure with one enemy. The penalties were set such that attacking this enemy and traveling directly to the treasure resulted in a lower overall cost than traversing the enemy-free path. This example illustrates the agent's dynamic learned decision making capabilities.

### How To Run

This project was written in Python 3.7.2 and requires modules that can be installed by navigating to the project directory and running this command:
```
pip3 install -r requirements.txt
```
Once the dependencies are installed, learning can commence. To train an agent, an environment size must be specified. The available sizes are 'small', 'medium', and 'large'. Optionally, the presence of enemies in each environment can be toggled by adding 'enemies' to the command. Each of the environments can used by issuing a command of this format:
```
python3 main.py <size> [enemies]
```

**Examples:**

To run the small maze with no enemies:
```
python3 main.py small
```

To run the medium maze with enemies:
```
python3 main.py medium enemies
```

**Note: It takes a very long time to train on the large mazes (with and without enemies). This has already been done and the results are shown below**

### Results

For each environment, a GIF and plot were created. The GIF graphically shows the agents path through the environment. The plot shows the number of time steps taken to collect all treasures at each episode during training. There is a general trend in each plot. They all start rather high (it takes a long time to collect all treasures initially because the agent hasn't learned how), and as training continues, the amount of time steps taken to collect all treasures decreases and eventually converges as the model learns the best path. Plots were not included for the small environments since they were so simple. Essentially no improvement was shown in the small plots.

**Small environment with no enemies:**
![](https://i.imgur.com/FdjkZI7.gif)

With no enemies or obstacles, the agent maximizes its reward by heading directly for each treasure.

**Small environment with enemies:**
![](https://i.imgur.com/8RNZwcU.gif)

To avoid the moderate penalty of fighting, the agent circumvents the enemies to collect the treasures. In this basic example, the agent essentially treats the enemies as walls. The penalty for attacking the enemies is much higher than the penalty for the few steps it takes to avoid them.

**Medium environment with no enemies:**
![](https://i.imgur.com/4yl0sSF.gif)
