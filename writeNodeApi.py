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

    final = '\n'
    final = final + "//" + funcName + "() \n"
    final = final + "app.post('" + url + "', function (req, res) { \n"
    final = final + "if (typeof req.body.name !== 'undefined' && typeof req.body.pass !== 'undefined') { \n"
    final = final + "proxmox = require('../node-proxmox/lib/proxmox')(req.body.name + '@pve', req.body.pass, proxmoxServerIp); \n"
    final = final + "proxmox." + funcName + "("
    for arg in args:
        final =  final + "req.body." + arg + ", "

    final = final + " function (err, response) { \n"
    final = final + "if (err) { \n"
    final = final + "console.log(err); \n res.send(err)"
    final = final + "} else { \n"
    final = final + "data = JSON.parse(response); \n res.json(data.data); \n }"
    final = final + "}); \n } \n }); \n"

    f.write(final)

f.close()
