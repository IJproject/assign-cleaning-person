from cleaning_turn.create_csv import Shift
from cleaning_turn.decide import Decide
from datetime import datetime
import os

if __name__ == '__main__':
    member = ["日付", "サンプル", "A本A男", "B橋B子", "C本C介", "D藤D音"]
    filename = 'cleaning_turn/file/shift' + '-' + str(datetime.year) + '-' + str(datetime.month) + '.csv'
    if os.path.exists(filename):
        decide = Decide()
        content = decide.assign() + 'さん、掃除好きでしたよね？\n今日はあなたが掃除したまえ'
        print(content)
    else:
        shift = Shift(2023, 8, member)
        shift.create()
