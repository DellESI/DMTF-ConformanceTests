#!/usr/bin/env python3

excludes = {
        '6.1.8.1':'Looks like a misconceived attempt to POST to Sessions \nAND password too short. Issue raised w DMTF 12/14',
        '6.4.32':'test expects 200, we return 204 - no content',
        '6.5.6.6':'URI mangling makes no sense. The test obviously looking for 301 to check for location.',
        '6.5.6.8':'confusing, but I dont think we support if-none-match',
        '6.5.6.9':'test mangled the odata.id. But this just removes trailing / so GET succeeded so  result 200, not 404.  Issue submitted 12/15',
        '6.5.6.10':'bug in test issue reported to DMTF #135',
        '6.5.8': 'misspelled propert reported to Josh and Paul',
        '6.5.23.1': 'Passes Now !!!',
        '7.2.1'  : 'It claims namespace not there but I see it. ???',
        '7.5.3': 'Description, LongDescription Annotation confusion- DMTF Isuues 56 & 57',
        '7.5.5': 'Description, LongDescription Annotation confusion- DMTF Isuues 56 & 57',
        '7.5.8': 'Description, LongDescription Annotation confusion- DMTF Isuues 56 & 57',
        '7.5.9': 'Description, LongDescription Annotation confusion- DMTF Isuues 56 & 57',
        '7.5.10':'Description, LongDescription Annotation confusion- DMTF Isuues 56 & 57',
        '7.5.13.xml': 'Bad logic, issue submitted to DMTF 12/15',
        '7.5.16':'Description, LongDescription Annotation confusion- DMTF Isuues 56 & 57',
            }
comments = {
        '6.4.23': '  ___ test correct, should return 405, but I dont like the PATCH data',
        '6.5.26': '  ___ oops, passes now'
            }
efile = input("Name of the stdout of Conformance Checker )")

f = open(efile,'r')
lines = f.readlines()
f.close()

fails = {}
errors = 0
for line in lines:
    line = line.strip()
    if 'FAIL' in line:
        if 'FAILures' in line: continue
        pts = line.split()
        assrt =  pts[2]
        assrt = assrt.replace(':','')
        if assrt in excludes:
            print (line + ' Exclude: ' + excludes[assrt])
        elif assrt in comments:
            print (line + comments[assrt])
            errors += 1 
        else:
            print (line)
            errors += 1 
        #print (line)
        fails[assrt] = ''
print ('')
print (errors, 'Errors')

print('')
print('')
failed = False
for line in lines:
    line = line.strip()
    if not line: continue
    if line[0:11] == '---> Assert':
        pts = line.split()
        assrt = pts[2]
        assrt = assrt.replace(':','')
        if assrt in fails:
            failed = True
            print ('')
    if failed: print (line)
    if line[0:11] == '<--- Assert':
        failed = False

