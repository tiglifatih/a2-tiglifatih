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

#######################################################
###
###	print("This assignment (assignment 2) hasn't been finished.")
###	print("All it can do is print out the contents of a couple of cells of the file a2_input.csv:")
###	print("Cell at index 0,0:")
###	print(contents[0][0])
###	print("Cell at index 0,1:")
###	print(contents[0][1])
###	print("Cell at index 1,0:")
###	print(contents[1][0])
###
###
###	print("\n\nfrom pdf\n\n")
###
###	print("print contents\n")
###	print(contents)
###	print("\nprint contents[0]\n")
###	print(contents[0])
###	print("\nprint contents[0][0]\n")
###	print(contents[0][0])
###	print("\ntype contents\n")
###	print("<!--")
###	print(type(contents))
###	print("-->")
###	print("\ntype contents[0]\n")
###	print("<!--")
###	print(type(contents[0]))
###	print("-->")
###	print("\ntype contents[0][0]\n")
###	print("<!--")
###	print(type(contents[0][0]))
###	print("-->")
###	print("\nprint contents[5][6]\n")
###	print(contents[5][6])
###	print("\ntype contents[5][6]\n")
###	print("<!--")
###	print(type(contents[5][6]))
###	print("-->")
###
###	print("\nsum of columns:\n")
###	agetotal = 0
###	for i in range(1, 16):
###		agetotal += int(contents[i][3])
###	print("Age total: ", str(agetotal), "!!")
###
#######################################################

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

		
total_age = 0
player_count = 0
for i in range(1, 16):
	total_age += float(contents[i][3])
	player_count += 1
average_age = round(float(total_age / player_count), 1)


shorter = 0
taller = 0
for i in range(1, 16):
	if(float(contents[i][4]) <= 1.80):
		shorter += 1
	if(float(contents[i][4]) >= 2.10):
		taller += 1

				
total_points = 0
scored_players = 0
for i in range(1, 16):
	total_points += float(contents[i][8])
	if(contents[i][6] != "0"):
		scored_players += 1
average_points = round(float(total_points / scored_players), 1)


max_points = 0
for i in range(1, 16):
	if(max_points <= float(contents[i][8])):
		max_points = float(contents[i][8])
		player_points = i
	else:
		continue


total_pir = 0
pir_players = 0
for i in range(1, 16):
	total_pir += float(contents[i][18])
	if(contents[i][6] != "0"):
		pir_players += 1
average_pir = round(float(total_pir / pir_players), 1)


max_pir = 0
for i in range(1, 16):
	if(max_pir <= float(contents[i][18])):
		max_pir = float(contents[i][18])
		player_pir = i
	else:
		continue


noplay = 0
for i in range(1, 16):
	if(contents[i][6] == "0"):
		noplay += 1
	

html_page = """ 
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8"/>
		<title>Fenerbahce Dogus Istanbul</title>
		<style>
			body{
				color: gold;
				background-color: grey;
			}
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
			th, caption{
				color: black;
			}
			div{
				border: 3px solid navy;
				margin: 10px;
			}
			li{
				margin: 2px;
			}
			tr:hover, div:hover{
				background-color: blue;
			}
		</style>
	</head>
	<body>
		<table>
			<caption><strong>Fenerbahce Dogus Istanbul Turkish Airlines Euroleague Statistics</strong><caption>
"""

for i in range(18):
	html_page += "			<tr>\n"
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
			
				html_page += "				<td>" + contents[i][j] + "</td>\n"
	html_page += "			</tr>\n"

html_page += """
		</table>
		</br>
		<div>
			<ul>
				<li>Number of players in 'Center' position is '""" + str(pos_c) + """'.</li>
				<li>Number of players in 'Forward' position is '""" + str(pos_f) + """'.</li>
				<li>Number of players in 'Guard' position is '""" + str(pos_g) + """'.</li>
				<li>'""" + str(noplay) + """' players did not play in any of the games this season</li>
				<li>Average age of the team is '""" + str(average_age) + """'.</li>
				<li>Number of players older than 30 years old is '""" + str(older) + """'.</li>
				<li>Number of players shorter than 1.80 is '""" + str(shorter) + """'.</li>
				<li>Number of players taller than 2.10 is '""" + str(taller) + """'.</li>
				<li>Average score per player is '""" + str(average_points) + """ points'.</li>
				<li>The player who scored the most points with '""" + str(max_points) + """' is '""" + str(contents[player_points][1]) + """'.</li>
				<li>Player Index Rating per player is '""" + str(average_pir) + """'.</li>
				<li>'""" + str(contents[player_pir][1]) + """' is the most efficient player with '""" + str(max_pir) + """' index rating.</li>	
			</ul>
		</div>
	</body>
</html>
"""

print(html_page)
