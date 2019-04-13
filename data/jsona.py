import csv
import json

csvfile = open('bsl_user.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("id","username","email","firstName","profession","rating","lower_bound","question_count","upper_bound","session_confidence","cSum","c_level","score")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
