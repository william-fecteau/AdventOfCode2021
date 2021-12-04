from utils.aoc_utils import AOCDay, day

@day(3)
class Day3(AOCDay):
    def common(self):
        # Get the lenght of one binary number (Assuming all numbers have same length)
        self.binLength = len(self.inputData[0])
        
        # Creating a list with lists containing every bit in that position
        self.bitLists = [[] for i in range(self.binLength)]
        
        for line in self.inputData:
            for i in range(self.binLength):
                # index 0 will contain the less significant bit (LSB)
                self.bitLists[i].append(int(line[i]))
        
        self.mostCommonBitInLst = self.compareBits(self.bitLists)


    # Return a list with the most common bit for each position in the array
    def compareBits(self, bitLists):
        result = []
        
        for bitLst in bitLists:
            nbOne = sum(bitLst)
            nbZero = len(bitLst) - nbOne

            if (nbOne > nbZero): 
                result.append(1)
            else:
                result.append(0)
        
        return result

    def part1(self):        
        # Looping through list in reverse because index 0 is LSB
        strEpsilon = ''.join([str(x) for x in self.mostCommonBitInLst[::-1]])
        
        # Inverting 0s and 1s for gamma
        strGamma = ''.join(['1' if i == '0' else '0' for i in strEpsilon])
        
        return int(strEpsilon, 2) * int(strGamma, 2)

    def column(self, matrix, i):
        # Too lazy to learn numpy
        return [row[i] for row in matrix]
    
    def evaluateCriteria(self, inputMatrix, isLeastCommon):
        columnToCheck = self.column(inputMatrix, 0)
        nbOne = sum(columnToCheck)
        nbZero = len(columnToCheck) - nbOne
            
        bitToKeep = 0        
        if (isLeastCommon and nbOne < nbZero or not isLeastCommon and nbOne >= nbZero):
            bitToKeep = 1
        
        for i in range(len(columnToCheck)):
            if (columnToCheck[i] != bitToKeep):
                inputMatrix.remove(inputMatrix[i])
        return 0
    
    def part2(self):
        # Putting everything in a matrix cuz im tired
        inputMatrix = []
        
        for bin in self.inputData:
            inputMatrix.append([int(bit) for bit in bin])
            
        result1 = self.evaluateCriteria(inputMatrix, True)
            

            
        return 0