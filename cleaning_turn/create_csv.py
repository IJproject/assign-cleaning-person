import csv
from datetime import datetime, timedelta


class Shift(object):
    def __init__(self, year, month, member):
        self.year = year
        self.month = month
        self.week = ['月', '火', '水', '木', '金', '土', '日']
        self.member = member

    # 月から日にちを取得する
    def get_dates(self):
        start_date = datetime(self.year, self.month, 1)
        if start_date.month < 12:
            next_month = start_date.replace(month=start_date.month + 1, day=1)
        else:
            next_month = start_date.replace(year=start_date.year + 1, month=1, day=1)
        end_date = next_month - timedelta(days=1)
        date_lists = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

        return date_lists

    # 曜日の番号を引数に加えるたとき、土日だとFalseを返す
    def is_weekdays(self, day):
        if(day == 5 or day == 6):
            return False
        else:
            return True

    # 日にちを引数に加えると、5か7の倍数の日にTrueを返す
    def make_sample(self, day):
        if(day % 5 == 0 or day % 7 == 0):
            return True
        else:
            return False

    # CSVファイルを生成する
    def create(self):
        filename = 'cleaning_turn/file/shift' + '-' + str(self.year) + '-' + str(self.month) + '.csv'
        with open (filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, self.member)
            writer.writeheader()
            for date in self.get_dates():
                day = str(date.month) + '/' + str(date.day) + '(' + self.week[date.weekday()] + ')'
                if(self.make_sample(date.day) and self.is_weekdays(date.weekday())):
                    writer.writerow({"日付": day, "サンプル": '10:00~19:00'})
                else:
                    writer.writerow({"日付": day})

