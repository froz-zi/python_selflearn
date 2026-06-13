# Python has the module called statistics and we can use this module to do all the statistical calculations.
# However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central 
# tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, 
# find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all 
# the functions that do statistical calculations as methods for the Statistics class. Check the output below.

class statistic():
    def __init__(self, data):
        self.data = data

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        total = 0
        for number in self.data:
            total += number
        return total

    def min(self):
        minimum = self.data[0]
        for number in self.data:
            if number < minimum:
                minimum = number
        return minimum

    def max(self):
        maximum = self.data[0]
        for number in self.data:
            if number > maximum:
                maximum = number
        return maximum

    def range(self):
        return self.max() - self.min()

    def mean(self):
        average = self.sum() / self.count()
        return round(average)

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        middle = n // 2

        if n % 2 == 1:
            return sorted_data[middle]
        else:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2

    def mode(self):
        frequency = {}

        for number in self.data:
            if number not in frequency:
                frequency[number] = 0
            frequency[number] += 1

        mode_value = None
        mode_count = 0

        for number, count in frequency.items():
            if count > mode_count:
                mode_value = number
                mode_count = count

        return {'mode': mode_value, 'count': mode_count}

    def var(self):
        average = self.sum() / self.count()
        total = 0

        for number in self.data:
            total += (number - average) ** 2

        variance = total / self.count()
        return round(variance, 1)

    def std(self):
        standard_deviation = self.var() ** 0.5
        return round(standard_deviation, 1)

    def percentile(self, p):
        sorted_data = sorted(self.data)
        n = self.count()

        index = (p / 100) * (n - 1)
        lower_index = int(index)
        upper_index = lower_index + 1

        if upper_index >= n:
            return sorted_data[lower_index]

        weight = index - lower_index
        result = sorted_data[lower_index] + (sorted_data[upper_index] - sorted_data[lower_index]) * weight

        return result

    def freq_dist(self):
        frequency = {}

        for number in self.data:
            if number not in frequency:
                frequency[number] = 0
            frequency[number] += 1

        result = []

        for number, count in frequency.items():
            percentage = round((count / self.count()) * 100, 1)
            result.append((percentage, number))

        result.sort(key=lambda item: item[0], reverse=True)
        return result
    



ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())
print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Range:', data.range())
print('Mean:', data.mean())
print('Median:', data.median())
print('Mode:', data.mode())
print('Variance:', data.var())
print('Standard Deviation:', data.std())
print('25th Percentile:', data.percentile(25))
print('50th Percentile:', data.percentile(50))
print('75th Percentile:', data.percentile(75))
print('Frequency Distribution:', data.freq_dist())#ai




# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, 
# account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for
# expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        income = {
            'amount': amount,
            'description': description
        }
        self.incomes.append(income)

    def add_expense(self, amount, description):
        expense = {
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income['amount']
        return total

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense['amount']
        return total

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"""
Account owner: {self.firstname} {self.lastname}
Total income: {self.total_income()}
Total expense: {self.total_expense()}
Account balance: {self.account_balance()}
Incomes: {self.incomes}
Expenses: {self.expenses}
"""