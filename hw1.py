# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061234.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

#=======================================
for item in data:
    if item['TEMP'] == '-99.000' or item['TEMP'] == '-999.000':
        item['TEMP'] = ' '
C0A880 = ['C0A880', 'None']
C0F9A0 = ['C0F9A0', 'None']
C0G640 = ['C0G640', 'None']
C0R190 = ['C0R190', 'None']
C0X260 = ['C0X260', 'None']
for item in data:
    if item['station_id'] == 'C0A880':
        if item['TEMP'] != ' ' and C0A880[1] != 'None':
            if float(item['TEMP']) > C0A880[1]: C0A880[1] = float(item['TEMP'])
        elif item['TEMP'] != ' ' and C0A880[1] == 'None': C0A880[1] = float(item['TEMP'])
    elif item['station_id'] == 'C0F9A0':
        if item['TEMP'] != ' ' and C0F9A0[1] != 'None':
            if float(item['TEMP']) > C0F9A0[1]: C0F9A0[1] = float(item['TEMP'])
        elif item['TEMP'] != ' ' and C0F9A0[1] == 'None': C0F9A0[1] = float(item['TEMP'])
    elif item['station_id'] == 'C0G640':
        if item['TEMP'] != ' ' and C0G640[1] != 'None':
            if float(item['TEMP']) > C0G640[1]: C0G640[1] = float(item['TEMP'])
        elif item['TEMP'] != ' ' and C0G640[1] == 'None': C0G640[1] = float(item['TEMP'])
    elif item['station_id'] == 'C0R190':
        if item['TEMP'] != ' ' and C0R190[1] != 'None':
            if float(item['TEMP']) > C0R190[1]: C0R190[1] = float(item['TEMP'])
        elif item['TEMP'] != ' ' and C0R190[1] == 'None': C0R190[1] = float(item['TEMP'])
    elif item['station_id'] == 'C0X260':
        if item['TEMP'] != ' ' and C0X260[1] != 'None':
            if float(item['TEMP']) > C0X260[1]: C0X260[1] = float(item['TEMP'])
        elif item['TEMP'] != ' ' and C0X260[1] == 'None': C0X260[1] = float(item['TEMP'])
target_data = [C0A880, C0F9A0, C0G640, C0R190, C0X260]
# Part. 4
#=======================================
# Print result
print(target_data)
#========================================