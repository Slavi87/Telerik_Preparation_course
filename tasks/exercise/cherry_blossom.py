expected_date = input().split()
average_temperature_prediction = int(input())
rain = int(input())
winter_length_days = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date = int(expected_date[0])
month = expected_date[1]
year = int(expected_date[2])

if (year - 2000) % 4 == 0:
    average_temperature_prediction = average_temperature_prediction + 5

winter_weeks = winter_length_days // 7
rain_difference = abs(rain - 30)
additional_rain_days = rain_difference // 3
final_date = date + int(winter_weeks) + additional_rain_days
if average_temperature_prediction > 20:
    diff = average_temperature_prediction - 20
    final_date -= diff
elif average_temperature_prediction < 20:
    diff = 20 - average_temperature_prediction
    final_date += diff
month_index = 0
if month in months:
    month_index = months.index(month)

if final_date < 1:
    diff = 0 - final_date
    final_month = months[month_index - 1]
    final_new_date = days[month_index - 1] - diff
    print(f'{final_new_date} {final_month} {year}')
else:
    print(f'{final_date} {month} {year}')

