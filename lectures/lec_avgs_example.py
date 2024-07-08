'''lec_avgs_exmaple.py'''

dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# start will be set to 2 and end will be set to 6

start = dates.index('2020-01-06')
end = dates.index('2020-01-10')
print(start, end)

#slicing the prices, slicing does not involve an ending point
prcs_w1 = prices[start:end+1]

#calculating the average prices
avgprc = sum(prcs_w1)/len(prcs_w1)
print(avgprc)

prc_dic = {
  '2020-01-02': 7.1600,
  '2020-01-03': 7.1900,
  '2020-01-06': 7.0000,
  '2020-01-07': 7.1000,
  '2020-01-08': 6.8600,
  '2020-01-09': 6.9500,
  '2020-01-10': 7.0000,
  '2020-01-13': 7.0200,
  '2020-01-14': 7.1100,
  '2020-01-15': 7.0400,
  }