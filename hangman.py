import random



hangman_mainboard = '''

    |----------------------
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |   


'''
hangman_with_head = '''
    
    |----------------------
    |           |                      
    |         __|__  
    |        /     \ 
    |        \_____/
    |          
    |         
    |          
    |         
    |
'''

empty_word = []
hangman_words = {
    "Easy": ['cat', 'dog', 'fish', 'bird', 'tree'],
    "Medium": ['python', 'programming', 'computer', 'science', 'engineering'],
    "Hard": ['encyclopedia', 'hippopotamus', 'rhinoceros', 'pneumonoultramicroscopicsilicovolcanoconiosis']
}

def guessing_sequence():
    for i in range(len(random_easy)):
        empty_word.append("_ ")
    
    if letter in random_easy:
        index_pos = random_easy.index(letter)
        empty_word[index_pos] == letter
        
    else:
        print(hangman_with_head)

  




while True:
   
    start_screen = int(input("Welcome to Hangman!!\n" \
        "What difficulty would you like to play\n" \
        "1.Easy\n" \
        "2.Medium\n" \
        "3.Hard\n"
        "Enter here: "))
 
    
    if start_screen == 1:
        
    
        random_easy = random.choice(hangman_words['Easy'])
        

        print(hangman_mainboard)
        letter = input("Guess a letter: ")
        guessing_sequence()
        print(empty_word)
    
    
    
    break 
    