import csv 
file_venue = open('venue_h5Index_final.csv', 'r')
file_citation = open('acm_citation.csv', 'r')
csvReader_paper = csv.DictReader(file_citation)
csvReader = csv.reader(file_venue)
file_venue.seek(0)
venues = []
for row in csvReader:
    venues.append(row[0])
   
Authors = []
temp = []
for row in csvReader_paper:
    if(row['venue'] in venues):
        temp = row['authors']
        temp = temp.lstrip('[').rstrip(']').replace("'","").strip().replace(", ",",")
        tempX = temp.split(",")
        Authors.extend(tempX)


Set_of_authors = set(Authors)
Authors1 = list(Set_of_authors)

file_citation.seek(0)
d = file_citation.readlines()
file_citation.seek(0)

file_citation1 = open('acm_citation.csv', 'r')
Authors_Original = []
for row in csvReader_paper:
    temp = row['authors']
    temp = temp.lstrip('[').rstrip(']').replace("'","").strip().replace(", ",",")
    tempX = temp.split(",")
    Authors_Original.append(set(tempX))

Authors_Original.pop(0)
Authors_Original[0]

file_citation1 = open('reduced_acm_citation.csv', 'w')
file_citation1.write(d[0])
global_a_count = 0
for i in d[1:]:
    if Set_of_authors & Authors_Original[global_a_count]:
        file_citation1.write(i)
    global_a_count+=1
file_citation1.close()

