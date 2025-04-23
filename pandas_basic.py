import pandas as pd
data = pd.read_csv('cpu_stats.csv')

print(data)

print('\n')

# Calculate average CPU usage
print(f"Average CPU usage: {data['cpu_usage'].mean():.2f}%")

print('\n')

# Filter high CPU usage days & high memory usage days

print("High CPU usage days: ")
print(data[data['cpu_usage'] > 80])

print('\n')

print("High Memory usage days: ")
print(data[data['memory_usage'] > 80])


# .mean() adds up all the values and divides by the total number of values
# Mean = sum of all values / number of values

#  :.2f means
#  : tells Python you want to format the value.
#  .2f means:
#       2 = show 2 digits after the decimal point.
#       f = floating-point number


#  What does "format the value" mean?
# It means changing how a value looks when you to print or display it — without
# changing the value itself.

# value = 3.1415926535
# print(value)  Output: 3.1415926535
# print(f"{value:.2f}")  Output: 3.14
# You still have the same value in memory, but you're showing only 2 digits
# after the decimal point. That’s what formatting does
