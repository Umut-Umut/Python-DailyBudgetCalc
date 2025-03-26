from DB import *
from datetime import datetime

class Butce(DB):
    # constants
    GUN = 0
    AYLIK = 1

    def __init__(self, name):
        self.values = self.get_values()
        self.gun = self.values[Butce.GUN]
        self.aylik = self.values[Butce.AYLIK]

        super().__init__(name)

    def update_values(self, int_value, float_value1, float_value2 = 0):
        self.gun = int_value
        self.aylik = float_value1

        return super().update_values(int_value, float_value1, float_value2)
    
    def daily_budget(self):
        today = datetime.date.today()
        future : datetime
        # next month
        if today.day < 8:
            # same month
            future = datetime.date(today.year, today.month, self.gun)
        else:
            # next month
            future = datetime.date(today.year, today.month + 1, self.gun)
        diff = future - today

        return self.aylik / diff.days
    
if __name__ == '__main__':
    # some tests
    bt = Butce("bt")
