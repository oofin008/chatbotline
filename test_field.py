#test DICT python

def main():
    final_message = []
    words = ['drat','crap','sucks']
    counter = 0
    userInput = input("Enter The Sentense: ")  # use raw_input if you're using python2.X
    truncatedInput = userInput[:140]
    sentence =  truncatedInput.split()
    for word in sentence:
        if word in words:
            word = 'x' * len(word)
        final_message.append(word)
    print (' '.join(final_message))

if __name__ == '__main__':
    main()
