from maze_env import Maze
from RL_brain import QLearningTable


def updata():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()
            # RL choose action based on observation
            action = RL.choose_action(str(observation))
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)
            # RL learn from the transition
            RL.learn(str(observation, action, reward, str(observation_)))
            # swap observation
            observation = observation_
            # break the while loop if this turn is done
            if done:
                break

    print("Game Over")
    env.destory()


if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, updata)
    env.mainloop()
