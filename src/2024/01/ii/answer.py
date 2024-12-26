'''
--- Part Two ---

Your analysis only confirmed what everyone feared: the two lists of location
IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read
most of the Chief's handwriting, but in the commotion you notice an interesting
detail: a lot of location IDs appear in both lists! Maybe the other numbers
aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the
left list appears in the right list. Calculate a total similarity score by
adding up each number in the left list after multiplying it by the number
of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

- The first number in the left list is 3. It appears in the right list three
times, so the similarity score increases by 3 * 3 = 9.

- The second number in the left list is 4. It appears in the right list once,
so the similarity score increases by 4 * 1 = 4.

- The third number in the left list is 2. It does not appear in the right
list, so the similarity score does not increase (2 * 0 = 0).

- The fourth number, 1, also does not appear in the right list.

- The fifth number, 3, appears in the right list three times; the similarity
score increases by 9.

- The last number, 3, appears in the right list three times; the similarity
score again increases by 9.

So, for these example lists, the similarity score at the end of this
process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
'''

import sys


class Puzzle:
    '''Puzzle class'''

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        '''Run Method'''
        self.parse()

    def get_similarity(self, lst1: list, lst2: list) -> int:
        '''Finds similarity score between list 1 and list 2'''
        score = 0

        for i in lst1:
            curr_num = i
            num_occurrence = 0
            for j in lst2:
                if curr_num == j:
                    num_occurrence += 1
            if num_occurrence > 0:
                score += (curr_num * num_occurrence)

        return score

    def parse(self) -> None:
        '''Parse Input'''
        file = open(sys.argv[1]).read().splitlines()

        lst1, lst2 = [], []

        for line in file:
            lst1.append(int(line.split()[0]))
            lst2.append(int(line.split()[1]))

        sim_score = self.get_similarity(lst1, lst2)
        print(sim_score)


if __name__ == '__main__':
    puzzle = Puzzle()
    puzzle.run()
