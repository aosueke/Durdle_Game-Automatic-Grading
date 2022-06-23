import random
def durdle_match(guess, target):
    '''
    Purpose:
        Determines which letters in the user's guess match the target
    Parameters:
        guess - a 5-letter string representing the user's guess
        target - a 5-letter string representing the target word
    Return Value:
        A 5-letter string, where each letter represents whether or not
        the letter in that position is correct.  'B' means the letter
        is not present in the target, 'Y' means that it's present in
        a different location, 'G' means it's in the correct location.
    '''
    matches = ''
    for i in range(5):
        if guess[i] not in target:
            matches += 'B'
        elif guess[i] == target[i]:
            matches += 'G'
        else:
            matches += 'Y'
    return matches
# Problem A
def get_word_list(filename):
    '''
    Purpose:
        Return a list of all 5-letter words (in strings) from a file, in the exact order it is found in the file
    Parameters:
        filename - string representing text file's name
    Return Value:
        List of strings of all words from the file in order
    '''
    fp_content = open(filename) # contains a list of acceptable 5-letter words for the Durdle game (one word per line)
    fp_content_removed_newline = [] # removes newline character from each line except from the last, before adding the word to the list
    for line in fp_content:
        file_list = line.replace('\n','')
        fp_content_removed_newline.append(file_list)

    fp_content.close()
    return fp_content_removed_newline

# Problem B
def durdle_game():
    '''
    Purpose:
        Lets the user play a game where they try to match a target word
    Parameters:
        None
    Return Value:
        The number of guesses it took the user to get the correct word.
    '''
    print("Welcome to Durdle!")
    guess = ''
    count = 0
    valid_words = get_word_list('words_full.txt')
    target = random.choice(valid_words) # choose a random target word from words found in valid_words list
    while guess != target:
        guess = input("Enter a guess:")
        if guess in valid_words: #check if the guess is in valid_words list
            print('              '+durdle_match(guess, target))
        else:
            print("Invalid guess,try it again")
        count += 1
    print("Congratulations, you got it in",count,"guesses!")
    return count

# Problem C
def grade_quiz(filename):
    '''
    Purpose:
        Grade students' scores on quiz (3 questions)
    Parameters:
        filename - string representing students' text file name (the contents of this file wile be graded in the function)
    Return Value:
        List of 3 scores based on the 3 answers found in the students' text files
    '''
    try:
        student_score = []
        with open(filename) as fp:
            # for loop to loop through the possibly number of points (i) of
            for i,line in enumerate(fp) :
                # line = lines[i]
                # if i < len(lines):
                # line = lines[i]
                line2 = line.strip()
                if i == 0 and line2 not in ['\n','']: # if 0 points and line2 is empty
                    if str(line2) == '42': # correct answer
                        student_score.append(2) # the number of points they recieved if answer is right or wrong
                    else:
                        student_score.append(1)
                elif i == 1 and line2 not in ['\n','']: # if 1 point and line2 is not empty
                    if str(line2) == 'Belgium': # correct answer
                        student_score.append(2)
                    else:
                        student_score.append(1)
                elif i == 2 and line2 not in ['\n','']: # if 2 points and line2 is not empty
                    if str(line2) == 'Towel': # correct answer
                        student_score.append(2)
                    else:
                        student_score.append(1)
                else:
                    student_score.append(0)
            for k in range(3 - len(student_score)):
                    student_score.append(0)

            if len(student_score) < 3:
                student_score = student_score[0:3]

            return student_score
    except FileNotFoundError:
        return [0,0,0]
# Problem D
def grade_all(grade_file):
    '''
    Purpose:
        Automatically find and input the name and grades of each student (using grade_quiz function to grade)
    Parameters:
        grade_file - string representing gradebook file (the contents of this file will be organized/ grades will automatically be inputted)
    Return Value:
        none (However,this function creates an updated version of the gradebook ("updated_gradebook1.csv", for example))
    '''
    grade_f = open(grade_file, 'r')
    remove_firstline = grade_f.readline()
    blank_data = grade_f.read()
    blank_data_list = blank_data.split('\n')
    grade_f.close()


    blank_data_list_lwr = []
    for x in blank_data_list:
        blank_data_list_lwr.append(x.lower())

    updated_grade_f = open(f'updated_{grade_file}', 'a')
    updated_grade_f.write('First Name,Last Name,Q1 Grade,Q2 Grade,Q3 Grade'+'\n')

    for rec in blank_data_list_lwr:
        if len(rec) > 1:
            rec = rec.split(',')
            student_file = f'{rec[0]}_{rec[1]}.txt' # student filename, idk if str fmt is right
            student_score = grade_quiz(student_file)
            student_score_str = [str(student_score[0]),str(student_score[1]),str(student_score[2])]
            student_score_str_joined = ','.join(student_score_str) # comma-separated score str

            updated_grade_f.write(f'{rec[0].title()},{rec[1].title()},{student_score_str_joined}\n')

    updated_grade_f.close()
