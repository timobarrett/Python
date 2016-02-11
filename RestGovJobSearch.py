import textwrap
def displayJobInfo(i):
	results.write("\n" + "TITLE -- " + i['JobTitle'] + "\n")
	results.write( "\tMINIMUM SALARY -- " + i['SalaryMin']) 
	results.write( "\tMAXMIMUM SALARY -- " + i['SalaryMax'] +"\n") 
	results.write( "\tURL -- " + i['ApplyOnlineURL'] + "\n")
	for width in [140]:
		results.write( "\tJOB SUMMARY -- \n" ) 
		results.write(textwrap.fill(i['JobSummary'], initial_indent='\t\t', subsequent_indent='\t\t'))
	for width in [140]:	
		results.write( "\n\tLOCATION -- \n" )
		results.write(textwrap.fill(i['Locations'], initial_indent='\t\t', subsequent_indent='\t\t')) 
	results.write("\n\tWHO CAN APPLY -- " + i["WhoMayApplyText"])
	results.write( "\n")
import requests
from requests.auth import HTTPDigestAuth
import json	
def processSeries(series):
	url = "https://data.usajobs.gov/api/jobs?series=0"+str(series)
	theResponse = requests.get(url)
	print theResponse.headers['content-type'] + "series = 0" + str(series)
	print theResponse.status_code
	if(theResponse.ok):
		jsonData = json.loads(theResponse.content)
		print ("jobs data contains {0} properties".format(len(jsonData)))
		count = 0
		if "JobData" in jsonData:
			for j in jsonData['JobData']:
				if location.lower() in j['Locations'].lower() and jobKeyword.lower() in j['JobSummary'].lower():
					displayJobInfo(j)
					count = count + 1
		print "count = " + count.__str__()
	else:
		print "ERROR Getting = " + theResponse.status_code

location = raw_input("Enter preferred job location - ")
jobKeyword = raw_input("Enter preferred job skill - ")
results=open('./jobResults.txt','w+')
for i in range(600, 900):
	processSeries(i)

