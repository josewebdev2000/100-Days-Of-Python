#!/bin/python3

import pandas

student_dict = {
	"student": ["Angela", "James", "Lily"],
	"score":   [56, 76, 98]
	}

student_df = pandas.DataFrame(student_dict)


# Loop through rows of data frame
for (index, row) in student_df.iterrows():
	print(row.student)
	print(row.score)

	if row.student == "Angela":
		print(row.score)
