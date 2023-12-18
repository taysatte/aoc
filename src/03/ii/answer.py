"""
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong?
Fortunately, the gondola has a phone labeled "help", so you pick it up and the
engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving with
the other. You're going so slowly that you haven't even left the station.
You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up
so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has
part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the
lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear
because it is only adjacent to one part number.) Adding up all of the gear
ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

import sys


class Solution():

    def run(self) -> None:
        self.main()

    def main(self):
        file = open(sys.argv[1]).read()
        lines = file.strip().split("\n")

        n = len(lines)      # line length
        m = len(lines[0])   # col length

        gear_nums = [[[] for _ in range(m)] for _ in range(n)]

        ans = 0

        def is_symbol(i, j, num):
            # checks if given cell is within the specified grid
            # n == line index
            # m == column index
            if not (0 <= i < n and 0 <= j < m):
                return False

            if lines[i][j] == "*":
                gear_nums[i][j].append(num)

            # returns true if the specified cell is not a "." and
            # not a number
            return lines[i][j] != "." and not lines[i][j].isdigit()

        for i, line in enumerate(lines):
            start = 0
            j = 0

            while j < m:
                start = j
                num = ""
                while j < m and line[j].isdigit():
                    num += line[j]
                    j += 1

                if num == "":
                    j += 1
                    continue

                num = int(num)

                is_symbol(i, start - 1, num) or is_symbol(i, j, num)

                for k in range(start - 1, j + 1):
                    is_symbol(i - 1, k, num) or is_symbol(i + 1, k, num)

        for i in range(n):
            for j in range(m):
                nums = gear_nums[i][j]
                if lines[i][j] == "*" and len(nums) == 2:
                    ans += nums[0] * nums[1]
        print(ans)


if __name__ == "__main__":

    s = Solution().run()
