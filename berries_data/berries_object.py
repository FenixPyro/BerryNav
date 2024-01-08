"""Módulo donde definimos la clase Berry, que contendrá todas sus características"""
from berries_attributes import get_berry_description
from berries_attributes import get_berry_flavors
from berries_attributes import get_berry_natural_gift
from berries_attributes import get_berry_growthtime
from berries_sprites import get_berry_sprite


class Berry:
    def __init__ (self, name):
        self.name = name
        self.flavor = None
        self.natural_gift = None
        self.description = None
        self.sprite = None
        self.growth_time = None
    
    # def get_flavor(self):
    #     self.flavor = get_berry_flavors(self.name)
    #     return self.flavor
   
    # def get_natural_gift(self):
    #     self.natural_gift = get_berry_natural_gift(self.name)
    #     return self.natural_gift
    
    # def get_description(self):
    #     self.description = get_berry_description(self.name)
    #     return self.description
   
    # def get_sprite(self):
    #     self.sprite = get_berry_sprite(self.name)
    #     return self.sprite
   
    # def get_growth_time(self):
    #     self.growth_time = get_berry_growthtime(self.name)
    #     return self.growth_time  
    def get_all(self):
        self.flavor = get_berry_flavors(self.name)
        self.natural_gift = get_berry_natural_gift(self.name)
        self.description = get_berry_description(self.name)
        self.sprite = get_berry_sprite(self.name)
        self.growth_time = get_berry_growthtime(self.name)
        return self.flavor, self.natural_gift, self.description, self.sprite, self.growth_time
