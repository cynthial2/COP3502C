#14.4 (M1) Convert from seconds

s = int(input())

hours = s // 3600
minutes = (s % 3600) // 60
seconds = ((s % 3600) % 60) // 1

print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)

