#import the package named 'csv' and 'sqlite3'
import csv
import sqlite3
#anything that's a separated value file (or delimited) will be called csv
#convert file into file object
csvfile = open('imdb_data/title.basics.tsv', newline='')
db = sqlite3.connect('imdb_data/imdb.sqlite')
cursor = db.cursor()
csvreader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)

def checkNull(val):
	if val == '\\N':
		return None
	else:
		return val

def checkNullInt(val):
	if val == '\\N':
		return None
	else:
		return int(val)

# row is an array
hasSeenHeader = False
for row in csvreader:
	if not hasSeenHeader:
		hasSeenHeader = True
		continue
	#print(', '.join(row))
	#statement = "INSERT INTO TitleBasics (titleId, titleType, primaryTitle, startYear) VALUES ('" + row[0] + "', '" + row[1] + "', '" + row[2] + "', " + row[5]+ ");"
	#print(statement)
	statement = 'INSERT INTO TitleBasics (titleId, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'
	params = (checkNull(row[0]), checkNull(row[1]), checkNull(row[2]), checkNull(row[3]), checkNullInt(row[4]), checkNullInt(row[5]), checkNullInt(row[6]), checkNullInt(row[7]))
	cursor.execute(statement, params)
	if row[8] != '\\N' and row[8] != '':
		#split returns an array (list is proper python term)
		genres = row[8].split(',')
		for genre in genres:
			statement2 = 'INSERT INTO TitleBasicsGenres (titleId, genre) VALUES (?, ?);'
			params2 = (row[0], genre)
			cursor.execute(statement2, params2)
# do the commit outside the loop or else it's slow
db.commit()
csvfile.close()
db.close()


