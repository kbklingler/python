#! /usr/bin/env python3

Sentence = input("Enter a sentence: ")
Sentence = Sentence.lower().replace(" ", "")
print ('New Sentence:', Sentence)

NewSentenceLength = float(len(Sentence))
print ('Sentence Length:', NewSentenceLength)

