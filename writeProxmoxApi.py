import sys

#color class
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def firstChar(s):
    return s[:1]

def lastChar(s):
    return s[-1:]

    #checks if the user has specified an input file
if len(sys.argv) < 2:
    print (bcolors.FAIL + "error no input file specified..." +  bcolors.ENDC)
    sys.exit()
else:
    inputfile = sys.argv[1]

    #checks if the user has specified an output file
if len(sys.argv) < 3:
    print(bcolors.FAIL + "error no output file specified..."  +  bcolors.ENDC)
    sys.exit()
else:
    outputfile =  sys.argv[2]

print(bcolors.OKGREEN + "opening file..." + bcolors.ENDC)

inputText = open(inputfile, 'r')
f = open(outputfile, 'w')

currentLink = ""
currentModule = ""
outputString = ""
for line in inputText:
    if firstChar(line) == '/':
        currentLink = line
        parts = line.split('/')
        Module = parts[3]

        if lastChar(Module) == 'n':
            Module = Module[:-1]

        if Module != currentModule:
            currentModule = Module
            outputString += "}, \n" + Module + " : { \n"

    else:

        linkPart = currentLink.split('/')
        linkPart[len(linkPart) - 1] = linkPart[len(linkPart) - 1][:-1]
        del linkPart[0]
        del linkPart[0]
        del linkPart[0]

        method = line.lower()
        method = method[:-1]

        #outputString += linkPart[0] + '.'

        for i in range(len(linkPart)):
            if i > 0:
                if firstChar(linkPart[i]) == '{':
                    linkPart[i] = linkPart[i][1:-1]
                if i == (len(linkPart) - 1):
                    outputString += method + linkPart[i]
                else:
                    outputString += linkPart[i]

        if len(linkPart) == 1:
            outputString += method

        print(bcolors.OKGREEN + 'creating function for ' + currentLink[:-1] + " "  + method + bcolors.ENDC)
        #creates the function name

        linkPart = currentLink.split('/')
        linkPart[len(linkPart) - 1] = linkPart[len(linkPart) - 1][:-1]
        del linkPart[0]

        params = []
        #adds the parameters to the name
        for x in range(len(linkPart)):
            if firstChar(linkPart[x]) == "{":
                part = linkPart[x][1:-1]
                params.append(part)

        outputString += ' : function ('
        for i in range(len(params)):
            outputString += params[i] + ','
        #checks if the method needs data input
        if method == 'put' or method == 'post':
            outputString += "data,"

        outputString += 'callback) { \n'
        #adds the data component if not added before
        if method == 'get' or method == 'del':
            outputString += "data = {}; \n"

        outputString += "url = "
        linkPart = currentLink.split('/')
        linkPart[len(linkPart) - 1] = linkPart[len(linkPart) - 1][:-1]
        del linkPart[0]
        for i in range(len(linkPart)):
            if firstChar(linkPart[i]) == "{":
                if i == (len(linkPart) - 1):
                    outputString += linkPart[i][1:-1]
                else:
                    outputString += linkPart[i][1:-1] + " + "
            else:
                if i == (len(linkPart) - 1):
                    outputString += "'/" + linkPart[i] + "'"
                else:
                    outputString += "'/" + linkPart[i] + "/' + "

        outputString += "; \n"
        outputString += method + "(url,data,callback); \n }, \n \n"


f.write(outputString)
print(bcolors.OKGREEN + "done!" + bcolors.ENDC)
f.close()
