
# optimizationtest.py

import optimization
import dorm

# domain = [(0,9)]*(len(optimization.people)*2)

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

'''
print('---- genetic optimization algorithm ----')
s = optimization.geneticoptimize(domain, optimization.schedulecost)
print(s)

optimization.printschedule(s)
'''

s = optimization.randomoptimize(dorm.domain, dorm.dormcost)
print 'random optimize dormcost = ', dorm.dormcost(s)
dorm.printsolution(s)

s = optimization.geneticoptimize(dorm.domain, dorm.dormcost)
print 'genetic optimize dormcost = ', dorm.dormcost(s)
dorm.printsolution(s)


























