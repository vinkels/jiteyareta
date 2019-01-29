from mesa import Agent
import random as rd


class Food(Agent):
    def __init__(self, model, pos, util_pars=(5, 2.5)):
        super().__init__(model.next_id(), model)

        self.pos = pos
        #TODO SET HIGHER PARAMETER FOR RANDOMNESS 
        self.max_util = rd.randint(1, 10)
        #TODO GENERATE RANDOMNESS BETWEEN 1 AND MAX_UTIL CHANGE THIS IN MODEL.PY
 
        # self.util = rd.randint(1, self.max_util)
        self.max_util = np.random.normal(util_pars[0], util_pars[1])
        self.steps = 0

    def step(self):
        #TODO CHANGE STEPCOUNT  AND ADD THIS VARIABLE IN CONFIG
        if self.steps % 3 == 0:
            if self.util < self.max_util:
                self.util += 1

        self.steps += 1


    def get_eaten(self):
        #TODO THIS SHOULD DEPENDENT ON CARRYING CAPACITY OF BEES. 
        self.util -= 1
