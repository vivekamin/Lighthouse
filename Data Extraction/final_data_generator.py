import csv
file_venue = open('venue_h5Index_final.csv', 'r')
file_citation = open('reduced_acm_citation.csv', 'r')
csvReader_paper = csv.DictReader(file_citation)
csvReader = csv.reader(file_venue)

def hIndex(citations):
     #print(citations)
    citations.sort(reverse=True)
    h = 0
    for x in citations:
        if x >= h + 1:
            h += 1
        else:
            break
    return h

def i10Index(citations):
	#citations.sort(reverse=True)
    h = 0
    for x in citations:
        if x >= 10:
            h += 1
        else:
            break
    return h






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


venue_score = dict()
file_venue_score = open('venue_score.csv', 'r')
csvReader_venuescore = csv.reader(file_venue_score)
for row in csvReader_venuescore:
    venue_score[row[0]] = int(row[1])



# change below file mode to 'a' instead of 'w'. So it will be open in APPEND MODE
final_dataset = open('final_dataset.csv', 'w',newline='')
#--------------------------------------------------------------------------------##

csvWriter_dataset = csv.writer(final_dataset,delimiter=',')

##---- comment below two lines when you are running file after first run---------##
s1 = ['AuthorName','aPublication','coAuthor','yearsInField','venueImpact','h-Index','i10-Index','aRefs','TotalCitation']
csvWriter_dataset.writerow(s1)
###################################################################################


#csvReader_author = csv.reader(file_Author_info)
author_count = 0
global_count = 0
#########################################################################################
'''When you change Dataset_Done_count..Don't forget to change file mode of final_dataser.csv &
	commenting writing header part as Stated Above . On line 103 '''

Dataset_Done_Count = 0

#########################################################################################

Authors1.sort()

for name in Authors1[Dataset_Done_Count + 1:]:
        total_citation = 0
        total_coauthors = 0
        refs = 0
        citationList = []
        global_count+=1
        author_count+=1
        file_citation.seek(0)
        years = set()
        papers = 0
        venue_impact = 0
        for row in csvReader_paper:
            temp = row['authors']
            refs1 = row['refs']

            temp = temp.lstrip('[').rstrip(']').replace("'","").strip().replace(", ",",")
            tempX = temp.split(",")

            if(name in temp):
                total_coauthors+=temp.count(",")
                if(refs1 != '[]'):
                    refs+=refs1.count(",")+1
                year = int(row['year'])
                if(year <= 2008):
                    years.add(year)
                    papers+=1
                    count = int(row['citation'])
                    if(count < 0 ):
                        count = 0
                    total_citation+=count
                    citationList.append(count)
                    if(row['venue'] in venue_score.keys()):
                        venue_impact+=venue_score[row['venue']]
        tYears = len(years)
        if(tYears <= 0 ):
            tYears = 1
            years_worked = 1
        else:
            years_worked = max(years)-min(years)+1
        print(papers, '  ', tYears, '  ',name)
        aPub = papers/tYears
        aCoauthor = total_coauthors/tYears
        hIndex_f = hIndex(citationList)
        i10Index_f = i10Index(citationList)
        aRefs = refs/tYears
        vImpact = venue_impact/tYears
        data1 = [name,aPub , aCoauthor, years_worked,vImpact,hIndex_f,i10Index_f, aRefs, total_citation]
        csvWriter_dataset.writerow(data1)
        # if(global_count > 3):
        #     final_dataset.close()
        #     break
