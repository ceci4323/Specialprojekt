import sys

#defines function that opens the file
def openfile(name, mode):
    #opens the file
    try:
        infile = open(name, mode)
    #error handling in case the file cannot be opened
    except IOError as error:
        sys.stdout.write("Can't read/write file, reason: " + str(error) + "\n")
        sys.exit(1)
    return infile

#defines function that processes the file and creates output file
def processfile(rfile, wfile):
    #iterates through file
    for line in rfile:
        #splits datasetlist 
        datasetlist = line.split(' pp ')
        #defines first protein
        str1 = datasetlist[0]
        #defines second protein and strips of newline
        str2 = datasetlist[1].rstrip()
        #if the first protein on the line is not the same as the second protein, write the line into the new file
        if str1 != str2:
            wfile.write(line)
    #closes file
    rfile.close()
    wfile.close()
    return

readfile = openfile("virtualpulldown.vp.sif",'r')
writefile = openfile("virtualpulldown.noself.sif", 'w')
processfile(readfile, writefile)
