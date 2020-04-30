"""
Alexander Christopher
abc5885@psu.edu
CMPSC 101
Final Project: A Simple Quiz
"""
import os, random
    
def listFiles():
    current = os.getcwd()
    listReadableFiles = os.listdir(current)
    returnFiles = []
    for i in range(len(listReadableFiles)):
        display = listReadableFiles[i]
        if display.endswith('.txt'):
            returnValue = displayReplace(display)
            returnFiles.append(returnValue)
    final = " | "
    final = final.join(returnFiles)
    return final

def displayReplace(display):
    string = display.replace('.txt','')
    return string

def retrieveFileName():
    while True:
        print(listFiles())
        ask = input('Which quiz would you like to take? ')
        select = ask + '.txt'
        if os.path.isfile(select):
            print("This will ask about " + ask +'!')
            return select
        else:
            print('Sorry, your response was not valid.')

def formatData():
    fileName = retrieveFileName()
    file = open(fileName, 'r')
    createData = []
    for line in file:
        createData.append(retrieveData(line))
    file.close()
    return createData

def retrieveData(line):
    splitLine = line.split('/')
    formatAnswer = splitLine[1].replace('\n', '')
    question = splitLine[0]
    return question, formatAnswer

def pickQuestions():
    questionBank = formatData()
    randomizedQuestion = random.sample(questionBank, len(questionBank))
    score = 0
    incorrect = 0
    recordIncorrect = []
    numberOfQuestions = int(len(randomizedQuestion) // 1.5)
    for i in range(1, numberOfQuestions + 1):
        print('Question ' + str(i) + ':')
        print(randomizedQuestion[i][0])
        correctAnswer = randomizedQuestion[i][1]
        userAnswer = input('Enter Answer Here: ')
        if userAnswer == '':
            compareAnswers = False
            print('No response was given, the correct answer was ' + correctAnswer + '!')
            print('')
        else:
            compareAnswers = checkAnswer(correctAnswer, userAnswer)
        if compareAnswers == True:
            score += 1
        elif compareAnswers == False:
            recordIncorrect.append(i)
            incorrect += 1
            
    return score, recordIncorrect, numberOfQuestions, incorrect

def checkAnswer(correctAnswer, userAnswer):
    FirstLetter = userAnswer[0]
    UpperFirstLetter = userAnswer[0].upper()
    formatUserAnswer = userAnswer.replace(FirstLetter,UpperFirstLetter, 1)
    if correctAnswer == formatUserAnswer:
        print('Correct! ' + str(correctAnswer) + ' is the right answer.')
        print('')
        return True
    else:
        print('Incorrect! The correct answer is ' + str(correctAnswer))
        print('')
        return False

def endOfQuiz():
    results = pickQuestions()
    score = results[0]
    numberOfIncorrect = results[3]
    incorrect = results[1]
    incorrect = formatIncorrect(incorrect)
    totalQuestions = results[2]
    print('You scored a ' + str(score) + '/' + str(totalQuestions) + '!')
    print(f'Your grade is a {percentage(score, totalQuestions):.0f}%')
    if numberOfIncorrect != 0:
        print('You got question(s)', incorrect, 'wrong.')
    else:
        print('You got a perfect score!')
    
    
def formatIncorrect(incorrect):
    formatting = str(incorrect)
    formatting = formatting.replace('[', '')
    formatting = formatting.replace(']', '')
    return formatting

def percentage(score, totalQuestions):
    percent = (score/totalQuestions) * 100
    return percent

def repeatQuiz():
    while True:
        print("")
        print('Would you like take another quiz?')
        print('Type anything to continue or press enter to quit')
        askUser = input('Enter: ')
        if askUser != '':
            endOfQuiz()
        else:
            break


if __name__ == "__main__":
    endOfQuiz()
    repeatQuiz()
    
    
