def max_requests(lines):
  gl = len(lines)
  s_ms = []
  e_ms = []

  # Data transformation into all millisecond level
  # O(n)
  for line in lines:
    d = line.split(' ')
    t = d[1].split(':')
    end_time = int(t[0])*3600000 + int(t[1])*60000 + int(float(t[2]) * 1000)
    time_took = int(float(d[2].replace('s','')) * 1000)

    s_ms.append(end_time - time_took)
    e_ms.append(end_time)
  
  max_r = 0 

  for i in range(gl):
    l_max = 1
    r_max = 1

    for j in range(gl):
      if i != j:
        if s_ms[j] <= e_ms[i] and e_ms[i] <= e_ms[j]:
          r_max += 1
        elif e_ms[i] <= s_ms[j] and s_ms[j] < e_ms[i] + 999:
          r_max += 1

    curr_max = max(l_max, r_max)
    max_r = max(max_r, curr_max)
    if i == 1:
      break

  return max_r
  
input1 = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
input2 = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
input3 = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", \
          "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", \
          "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", \
          "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", \
          "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

print(max_requests(input1))
print(max_requests(input2))
print(max_requests(input3))
