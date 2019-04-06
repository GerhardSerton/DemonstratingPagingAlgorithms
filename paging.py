# Pieter Gerhard Serton
# OS Assignment 1
import random
import sys
from collections import deque


class OS:

    def __init__(self, length=0):
        self.size = length
        self.pageNo = self.reinitializeList()
        self.referenceString = self.randomPageReferenceString()

    def printList(self):
        for x in range(0, self.size):
            print(self.pageNo[x])

    def FIFO(self, pages):
        self.referenceString = pages
        self.pageNo = self.reinitializeList()
        errors = 0
        lastOut = 0
        for x in self.referenceString:
            if x not in self.pageNo:
                errors = errors + 1
                self.pageNo[lastOut] = x
                lastOut = lastOut + 1
                if lastOut >= self.size:
                    lastOut = 0
        return errors

    def LRU(self, pages):
        self.referenceString = pages
        self.pageNo = self.reinitializeList()
        errors = 0
        lasttried = self.initializeFrequencies()
        for x in range (0, len(self.referenceString)):
            if self.referenceString[x] not in self.pageNo:
                errors = errors + 1
                biggest = 0
                yofbiggest = 0
                for y in range (0, self.size):
                    if lasttried[y] > biggest:
                        biggest = lasttried[y]
                        yofbiggest = y

                self.pageNo[yofbiggest] = self.referenceString[x]
                lasttried[yofbiggest] = 0
                for z in range (0, self.size):
                    lasttried[z] = lasttried[z] + 1
            else:
                lasttried[self.pageNo.index(self.referenceString[x])] = 0
                for z in range (0, self.size):
                    lasttried[z] = lasttried[z] + 1

        return errors

    def OPT(self, pages):
        queue = deque(pages)
        self.pageNo = self.reinitializeList()
        errors = 0
        differentPages = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        differentPagesValues = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999]
        while queue:
            currentRef = queue.popleft()
            for z in differentPages:
                if z not in queue:
                    differentPagesValues[differentPages.index(z)] = 99999
                else:
                    differentPagesValues[differentPages.index(z)] = queue.index(z)
            if currentRef not in self.pageNo:
                errors = errors + 1
                chosenPageNoIndex = 0
                highest = -1
                for x in self.pageNo:
                    if differentPagesValues[differentPages.index(x)] > highest:
                        highest = differentPagesValues[differentPages.index(x)]
                        chosenPageNoIndex = self.pageNo.index(x)

                self.pageNo[chosenPageNoIndex] = currentRef



        return errors

    def reinitializeList(self):
        newPage = []
        for x in range (0, self.size):
            newPage.append(-1)
        return newPage

    def initializeFrequencies(self):
        freq = []
        for x in range (0, self.size):
            freq.append(99999999)
        return freq

    def randomPageReferenceString(self, length = 10):
        s = []
        for x in range(0, length):
            s.append(random.randint(0, 9))

        return s

    def main(self):
        p = self.randomPageReferenceString()
        print("this shit works")
        print("FIFO", self.FIFO(p), "errors")
        print("LRU", self.LRU(p), "errors")
        print ("OPT", self.OPT(p), "errors")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
        p1 = OS(3)
        p1.main()
    else:
        if sys.argv[1] < 1 | sys.argv[1] > 7:
            print("Too many frames. Try a value between 1 and 7")
        else:
            p1 = OS(sys.argv[1])
            p1.main()
