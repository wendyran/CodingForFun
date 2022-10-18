"""
### Introductions
The popular game "Snake" with multi-players.

There are N players. Each one has a snake. Each snake can be killed by another snake. Snakes can resurrect after died. 

We want to add some voice effect of "Revenge", if a snake kills another snake, which has killed it before. 
i.e. Snake A has killed Snake B before. When Snake B kills Snake A, we add a voice effect of "Revenge".

### Coding Question
Given N palyers (i.e. N snakes), write a program that imitates this process of having the voice effect of "Revenge". 

You can define your own class and objects. 

Input: An array of Snake killing pairs.
Output: An array of Booleans. For each element in the array, decide whether "Revenge" voice output is needed. 

e.g.

Input: 

[
    [1, 2],
    [2, 1],
    ...
    [1, 2]
]

Output:

[
    "",
    "Revenge",
    ...,
    "Revenge"
]

- Snake 1 kills Snake 2
- Snake 2 kills Snake 1 ---> "Revenge"
- ...
- Snake 1 kills Snake 2 ---> "Revenge"
"""
class SnakeGame(object):
    def __init__(self):
        self.kill_history = {}

    def kill(self, i, j):      # snake i kills snake j
        # add snake (i, j ) pair to the map 
        if i not in self.kill_history:
            self.kill_history[i] = set([j])
        else:
            self.kill_history[i].add(j)
        # check whether it qualififes as revenge 
        # (i.e. if snake j has killed snake i before)
        if j in self.kill_history and i in self.kill_history[j]:
            print("Revenge")
        else:
            print("")

'''
hashed map
set
'''

game = SnakeGame()
game.kill(3,4)
game.kill(1,2)
game.kill(2,1)
game.kill(1,2)
game.kill(4,5)
game.kill(1,2)

"""
### Followup

After a revenge, all previous killing history between these two snakes is cleared, except the one just happened that's for the 'revenge'. 

i.e. no matter how many times Snake A has killed Snake B consequtively before, as long as Snake B killed Snake A as 'Revenge', then the previous killings of Snake A to Snake B are clearly. Snake B killed Snake A is still 'On record'. 

### Coding Question
Write a pogram which output "Revenge" when needed. 

e.g.

Input: 

[
    [1, 2],
    [4, 7],
    ...
    [1, 2],
    [1, 3]
]

Output:

[
    False,
    False,
    ...,
    False,
    True
]

- Snake 1 kills Snake 2
- Snake 4 kills Snake 7
- Snake 1 kills Snake 3
- Snake 2 kills Snake 1 ---> "Revenge"
- Snake 2 kills Snake 1
- Snake 3 kills Snake 1 ---> "Revenge"
- Snake 2 kills Snake 1
- Snake 1 kills Snake 2 ---> "Revenge"
- Snake 1 kills Snake 2
- Snake 1 kills Snake 3 ---> "Revenge"
"""

class SnakeGame1(object):
    def __init__(self):
        self.kill_history = {}

    def kill(self, i, j):      # snake i kills snake j
        # add snake (i, j ) pair to the map 
        if i not in self.kill_history:
            self.kill_history[i] = set([j])
        else:
            self.kill_history[i].add(j)
        # check whether it qualififes as revenge 
        # (i.e. if snake j has killed snake i before)
        if j in self.kill_history and i in self.kill_history[j]:
            self.kill_history[j].delete(i)
            print("Revenge")
        else:
            print("")

'''
hashed map
set
'''

"""
### Follow Up
Output the ranks of players, in descending order of how many other snakes it has killed. 
"""
