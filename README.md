# Basic Reinforcement Learning agent

## Problem Formulation 

We have to set the value at each states / block of the grid and use it to determine the path. Initially the
agent should explore more and then gradually it would exploit more. This is ensured as we are using
boltzman distribution, an exponential function will find the probability. As the power of e increases,
the higher probability would become even higher. Thus, as we proceed with each successive iteration,
we try to exploit more.


Notice that the actions that we are performing are left , right , up and down. However, it has a
constraint i.e., it cannot pass through a barrier or a block which is represented with black squares.
Another constraint is that the journey of the agent cannot exceed maximum number of steps and a
counter is used to keep note of that. Sinking states (red and green) also ensure that the journey ends.
Red state has a reward of -100, Green state has a reward of 100 and white state has no reward
Value is the amount of reward an agent can expect to accumulate over the future and its value is
updated after every action since we are asked to implement Temporal Difference
Thus we update the values on every action.


Gamma or discounting factor is 0.8. Larger gamma means care more about long term reward.

## Visualization of learned policy

![image](https://user-images.githubusercontent.com/110885397/235712135-03dbb61f-3e8b-466f-9ba3-827b9c8584df.png)
![image](https://user-images.githubusercontent.com/110885397/235712214-7c8a2b36-5ccf-487f-8b84-06196b3ec3ab.png)

## Adjustable grid configuration 
As soon as you start the code, it asks you whether or not you need a pre-built grid. Upon receiving
the input, it then makes the map randomly as per the following probability:
Probability of white path: 0.85
Probability of green sink state: 0.05
Probability of red sink state: 0.05
Probability of path hurdle / block / black square: 0.05

![image](https://user-images.githubusercontent.com/110885397/235712452-ef146c19-0a6b-451d-9648-7f60e09d4a72.png)

## Convergence of value function

The video shows how in the fixed grid, value function converged eventually. In the beginning we
explore more, then, eventually, since we are using Boltzmann distribution, therefore, it moves towards
the path with greater probability.

You can see that the random grid values soon converges to the shortest path towards the green state.

https://www.youtube.com/watch?v=RggXEOuYRRQ
