tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5) # TypeError indicates that function or expression is taking an invalid input. In this case, tweet is a string, so + operation is a concatenation, which needs another string. But 5 is an integer, so it will raise an TypeError.