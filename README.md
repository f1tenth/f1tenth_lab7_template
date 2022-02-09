# Lab 7: Motion Planning

## I. Learning Goals

- Motion Planning basic concepts
  * Configuration space vs. Workspace: you should understand the difference between configuration space and workspace, and the advantages and disadvantages of planning in each of them.
  * Free space vs. Obstacle space: you should understand the difference between free space and obstacle space.
  * Occupancy grids and Costmaps: you should understand what occupancy grids and costmaps are, how to use them, and how to create them.
- Motion Planning algorithms
  * Grid-based search: Dijkstra’s, A*, and their variants.
  * Sampling based algorithms: RRT and its variants.

## II. Overview

The goal of this lab is to provide you with tools that will help you in a head-to-head race on a race track. After finishing this lab, your car should be able to do something like [this](https://www.youtube.com/watch?v=llHCRqwIllM).

Before you start this lab, you should read the [paper](https://arxiv.org/pdf/1105.1186.pdf}{https://arxiv.org/pdf/1105.1186.pdf). Pay close attention to sections 3.1, 3.2, Algorithm 3, 3.3, Algorithm 6.

## III. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node. As per usual, test your algorithm first in the
simulator before you test it on the car. As shown in the lecture, the curvature of the arc to track
can be calculated as:

![](https://latex.codecogs.com/svg.latex?\gamma=\frac{2|y|}{L^2})

## IV. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

## V: Grading Rubric
- Compilation: **10** Points
- Occupancy grid init and update: **20** Points
- Correct collision check: **30** Points
- Correct find path: **30** Points
- Video: **10** Points
