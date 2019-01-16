from mesa import Model
from mesa import Agent
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

import random as rd

from food import Food
from bee import Bee
from hive import Hive
from obstacle import Obstacle

from schedule import RandomActivationBeeWorld

class BeeForagingModel(Model):
    def __init__(self, width, height):
        super().__init__()
        self.height = height
        self.width = width

        self.grid = MultiGrid(self.width, self.height, torus=False)

        self.schedule = RandomActivationBeeWorld(self)

        # Init Hive
        hive = Hive(self, (0,0))
        self.hive = hive
        self.add_agent(self.hive, (0, 0))

        # Init Bees
        for i in range(0, 20):
            bee = Bee(self, self.hive.pos, self.hive, "scout")
            self.add_agent(bee, self.hive.pos)

            bee_for = Bee(self, self.hive.pos, self.hive, "rester")
            self.add_agent(bee_for, self.hive.pos)

        #Init obstacle
        obs_position = (rd.randrange(self.width),rd.randrange(self.height))
        obstacle = Obstacle(unique_id=self.next_id(), model=self, pos=obs_position)
        
        self.grid.place_agent(obstacle, obs_position)


        for obs_position in [(3, 1), (3, 2), (3, 3), (2, 3), (1, 3)]:
            obstacle = Obstacle(unique_id=self.next_id(), model=self, pos=obs_position)
            self.grid.place_agent(obstacle, obs_position)
        

        # Init Food
        for i in range(0, 10):
            loc1 = rd.randint(0, width - 1)
            loc2 = rd.randint(0, height - 1)
            food = Food(self, (loc1,loc2), rd.randint(1, 4))
            self.add_agent(food, (loc1, loc2))

        

        self.datacollector = DataCollector({
            "Bees": lambda m: m.schedule.get_breed_count(Bee),
            "HiveFood": lambda m: m.hive.get_food_stat(),
            "Scout bees": lambda m: m.schedule.get_scout_count()[0],
            "Foraging bees": lambda m: m.schedule.get_scout_count()[1],
            "Rester bees": lambda m: m.schedule.get_scout_count()[2]
        })
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def add_agent(self, agent, pos):
        self.grid.place_agent(agent, pos)
        self.schedule.add(agent)

    def remove_agent(self, agent):
        self.grid.remove_agent(agent)
        self.schedule.remove(agent)

    def add_bee(self, pos, hive, type_bee):
            bee = Bee(self, pos, hive, type_bee)
            self.add_agent(bee, pos)