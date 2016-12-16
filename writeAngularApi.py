#libraries
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

inputText = open(inputfile, 'r')
f = open(outputfile, 'w')

for line in inputText:
    args = line.split('(')
    funcName = args[0]

    url = '/api/' + funcName
    args = args[1].split(',')
    del args[-1]

    final = "\n //" + funcName + "() \n"

    #sets the header
    final = final +  " $scope." + funcName + " = function ("
    for arg in args:
        final = final + arg + ","
    #sets the config
    final = final + " callback) { \n url = '" +  url + "'; \n data = {  \n name: $scope.user.name, \n pass: $scope.user.pass, \n"
    for arg in args:
        final = final + arg + ": " + arg + ", \n"
    #finishes the config
    final = final + " }; \n"
    #http function
    final = final + " $http.post(url, data).then (function (res) { \n if (typeof callback == 'function'){ \n callback(res); \n } \n }); \n };"

    final = final + " \n"

    f.write(final)

print(bcolors.OKGREEN + "done! cleaning up..." + bcolors.ENDC)
f.close();
