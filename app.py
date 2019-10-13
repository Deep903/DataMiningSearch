from flask import Flask, render_template, request
import math
import json

app = Flask(__name__)

documents = []
with open('UFO.json') as json_file:
    data = json.load(json_file)
    for p in data:
        # print('Description: ' + p['Description'])
        documents = [p['Description']] + documents
import pickle

f = open('indexed.pckl', 'rb')
dictOFTF_IDF = pickle.load(f)
f.close()


@app.route('/')
def my_form():
    return render_template('base.html')


@app.route('/', methods=['POST'])
def index_file():
    query = request.form['text']
    print(query)
    # Load Document:
    ''' documents = []
    with open('UFO.json') as json_file:
        data = json.load(json_file)
        for p in data:
            # print('Description: ' + p['Description'])
            documents = [p['Description']] + documents
    '''
    '''
    # Create word dictionary (Stemming/Stop words/Etc might go here):
    ufoDictionary = {}

    # This splits the various descriptions into unique words and their counts for each document
    for index, sentence in enumerate(documents):
        sentence = str(sentence)
        print(sentence)
        tokenizedWords = sentence.split(' ')
        ufoDictionary[index] = [(word, tokenizedWords.count(word)) for word in tokenizedWords]

    #print(ufoDictionary)

    # Create a list of terms that are unique and have no duplicates.
    termFrequency = {}

    for i in range(0, len(documents)):
        listOfNoDuplicates = []
        for wordFreq in ufoDictionary[i]:
            if wordFreq not in listOfNoDuplicates:
                listOfNoDuplicates.append(wordFreq)
            termFrequency[i] = listOfNoDuplicates
    #print("\nWords that don't appear twice:")
    #print(termFrequency)

    # Create a list of tokens from all documents
    allDocuments = ''
    for sentence in documents:
        allDocuments += str(sentence) + ' '
    allDocumentsTokenized = allDocuments.split(' ')

    #print("\nTokens:")
    #print(allDocumentsTokenized)

    # Use the above lists to remove duplicates and make a list of all unique terms
    allDocumentsNoDuplicates = []

    for word in allDocumentsTokenized:
        if word not in allDocumentsNoDuplicates:
            allDocumentsNoDuplicates.append(word)
    #print("\nAll Unique Words:")
    #print(allDocumentsNoDuplicates)

    # Count the number of times a term appears
    dictOfNumberOfDocumentsWithTermInside = {}

    for index, voc in enumerate(allDocumentsNoDuplicates):
        count = 0
        for sentence in documents:
            if voc in str(sentence):
                count += 1
        dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)
    #print("\nCount of Terms:")
    #print(dictOfNumberOfDocumentsWithTermInside)

    # Find IDF
    dictOFIDFNoDuplicates = {}
    for i in range(0, len(termFrequency)):
        listOfIDFCalcs = []
        for word in termFrequency[i]:
            for x in range(0, len(dictOfNumberOfDocumentsWithTermInside)):
                if word[0] == dictOfNumberOfDocumentsWithTermInside[x][0]:
                    listOfIDFCalcs.append(
                        (word[0], math.log(len(documents) / dictOfNumberOfDocumentsWithTermInside[x][1])))
        dictOFIDFNoDuplicates[i] = listOfIDFCalcs
    #print("\nIDF Number:")
    #print(dictOFIDFNoDuplicates)

    # Find tf-IDF by multiplying
    dictOFTF_IDF = {}
    for i in range(0, len(termFrequency)):
        listOFTF_IDF = []
        TFsentence = termFrequency[i]
        IDFsentence = dictOFIDFNoDuplicates[i]
        for x in range(0, len(TFsentence)):
            listOFTF_IDF.append((TFsentence[x][0], TFsentence[x][1] * IDFsentence[x][1]))
        dictOFTF_IDF[i] = listOFTF_IDF
    #print("\nTF-IDF Number:")
    #print(dictOFTF_IDF)

    import pickle

    f = open('indexed.pckl', 'wb')
    pickle.dump(dictOFTF_IDF, f)
    f.close()
    '''
    '''import pickle
    f = open('indexed.pckl', 'rb')
    dictOFTF_IDF = pickle.load(f)
    f.close()'''

    topDocIndex = search_term_index(query, dictOFTF_IDF)
    topDocScore = search_term_score(query, dictOFTF_IDF)
    # for k in enumerate(topDocIndex):
    # print(documents[k[1]])
    # for j in topDocScore:
    # print(j[1])
    # print(documents[topDocIndex[0]])
    # print(topDocScore[0][1])
    #score1 = str(topDocScore[0][1])

    return '''
    <html>
        <head>
            <title>Home Page - UFO Search</title>
        </head>
        <body>
        <h1>''' + query + '''</h1>
        <hr>
            <h3>''' + documents[topDocIndex[0]] + '''</h3>
            <h4>''' + str(topDocScore[0][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[1]] + '''</h3>
            <h4>''' + str(topDocScore[1][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[2]] + '''</h3>
            <h4>''' + str(topDocScore[2][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[3]] + '''</h3>
            <h4>''' + str(topDocScore[3][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[4]] + '''</h3>
            <h4>''' + str(topDocScore[4][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[5]] + '''</h3>
            <h4>''' + str(topDocScore[5][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[6]] + '''</h3>
            <h4>''' + str(topDocScore[6][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[7]] + '''</h3>
            <h4>''' + str(topDocScore[7][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[8]] + '''</h3>
            <h4>''' + str(topDocScore[8][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[9]] + '''</h3>
            <h4>''' + str(topDocScore[9][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[10]] + '''</h3>
            <h4>''' + str(topDocScore[10][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[11]] + '''</h3>
            <h4>''' + str(topDocScore[11][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[12]] + '''</h3>
            <h4>''' + str(topDocScore[12][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[13]] + '''</h3>
            <h4>''' + str(topDocScore[13][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[14]] + '''</h3>
            <h4>''' + str(topDocScore[14][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[15]] + '''</h3>
            <h4>''' + str(topDocScore[15][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[16]] + '''</h3>
            <h4>''' + str(topDocScore[16][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[17]] + '''</h3>
            <h4>''' + str(topDocScore[17][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[18]] + '''</h3>
            <h4>''' + str(topDocScore[18][1]) + '''</h4>
            
            <h3>''' + documents[topDocIndex[19]] + '''</h3>
            <h4>''' + str(topDocScore[19][1]) + '''</h4>
            
        </body>
    </html>'''


def search_term_index(term, dicOFTF_IDF):
    # Will take the term, break it up into tokens. Find the TF_IDF of each term and return index of the best doc

    # Tokenize term
    wordsList = term.split(" ")
    # print('\nWordslist:')
    # print(wordsList)

    scoresOfDocs = {}
    for index, words in enumerate(dicOFTF_IDF):
        scoresOfDocs[index] = 0;
        # i represents number of words in each doc.
        for i in range(0, len(dicOFTF_IDF[index])):
            # The below prints all words
            # print(dicOFTF_IDF[index][i][0])

            # The below prints all scores
            # print(dicOFTF_IDF[index][i][1])
            # print("\n")
            for x, terms in enumerate(wordsList):
                if wordsList[x] == (dicOFTF_IDF[index][i][0]):
                    scoresOfDocs[index] += (dicOFTF_IDF[index][i][1])
    # print(scoresOfDocs)
    indexArray = sorted(range(len(scoresOfDocs)), key=lambda k: scoresOfDocs[k])[-20:]
    indexArray.reverse()
    # print(indexArray)
    return indexArray


def search_term_score(term, dicOFTF_IDF):
    # Will take the term, break it up into tokens. Find the TF_IDF of each term and return the score of the best doc.

    # Tokenize term
    wordsList = term.split(" ")
    # print('\nWordslist:')
    # print(wordsList)

    scoresOfDocs = {}
    for index, words in enumerate(dicOFTF_IDF):
        scoresOfDocs[index] = 0;
        # i represents number of words in each doc.
        for i in range(0, len(dicOFTF_IDF[index])):
            # The below prints all words
            # print(dicOFTF_IDF[index][i][0])

            # The below prints all scores
            # print(dicOFTF_IDF[index][i][1])
            # print("\n")
            for x, terms in enumerate(wordsList):
                if wordsList[x] == (dicOFTF_IDF[index][i][0]):
                    scoresOfDocs[index] += (dicOFTF_IDF[index][i][1])
    topDocScores = sorted(scoresOfDocs.items(), key=lambda u: u[1], reverse=True)
    # print(topDocScores)
    indexArray = sorted(range(len(scoresOfDocs)), key=lambda k: scoresOfDocs[k])[-20:]
    indexArray.reverse()
    # print(indexArray)
    return topDocScores


if __name__ == '__main__':
    app.run()
