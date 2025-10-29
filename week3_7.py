# for hour in range(12,24):
#     for minute in range(0,60,15):
#         if minute == 0:
#             print (f"{hour}:00")
#         else:
#             print (f"{hour}:{minute}")

for hour in range(12, 24):
    for minute in range(0, 60, 15):
        print(f"{hour}:{minute:02d}")
