#!/usr/bin/python2

input = ''
with open('input.txt') as f:
    for line in f:
        input += line

sentences = input.split('.')
map = {}

for sentence in sentences:
    words = sentence.split(' ')
    index = 0
    while index < len(words):
        pass
