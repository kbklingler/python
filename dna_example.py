#! /usr/bin/env python3
DNASeq = input("Enter a DNA sequence: ")
DNASeq = DNASeq.upper().replace(" ", "")
print ('Sequence:', DNASeq)

SeqLength = float(len(DNASeq))
print ('Sequence Length:', SeqLength)

NumberA = DNASeq.count('A')
NumberC = DNASeq.count('C')
NumberG = DNASeq.count('G')
NumberT= DNASeq.count('T')

print ("A:", NumberA/SeqLength)
print ("C:", NumberC/SeqLength)
print ("G:", NumberG/SeqLength)
print ("T:", NumberT/SeqLength)

print ("There are %d A bases." % (NumberA))
print ("There are %d C bases." % (NumberC))
print ("There are %d G bases." % (NumberG))
print ("There are %d T bases." % (NumberT))

print ("A occurs in %d bases out of %d." % (NumberA, SeqLength))
print ("C occurs in %d bases out of %d." % (NumberC, SeqLength))
print ("G occurs in %d bases out of %d." % (NumberG, SeqLength))
print ("T occurs in %d bases out of %d." % (NumberT, SeqLength))

print ("A occurs in %.1f%% of %d bases." % (100 * NumberA/SeqLength, SeqLength))
print ("C occurs in %.1f%% of %d bases." % (100 * NumberC/SeqLength, SeqLength))
print ("G occurs in %.1f%% of %d bases." % (100 * NumberG/SeqLength, SeqLength))
print ("T occurs in %.1f%% of %d bases." % (100 * NumberT/SeqLength, SeqLength))

