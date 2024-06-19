import datetime
class DateFormat:
    @classmethod
    def conver_data(self, date):
        return datetime.datetime.strptime(date, '%d/%m/%Y')