sensor_data = [116.28, 117.1, 123.96, 117.17]


def calc(sensor_data):
  mean_div = []
  for d_point in sensor_data:
      mean = sum(sensor_data)/len(sensor_data)
      if (d_point - mean) < 0:
         avg_point = (d_point - mean)**2
      mean_div.append(pass)
      mean_divi = (sum(mean_div))/4
  #print(str((sum(mean_div))) + "mean diff sum")
  return mean, mean_divi

print(calc(sensor_data))

#print(calc(sensor_data))


  


