if 'bird' in 'How could a 5-ounce bird possibly carry a 1-pound coconut?':
    print 'Found'
else:
    print 'Not found'

if 'cat' in 'How could a 5-ounce bird possibly carry a 1-pound coconut?':
    print 'Found'
else:
    print 'Not found'

monty_python_quote = 'How could a 5-ounce bird possibly carry a 1-pound coconut?'
search_term = 'coconut'

if search_term in monty_python_quote:
    print 'Found ' + search_term
else:
    print search_term + 'Not found'

# Expected: Found coconut# Example 4
# For case insensitive searching, make sure your needle and haystack are all lowercase.
monty_python_quote = 'How could a 5-ounce bird possibly carry a 1-pound coconut?'
search_term = 'Coconut'

# Convert needle and haystack into lowercase
monty_python_quote = monty_python_quote.lower()
search_term = search_term.lower()

if search_term in monty_python_quote:
    print 'Found ' + search_term
else:
    print search_term + 'Not found'

# Expected: Found coconut
