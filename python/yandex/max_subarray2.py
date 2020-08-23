def maxsum(iterable):
    maxsofar = 0
    maxendinghere = 0
    for x in iterable:
        maxendinghere = max(maxendinghere + x, 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar
