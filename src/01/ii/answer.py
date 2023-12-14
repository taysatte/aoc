"""
Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and
last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""


class Solution():

    def replace_words(self, line: str):
        word_to_num = {
                "one": "o1e",
                "two": "t2o",
                "three": "t3e",
                "four": "f4r",
                "five": "f5e",
                "six": "s6x",
                "seven": "s7n",
                "eight": "e8t",
                "nine": "n9e",
                }

        for key in word_to_num.keys():
            curr = key
            if line.find(curr) >= 0:
                new = word_to_num.get(curr)
                line = line.replace(curr, new)
        return line

    def get_cal_number_from_line(self, line: list) -> int:
        text_length = len(line)
        temp = ""
        for i in range(0, text_length):
            curr = str(line[i])
            if curr.isdigit():
                temp += curr
        if len(temp) <= 1:
            temp += temp

        cal_val = str(temp[0] + temp[-1])
        return cal_val

    def parse_document(self) -> list:
        document = []
        calibration_vals = []

        with open('./input.txt', 'r') as file:
            lines = file.readlines()
            for i in lines:
                word = i
                document.append(word.removesuffix("\n"))

        doc_length = len(document) - 1
        i = 0
        while i <= doc_length:
            text = document[i]
            clean_val = self.replace_words(text)
            cal_val = self.get_cal_number_from_line(clean_val)
            calibration_vals.append(cal_val)
            i += 1

        return calibration_vals

    def sum_calibration_values(self, values: list) -> int:
        cal_sum = 0
        for val in values:
            cal_sum += int(val)
        return cal_sum
