import csv
from datetime import datetime
import random
import re


class Decide(object):
    def __init__(self):
        self.today = datetime.today()

    def assign(self):
        filename = 'cleaning_turn/file/shift-' + str(self.today.year) + '-' + str(self.today.month) + '.csv'
        total = 0
        bias = []
        with open (filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            lines = list(reader)
            for index, time in enumerate(lines[self.today.day]):
                if(index == 0 or time == ''):
                    continue
                else:
                    numbers = re.findall(r'\d+', time)
                    howlong = int(numbers[2]) - int(numbers[0])
                    total += howlong
                    bias.insert(index + 1, total)
            random_number = random.randint(1, total)
            assign_person_number = 0
            for index, bia in enumerate(bias):
                if(bia >= random_number):
                    assign_person_number = index + 2
                    break
                else:
                    continue
            return lines[0][assign_person_number]
