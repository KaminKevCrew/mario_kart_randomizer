#!/usr/bin/env python3
# AUTHOR: Kevin Kaminski
# DATE: June 26, 2020
# DESC: Randomizer for Mario Kart setups.


from characters import characters
from gliders import gliders
from vehicles import vehicles
from wheels import wheels
from random import randrange


def randomizer():
  build = []

  for category in [characters, gliders, vehicles, wheels]:
    build.append(category[randrange(0, len(category))])

  return build

def _main():
  print(randomizer())

if __name__ == '__main__':
    _main()
