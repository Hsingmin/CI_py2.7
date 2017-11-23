
# optimizationtest.py

import optimization

domain = [(0,9)]*(len(optimization.people)*2)

# hillclimb algorithm
'''
s = optimization.hillclimb(domain, optimization.schedulecost)

print('hillclimb algorithm -- schedulecost : ' )
print(optimization.schedulecost(s))

optimization.printschedule(s)
'''

'''
# annealing algorithm
s = optimization.annealingoptimize(domain, optimization.schedulecost)

print('annealing algorithm -- schedulecost : ' )
print(optimization.schedulecost(s))

optimization.printschedule(s)
'''
print('---- genetic optimization algorithm ----')
s = optimization.geneticoptimize(domain, optimization.schedulecost)
print(s)

optimization.printschedule(s)


























