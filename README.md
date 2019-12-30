# QLearningExample
This is an example of q-learning

# Libraries Used
- numpy
- pandas
- pygame

# How To Run
- run the command 'python3 game.py'

# How It Works
- The object of the game is for the blue circle to make its way to the yellow circle
- The red circles indicate barriers that the blue circle is not allowed to run into; if it does, it must restart
- The numbers indicate the current max value in the Q-Table for that state

# Tips
- To slow down the learning, simply pass a slower FPS value into the initialization of the 'game' variable (i.e. game = Game(30))
- You can stop the program and it will write the values in the Q-table to a file called qtable.npy and will reuse this file when the program starts again
- To complete reset learning, delete the qtable.npy file