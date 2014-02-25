import json
import re
import sys


def getFormattedChangesetID(id):
    return '=={{Commit|' + str(id) + '}}=='

def getFormattedComment(comment):
    #Do find and replace to add mediawiki formatting
    
    #Replace 'PBI 12345' with '{{PBI|12345}}'
    formattedComment = re.sub(r'(?P<pbi>PBI|Pbi|pbi)\W(?P<pbiID>\d{5})', '{{\g<pbi>|\g<pbiID>}}',comment)
    
    #Replace 'Bug 12345' with '{{Bug|12345}}'
    formattedComment = re.sub(r'(?P<bug>BUG|Bug|bug)\W(?P<bugID>\d{5})', '{{\g<bug>|\g<bugID>}}',formattedComment)
    
    #Replace 'VAN-123' with '{{Jira|VAN-123}}'
    formattedComment = re.sub(r'(?P<van>VAN|Van|van)-(?P<vanID>\d{1,5})', '{{Jira|\g<van>-\g<vanID>}}',formattedComment)

    #Replace 'Ticket #123456' with '{{Ticket|123456}}'
    #Or Ticket# 123456
    #Or Ticket 123456
    formattedComment = re.sub(r'(?P<tick>Ticket)((\W*#\W*)|\W*)(?P<tickID>\d{6})', '{{\g<tick>|\g<tickID>}}', formattedComment)
    
    return formattedComment
	
def getFormattedChangeset(id, comment):
    return getFormattedChangesetID(id) + '\r\n' + getFormattedComment(comment) + '\r\n'

def usage():
    print 'Usage: ' + sys.argv[0] + ' [InputFileName] '

def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(2)

    adjacentFileName = sys.argv[1]

    fileText = open(adjacentFileName).read()

    jsonData = json.loads(fileText)


    out = open( 'format'+sys.argv[1] ,'wb')

    changesets = jsonData
    changesets.reverse() #Github api gives news commits first by default, we want oldest first
    
    #Write each changeset formatting to file:
    for set in changesets:
        out.write(getFormattedChangeset(set['sha'],set['commit']['message']))
        out.write('*to review' + '\r\n')
        out.write('')
        
if  __name__ =='__main__':
    main()