from datetime import date


class AgeCalculator:
    def __init__(self, birth_date):
        self.birth_date = birth_date
        self.today = date.today()

    def get_age_in_years(self):
        age = self.today.year - self.birth_date.year
        if (self.today.month, self.today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def get_age_breakdown(self):
        years = self.get_age_in_years()
        last_birthday = date(self.today.year - (
            1 if (self.today.month, self.today.day) < (self.birth_date.month, self.birth_date.day) else 0),
                             self.birth_date.month, self.birth_date.day)

        months = self.today.month - last_birthday.month
        if months < 0:
            months += 12

        days = self.today.day - last_birthday.day
        if days < 0:
            # Borrow days from previous month
            if self.today.month == 1:
                previous_month = 12
                previous_year = self.today.year - 1
            else:
                previous_month = self.today.month - 1
                previous_year = self.today.year

            days_in_previous_month = (date(previous_year, previous_month + 1, 1) -
                                      date(previous_year, previous_month, 1)).days
            days += days_in_previous_month
            months -= 1

        return years, months, days

    def get_next_birthday(self):
        next_birthday = date(self.today.year, self.birth_date.month, self.birth_date.day)
        if next_birthday < self.today:
            next_birthday = date(self.today.year + 1, self.birth_date.month, self.birth_date.day)

        days_until = (next_birthday - self.today).days
        return next_birthday, days_until


# Usage example
calculator = AgeCalculator(date(1995, 8, 20))
years, months, days = calculator.get_age_breakdown()
next_bday, days_until = calculator.get_next_birthday()

print(f"Current age: {years} years, {months} months, {days} days")
print(f"Next birthday: {next_bday} (in {days_until} days)")