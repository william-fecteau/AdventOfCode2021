from utils.aoc_utils import AOCDay, day
from statistics import median, mean
import math

@day(7)
class Day7(AOCDay):
    def common(self):
        self.lstPos = [int(x) for x in self.inputData[0].split(',')]        
        return 0

    def part1(self):
        lstMedian = int(median(self.lstPos))
        return sum([abs(lstMedian-x) for x in self.lstPos])
    

    def part2(self):
        lstAvg = math.floor(mean(self.lstPos))
        return int(sum([(abs(lstAvg-x)*(abs(lstAvg-x)+1))/2 for x in self.lstPos]))