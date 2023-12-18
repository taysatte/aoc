"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you.

You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation
of the engine. There are lots of numbers and symbols you don't really
understand, but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum. (Periods (.) do not
count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger.

What is the sum of all of the part numbers in the engine schematic?
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

        def is_symbol(i, j):
            # checks if given cell is within the specified grid
            # n == line index
            # m == column index
            if not (0 <= i < n and 0 <= j < m):
                return False

            # returns true if the specified cell is not a "." and
            # not a number
            return lines[i][j] != "." and not lines[i][j].isdigit()

        ans = 0

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

                if is_symbol(i, start - 1) or is_symbol(i, j):
                    ans += num
                    j += 1
                    continue

                for k in range(start - 1, j + 1):
                    if is_symbol(i - 1, k) or is_symbol(i + 1, k):
                        ans += num
                        break
        print(ans)


if __name__ == "__main__":

    s = Solution().run()
