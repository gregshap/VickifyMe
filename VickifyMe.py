import json
import re
import sys


def getFormattedChangesetID(id):
    return '=={{Changeset|' + str(id) + '}}=='

def getFormattedComment(comment):
    #Do find and replace to add mediawiki formatting
    
    #Replace 'PBI 12345' with '{{PBI|12345}}'
    formattedComment = re.sub(r'(?P<pbi>PBI|Pbi|pbi)\W(?P<pbiID>\d{5})', '{{\g<pbi>|\g<pbiID>}}',comment)
    
    #Replace 'Bug 12345' with '{{Bug|12345}}'
    formattedComment = re.sub(r'(?P<bug>BUG|Bug|bug)\W(?P<bugID>\d{5})', '{{\g<bug>|\g<bugID>}}',formattedComment)
    
    
    #Replace 'Ticket #123456' with '{{Ticket|123456}}'
    formattedComment = re.sub(r'(?P<tick>Ticket)(\W#|#\W)(?P<tickID>\d{6})', '{{\g<tick>|\g<tickID>}}', formattedComment)
    
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

    changesets = jsonData['__wrappedArray']

    #Print each changeset
    changesets.reverse() #TFS gives us newest sets first, but we want oldest first
    for set in changesets:
        out.write(getFormattedChangeset(set['id'],set['comment']))
        out.write('*to review' + '\r\n')
        out.write('')
        
