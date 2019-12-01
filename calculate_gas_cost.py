# I made this as I was curious on how much I spend on gas in a month
# all values are based in USD (United States Dollar)
# keep in mind the amount of weeks will be placed in a decimal format to account for leap year + accuracy

# values below are set for my specific vehicle
gas_tank_size = 13.2
average_cost_per_gallon = float(2.57)
fill_up_per_week = 1
# to avoid repeating this calculation over and over I turned it into a variable
needed_calculation_for_each_function = (gas_tank_size * average_cost_per_gallon * fill_up_per_week)

# this is basic but explaining the parameters this program follows
print("This will show you how much you spend on gas depending on:\n your gas tank size\n avg cost per gallon for your area\n and how many times you fill per week\n")

# calculate the weekly cost on gas
def weekly_cost():
    week = needed_calculation_for_each_function
    print("Weekly cost on gas: " + str(week))

# lets see how much it costs per month - number 4.. represents weeks in a month
def one_month_cost():
    month = needed_calculation_for_each_function * 4.34524
    print("One month cost on gas: " + str(month))

# solution to the three month cost - number 13.. is for # of weeks in 3 months
def three_month_cost():
    three_months = needed_calculation_for_each_function * 13.0357
    print("Three months cost on gas: " + str(three_months))

# determine the cost of six months - there are 26.. weeks in 6 months
def six_month_cost():
    six_months = needed_calculation_for_each_function * 26.0715
    print("Six months cost on gas: " + str(six_months))

# computing full year cost - 52.. weeks in a year
def full_year_cost():
    full_year = needed_calculation_for_each_function * 52.1429
    print("One year cost on gas: " + str(full_year))

# calling all functions to display values all at once in this order
weekly_cost()
one_month_cost()
three_month_cost()
six_month_cost()
full_year_cost()