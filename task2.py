"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest = 0
longest_key = None
longest_call = {}

for call in calls:
    call_duration = int(call[3])

    if call[0] in longest_call.keys():
        longest_call[call[0]] = longest_call[call[0]] + call_duration
    else:
        longest_call[call[0]] = call_duration

    if call[1] in longest_call.keys():
        longest_call[call[1]] = longest_call[call[1]] + call_duration
    else:
        longest_call[call[1]] = call_duration

    if longest_call[call[0]] > longest:
        longest_key = call[0]
        longest = longest_call[call[0]]

    if longest_call[call[1]] > longest:
        longest_key = call[1]
        longest = longest_call[call[1]]

print("{} spent the longest time, {} seconds, on the phone during September 2016."
      .format(longest_key, longest))
