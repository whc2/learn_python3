#!/usr/bin/env python3
# -*- coding: utf-8  -*-

__author__ = 'Martin Wang'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integer', type = int, help = 'display an integer')
args = parser.parse_args()

print (args.integer)
