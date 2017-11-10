
# recommendationTest.py

import recommendations

itemsim = recommendations.calculateSimilarItems(recommendations.critics)

'''
recommendedList = recommendations.getRecommendedItems(recommendations.critics, itemsim, 'Toby')

print(recommendedList)
'''

prefs = recommendations.loadMovieLens()
# print prefs['87']

print 'user-based recommendations : '
recommendeduser = recommendations.getRecommendations(prefs, '87')[0:30]
print recommendeduser

print 'item-based recommendations : '
itemsim = recommendations.calculateSimilarItems(prefs, n = 50)
recommendeditems = recommendations.getRecommendedItems(prefs, itemsim, '87')[0:30]
print recommendeditems




















