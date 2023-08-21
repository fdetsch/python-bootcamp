# %% create plot

import matplotlib.pyplot as plt

numbers = [5, 10, 15, 20]

fig, ax = plt.subplots()

ax.plot(numbers)

plt.show()

# %% plot revenue over time

revenue_2020 = [6436, 2355, 5533, 6334, 5332, 5466, 7576, 4356, 3258, 2356, 2545, 5255]
revenue_2021 = [3542, 5243, 5121, 7321, 9511, 5541, 8851, 3574, 4215, 5678, 8422, 7512]

month = list(range(1, 13))

plt.style.use('seaborn')
fig, ax = plt.subplots()

plt.xticks(month)
ax.plot(month, revenue_2020, label = '2020')
ax.plot(month, revenue_2021, label = '2021')

plt.legend()

ax.set_title('revenue by month')
ax.set_xlabel('month')
ax.set_ylabel('revenue in €')

plt.show()

# %% add more data and fine-tuning