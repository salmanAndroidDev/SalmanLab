def correctify_word(word):

    for character in word:
          if not character.isalnum():
              word = word.replace(character,'')
    return word


def encode(text):
    words =text.replace('\n',' ').split()

    dic_words = {}
    numbers = []
    counter = 1

    for word in words:
        selected_word = word

        if not word.isalnum():
            selected_word = correctify_word(word)
        
        if selected_word == '':
            continue

        if not selected_word in dic_words:
            dic_words[selected_word] = counter
            numbers.append(counter)        
            counter += 1
        
        else:
            numbers.append(dic_words.get(selected_word))
    
    return dic_words, numbers
