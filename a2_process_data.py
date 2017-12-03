#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

"""

	print("This assignment (assignment 2) hasn't been finished.")
	print("All it can do is print out the contents of a couple of cells of the file a2_input.csv:")
	print("Cell at index 0,0:")
	print(contents[0][0])
	print("Cell at index 0,1:")
	print(contents[0][1])
	print("Cell at index 1,0:")
	print(contents[1][0])


	print("\n\nfrom pdf\n\n")

	print("print contents\n")
	print(contents)
	print("\nprint contents[0]\n")
	print(contents[0])
	print("\nprint contents[0][0]\n")
	print(contents[0][0])
	print("\ntype contents\n")
	print("<!--")
	print(type(contents))
	print("-->")
	print("\ntype contents[0]\n")
	print("<!--")
	print(type(contents[0]))
	print("-->")
	print("\ntype contents[0][0]\n")
	print("<!--")
	print(type(contents[0][0]))
	print("-->")
	print("\nprint contents[5][6]\n")
	print(contents[5][6])
	print("\ntype contents[5][6]\n")
	print("<!--")
	print(type(contents[5][6]))
	print("-->")

	print("\nsum of columns:\n")
	agetotal = 0
	for i in range(1, 16):
		agetotal += int(contents[i][3])
	print("Age total: ", str(agetotal), "!!")

"""
pos_c = 0
pos_f = 0
pos_g = 0

for i in range(16):
	if(contents[i][5] == "C"):
		pos_c += 1
	if(contents[i][5] == "F"):
		pos_f += 1
	if(contents[i][5] == "G"):
		pos_g += 1

older = 0

for i in range(1, 16):
	if(int(contents[i][3]) >= 30):
		older += 1
		
age_total = 0
player_count = 0
for i in range(1, 16):
	age_total += int(contents[i][3])
	player_count += 1
average_age = age_total / player_count

html_page = """ 
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8"/>
		<title>Fenerbahce Dogus Istanbul Euroleague Statistics</title>
		<style>
			table{
				margin: 10px;
				border-collapse: collapse;
				border: 3px solid navy;
				text-align: center;
			}
			td, th{
				border: 2px solid navy;
				padding: 2px;
			}
		</style>
	</head>
	<body>
		<table>
"""

for i in range(18):
	html_page += "			<tr>\n"
	row = contents[i]
	if i == 0:
		for j in range(19):
			html_page += "				<th>" + contents[i][j] + "</th>\n"
	elif(i == 16):
		continue
	elif(i == 17):
		for j in range(19):
			if(j == 0):
				html_page += "				<td colspan='2' style='font-style:italic;'>" + contents[i][1] + "</td>\n"
			elif(j == 1):
				continue
			else:
				html_page += "				<td style='font-style:italic;'>" + contents[i][j] + "</td>\n"	
	else:
		for j in range(19):
			if(contents[i][j] == ""):
				html_page += "				<td>&empty;</td>\n"
			else:
				html_page += "				<td>" + contents[i][j] + "</td>\n"
	html_page += "			</tr>\n"

html_page += """
		</table>
		</br>
		<ul>
			<li>Number of players in 'Center' position is """ + str(pos_c) + """.</li>
			<li>Number of players in 'Forward' position is """ + str(pos_f) + """.</li>
			<li>Number of players in 'Guard' position is """ + str(pos_g) + """.</li>
			<li>Number of players older 30 years old is """ + str(older) + """.</li>
			<li>Average age of team is """ + str(average_age) + """.</li>
			<li>"""


html_page += """
		</ul>
	</body>
</html>
"""

print(html_page)
