from flask import Flask
import math
import json

app = Flask(__name__)


@app.route('/')
def index_file():
    # Load Document:
    documents = []
    with open('UFO - Test.json') as json_file:
        data = json.load(json_file)
        for p in data:
            print('Description: ' + p['Description'])
            documents = [p['Description']] + documents

    # Create word dictionary (Stemming/Stop words/Etc might go here):
    ufoDictionary = {}

    # This splits the various descriptions into unique words and their counts for each document
    for index, sentence in enumerate(documents):
        tokenizedWords = sentence.split(' ')
        ufoDictionary[index] = [(word, tokenizedWords.count(word)) for word in tokenizedWords]

    print(ufoDictionary)

    # Create a list of terms that are unique and have no duplicates.
    termFrequency = {}

    for i in range(0, len(documents)):
        listOfNoDuplicates = []
        for wordFreq in ufoDictionary[i]:
            if wordFreq not in listOfNoDuplicates:
                listOfNoDuplicates.append(wordFreq)
            termFrequency[i] = listOfNoDuplicates
    print("\nWords that don't appear twice:")
    print(termFrequency)

    # Create a list of tokens from all documents
    allDocuments = ''
    for sentence in documents:
        allDocuments += sentence + ' '
    allDocumentsTokenized = allDocuments.split(' ')

    print("\nTokens:")
    print(allDocumentsTokenized)

    # Use the above lists to remove duplicates and make a list of all unique terms
    allDocumentsNoDuplicates = []

    for word in allDocumentsTokenized:
        if word not in allDocumentsNoDuplicates:
            allDocumentsNoDuplicates.append(word)
    print("\nAll Unique Words:")
    print(allDocumentsNoDuplicates)

    # Count the number of times a term appears
    dictOfNumberOfDocumentsWithTermInside = {}

    for index, voc in enumerate(allDocumentsNoDuplicates):
        count = 0
        for sentence in documents:
            if voc in sentence:
                count += 1
        dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)
    print("\nCount of Terms:")
    print(dictOfNumberOfDocumentsWithTermInside)

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
    print("\nIDF Number:")
    print(dictOFIDFNoDuplicates)

    # Find tf-IDF by multiplying
    dictOFTF_IDF = {}
    for i in range(0, len(termFrequency)):
        listOFTF_IDF = []
        TFsentence = termFrequency[i]
        IDFsentence = dictOFIDFNoDuplicates[i]
        for x in range(0, len(TFsentence)):
            listOFTF_IDF.append((TFsentence[x][0], TFsentence[x][1] * IDFsentence[x][1]))
        dictOFTF_IDF[i] = listOFTF_IDF
    print("\nTF-IDF Number:")
    print(dictOFTF_IDF)


    test_tf('universe','the the universe has very many stars')
    return 'Hello World!'

def test_tf(term, text):
    newText = text.split(' ')
    print(text.count(term))
    print(len(newText))

if __name__ == '__main__':
    app.run()
