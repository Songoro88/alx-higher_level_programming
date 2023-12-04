#!/usr/bin/python3
Multiple_Returns = __import__('8-multiple_returns').Multiple_Returns

Sentence = "At school, I learnt C!"
Length, First = Multiple_Returns(Sentence)
print("Length: {:d} - First character: {}".Format(Length, First))
