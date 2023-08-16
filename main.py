from cleaning_turn.create_csv import Shift
from cleaning_turn.decide import Decide
from datetime import datetime

if __name__ == '__main__':
    member = ["日付", "サンプル", "A本A男", "B橋B子", "C本C介", "D藤D音"]
    decide = Decide()
    content = decide.assign() + 'さん、掃除好きでしたよね？\n今日はあなたが掃除したまえ'
    print(content)

    shift_make = input('\n来月のシフト表を作成しますか？(y/n)：')
    if(shift_make == 'y'):
        shift = Shift(2023, datetime.today().month, member)
        shift.create()
