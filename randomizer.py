#!/usr/bin/env python3
# AUTHOR: Kevin Kaminski
# DATE: June 26, 2020
# DESC: Randomizer for Mario Kart setups.

import atvs
import bikes
import characters
import gliders
import karts
import wheels
from random import randrange


def randomizer():
  vehicles = atvs + bikes + karts
  build = []

  for category in [characters, gliders, vehicles, wheels]:
    build.append(category[randrange(0, category.length)])

  return build

def _main():
  p randomizer()

if __name__ == '__main__':
    _main()
