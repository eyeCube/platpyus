# func.py
# various independent global functions

# flatten:
# reduces an iterable down to one layer.
# recursively check each item in the iterable.
# if any items in the root iterable are themselves iterable,
# then split those items and add them into the root iterable.
def flatten(*args):
    ans = []
    for arg in args:
        if hasattr(arg, '__iter__'):
            ans.extend(flatten(*arg))
        else:
            ans.append(arg)
    return ans

# sign: returns 1 or -1 (positive or negative)
def sign(value):
    return 1 if value >= 0 else -1
