import numpy as np


# TODO: Implement the reward function as described in Gymnasium documentation.
# The end-state is always at [env_size-1,env_size-1].
def reward_function(s, env_size):
    r =  0
    if s[0] == [env_size - 1] and s[1] == [env_size - 1]: # Check if we are in the goal state
        r = 1
    return r

# do not modify this function
def reward_probabilities(env_size):
    rewards = np.zeros((env_size*env_size))
    i = 0
    for r in range(env_size):
        for c in range(env_size):
            state = np.array([r,c], dtype=np.uint8)
            rewards[i] = reward_function(state, env_size)
            i+=1

    return rewards

# Check feasibility of the new state.
# If it is a possible state return s_prime, otherwise return s
def check_feasibility(s_prime, s, env_size, obstacles):
  # TODO
    if (s_prime < env_size).all() and (s_prime >= 0).all(): # Check if we are inside the envirment
        return s_prime                                      # We can move,  let's move!
    return s                                                # We can't move , let's stay where we are! 

def transition_probabilities(env, s, a, env_size, directions, obstacles):
    prob_next_state = np.zeros((env_size, env_size))

    # TODO
    # Fill in the cells corresponding to the next possible states with the probability of visiting each of them
    # Remember to check the feasibility of each new state!

    s_prime = check_feasibility(s + directions[a], s , env_size, obstacles) # Check if the action is feasible or nor
    prob_next_state[s_prime[0],s_prime[1]] += 1/3    # update the probability to end in the next state
    
    s_prime = check_feasibility(s + directions[(a+1) % 4], s , env_size, obstacles)  # Check if the action is feasible or nor
    prob_next_state[s_prime[0],s_prime[1]] += 1/3    # update the probability to end in the next state

    s_prime = check_feasibility(s + directions[(a+3) % 4], s , env_size, obstacles)  # Check if the action is feasible or nor
    prob_next_state[s_prime[0],s_prime[1]] +=1/3     # update the probability to end in the next state



    return prob_next_state