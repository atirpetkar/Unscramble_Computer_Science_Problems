"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

text_out_set = set([text[0] for text in texts])
text_in_set = set([text[1] for text in texts])

call_out_set = set([call[0] for call in calls])
call_in_set = set([call[1] for call in calls])

different_records = set()

different_records.update(text_out_set)
different_records.update(text_in_set)

different_records.update(call_out_set)
different_records.update(call_in_set)

print("There are {} different telephone numbers in the records.".format(len(different_records)))
