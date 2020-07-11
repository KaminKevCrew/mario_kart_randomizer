#!/usr/bin/env python3
# AUTHOR: Kevin Kaminski
# DATE: June 26, 2020
# DESC: Randomizer for Mario Kart setups.


from characters import characters
from karts import karts
from atvs import atvs
from bikes import bikes
from wheels import wheels
from gliders import gliders
from random import randrange


def randomizer():
  build = []
  category_list = []
  print("Please select the categories you would like to randomize: ")
  print("Separate selections with space: all charaters karts bikes atvs wheels gliders")

  user_input = input()
  selection = user_input.split(" ")

  vehicles = karts + atvs + bikes + atvs

  category_dict = {
    "all": [characters, vehicles, wheels, gliders],
    "characters": [characters],
    "karts": [karts],
    "bikes": [bikes],
    "atvs": [atvs],
    "wheels": [wheels],
    "gliders": [gliders]
  }

  for item in selection:
    if item in category_dict:
      category_list += category_dict[item]

  for category in category_list:
    build.append(category[randrange(0, len(category))])

  return build

def _main():
  print(randomizer())

if __name__ == '__main__':
    _main()
