import re
import pdftotext
import pprint
from app import airportdata

keys = ['data', 'year', 'notam_no', 'class', 'timestamps', 'priority_score', 'phrase', 'widget', 'airport', 'coords']
daysall = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
def pdf_to_notams(filename):
    data_list = []
    with open(filename,"rb") as f:
        pdf = pdftotext.PDF(f)
        for i in range(len(pdf)):
            data_list.append(pdf[i])
    data = ""
    for page in data_list:
        data += "\n".join(page.split('\n')[1:-2])
    notams = []
    notam_no = re.findall('[0-9][a-zA-Z][0-9]+\/[0-9]+',data)
    for i in range(len(notam_no)-1):
        notams.append(notam_no[i]+data[data.find(notam_no[i])+len(notam_no[i]): data.find(notam_no[i+1])])
    notams.append(notam_no[-1]+data[data.find(notam_no[-1]):])
    return notams

def getSubjects(s):
    sall = ['ABN', 'ACC', 'ACFT', 'ACR', 'AFD', 'AGL', 'ALS', 'ALTM', 'ALSTG', 'AMGR', 'AMOS', 'AP', 'APCH', 'AP', 'APP', 'ARFF', 'ASOS', 'ATC', 'ATCCC', 'ATIS', 'AUTOB', 'AWOS', 'AWY', 'AZM', 'BA', 'BA', 'BA', 'BC', 'BCN', 'BERM', 'CAAS', 'CAT', 'CBAS', 'CBSA', 'CCAS', 'CCLKWS', 'CCSA', 'CD', 'CDAS', 'CDSA', 'CEAS', 'CESA', 'CFR', 'CGAS', 'CHAN', 'CHG', 'CIG', 'CK', 'CL', 'CNTRLN', 'COM', 'DME', 'DRFT', 'EFAS', 'ENG', 'FAC', 'FAF', 'FAN', 'FDC', 'FI/T', 'FI/P', 'FRH',  'FSS', 'GC', 'GCA', 'GCO', 'GOVT', 'GP', 'GPS', 'HAA', 'HAT', 'HDG', 'HEL', 'HELI', 'HIRL', 'HIWAS', 'HLDG', 'HP', 'IAF', 'IAP', 'INBD', 'ID', 'IDENT', 'IF', 'ILS', 'IM', 'IMC', 'INSTR', 'IR', 'LAA', 'LAWRS', 'LB', 'LC', 'LOC', 'LCTD', 'LDA', 'LGT', 'LIRL', 'LLWAS', 'LM', 'LLZ', 'LO', 'LRN', 'LSR', 'LT', 'MAG', 'MAINT', 'MALS', 'MALSF', 'MALSR', 'MAPT', 'MCA', 'MDA', 'MEA', 'MED', 'MIN', 'MIRL', 'MKR', 'MLS', 'MM', 'MRA', 'MSA', 'MSAW', 'MSL', 'MU', 'MUD', 'MUNI', 'N', 'NA', 'NAV', 'NB', 'NDB', 'NE', 'NGT', 'NM', 'NMR', 'NONSTD', 'NOPT', 'NR', 'NTAP', 'OBSC', 'OBST', 'OM', 'ORIG', 'OTS', 'OVR', 'PAEW', 'PAX', 'PAPI', 'PAR', 'PARL', 'PAT', 'PCL', 'PERM', 'PJE', 'PLA', 'PLW', 'PN', 'PPR', 'PRN', 'PROC', 'PROP', 'PSR', 'PTCHY', 'PTN', 'PVT', 'RAIL', 'RAMOS', 'RCAG', 'RCL', 'RCLL', 'RCO', 'REC', 'REIL', 'RELCTD', 'REP', 'RLLS', 'RMNDR', 'RMK', 'RNAV', 'RPLC', 'RQRD', 'RRL', 'RSR', 'RSVN', 'RT', 'RTE', 'RTR', 'RTS', 'RUF', 'RVR', 'RVRM', 'RVRR', 'RVRT', 'RWY', 'SAWRS', 'SDF', 'SE', 'SFL', 'SIMUL', 'SIR', 'SKED', 'SLR', 'SN', 'SNBNK', 'SSALF', 'SSALR', 'SSALS', 'SSR', 'STA', 'STAR', 'SVN', 'TACAN', 'TAR', 'TDWR', 'TDZ', 'TDZ', 'TEMPO', 'TFC', 'TFR', 'TGL', 'TIL', 'TM', 'TMPA', 'TRML', 'TWR', 'TWY', 'UAV', 'UFN', 'VASI', 'VDP', 'VICE', 'VIS', 'VMC', 'VOL', 'VOR', 'VORTAC', 'MSSR', 'MACHINERY', 'FREQ', 'AERODOME', 'BIRD', 'PARACHUTE', 'RUNWAY', 'TAXIWAY', 'ALTITUDE', 'AD', 'AIRSPACE']
    
    # regs = '([^A-Za-z]'+('[^A-Za-z])|([^A-Za-z]'.join(sall))+'[^A-Za-z])'
    # print(regs)
    found = set()
    for salle in sall:
        try:
            found.add(re.findall('[^A-Za-z]'+salle+'S{0,1}[^A-za-z]', s)[0][1:-1])
        except:
            pass
    
    return list(found)

def getMod(s):
    aall = ['CLSD', 'CLOSED', 'CLOSURE', 'AVBL', 'RELOCATED', 'PERMITTED', 'COMMISSIONED', 'RENAMED', 'RESTRICTED', 'NA', 'DEPLOYED','WITHDRAWN' , 'OBSTACLES', 'PROC', 'RESERVED', 'INTRODUCED', 'INTRODUCTION', 'GRANT', 'GRANTED', 'UNUSABLE', 'USABLE', 'AMENDED', 'ERECTED', 'LGTD', 'MAINT', 'MAINTANENCE', 'SERVICABLE', 'UNSERVICEABLE', 'ACTIVITY', 'BUSY', 'USABLE', 'RESTRICTIONS']
    found = set()
    for aalle in aall:
        try:
            #print(re.findall('[^A-Za-z]'+aalle+'[^A-za-z]', s)[0][1:-1])
            found.add(re.findall('[^A-Za-z]'+aalle+'[^A-za-z]', s)[0][1:-1])
        except:
            pass
    #print(list(found))
    found = list(found)
    for i in range(len(found)):
        if len(re.findall('NO(\w+){0,2} '+found[i], s)) > 0 or len(re.findall('NOT(\w+){0,2} '+found[i], s)) > 0:
            found[i]='not '+found[i]
    return list(found)

def getExtra(s):
    aall = ['OPS','LDG', 'TAXING','TAX', 'TOWING', 'CROSSING', 'TKOF', 'PRKG', 'STANDS', 'LTN', 'THR', 'THRESHOLD', 'WIP', 'COORD']
    found = set()
    for aalle in aall:
        try:
            #print(re.findall('[^A-Za-z]'+aalle+'[^A-za-z]', s)[0][1:-1])
            found.add(re.findall('[^A-Za-z]'+aalle+'[^A-Za-z]', s)[0][1:-1])
        except:
            pass
    
    return list(found)

def getDaysTimes(s):
    punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''

    no_punct = ""
    for c in s:
        if not (c in punctuations):
            no_punct = no_punct + c
        else:
            no_punct+=' '
    
    s = no_punct
    s = s.replace('\n', '')
    s = s.split(' ')
    form = -1
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    toret = []
    ddict = {}
    dot = ''
    #print(s)
    for w in s:
        if w in days:
            
            form = 0 if form == -1 else form
            if dot == 't' and form == 0:
                toret.append(ddict.copy())
                ddict = {}
            ddict['days']=ddict.get('days', [])+[w]
            dot = 'd'
        elif ('-' in w and len(w.split('-'))==2 and w.split('-')[0].isdigit() and w.split('-')[1]) or w == 'H24':
            
            form = 1 if form == -1 else form
            if dot == 'd' and form == 1:
                toret.append(ddict.copy())
                ddict = {}
            ddict['time']=ddict.get('time', [])+[w]
            dot = 't'
    toret.append(ddict.copy())
            
    return toret

#getDaysTimes("1A166/19\n  MON 0430-2359,TUE WED THU FRI H24, SAT 0000-1230\n  PORTION OF RWY 32 FM BEGINNING UP TO THR RWY 32\n   NOT AVBL FOR TAX. REMAINING PORTION OF RWY\n   14/32 AVBL FOR TAX. TOWING OF ACFT TO/FM APN L\n   WILL BE PERMITTED UNDER FLW ME SER WITH 01HR\n   NOTICE.EMERG RESTORATION TIME 03HR FM SUNRISE\n   TO SUNSET AND 04HR FM SUNSET TO SUNRISE\n")

def valuetype(s):
    aall = ['LENGTH','WIDTH','PSN', 'POSITION', 'ALTITUDE', 'DISTANCE','DIST', 'FREQ','FREQUENCY','SPEED', 'HEIGHT', 'COORD', 'ANGLE', 'DAYS', 'DATES','ELEVATION', 'ELEV']
    found = set()
    for aalle in aall:
        try:
            #print(re.findall('[^A-Za-z]'+aalle+'[^A-za-z]', s)[0][1:-1])
            found.add(re.findall('[^A-Za-z]'+aalle+'[^A-Za-z]', s)[0][1:-1])
        except:
            pass
    if 'DEG' in s.split():
        found.add('ANGLE')
    return list(found)

def rushang():
    # priority thing ko call
    pass

def extract(filename='NOTAM.pdf'):
    notams = pdf_to_notams(filename)
    dataout=[]

    for notam in notams:
        data = tags(notam)
        dataout.append(data)
    pprint.pprint(dataout)
    return dataout

def tags(notam):
    upl = notam.split('\n')[0].split('/')
    notamno = upl[0]
    # year = upl[1][:2]
    clas = notamno[1]
    times = re.findall('[0-9]{4}-[0-9]{4}', notam)
    days = list(filter(lambda x: x in notam,daysall ))
    runways = list(set(re.findall('RWY *[0-9][0-9A-Za-z/]+', notam)))
    taxiways = list(set(re.findall('TWY *[0-9][0-9A-Za-z/]+', notam)))
    
    ls = notam.split('\n')
    for e in ls:
        if 'EAIP' in e:
            ls.remove(e)
    
    sentences = ' '.join(ls).replace('.\n', '. ').replace('+\n', '. ').replace('-\n', '. ').split('. ')
    # print(sentences)
    sentence_an = []
    for sentence in sentences:
        runs = list(set(re.findall('RWY *[0-9][0-9A-Za-z/]+', sentence)))
        taxis = list(set(re.findall('TWY *[0-9][0-9A-Za-z/]+', sentence)))
        coords = re.findall('[0-9]{6,7}.[0-9]{1,2}[N|E|W|S]', sentence)
        san = {}
        san['content'] = sentence
        san['subject'] = getSubjects(' '+sentence.replace('\n', ' ')+' ')
        san['mod'] = getMod(' '+sentence.replace('\n', ' ')+' ')
        san['extra'] = getExtra(' '+sentence.replace('\n', ' ')+' ')
        san['runways'] = runs
        san['taxiways'] = taxis
        #san['coords'] = coords
        san['daystimes']=getDaysTimes(sentence)
        san['valuetypes']=valuetype(sentence)
        sentence_an.append(san)
    data = {}
    #data['notamno']=notamno
    data['class']=clas
    data['content']='\n'.join(notam.split('\n')[1:])
    data['priority'] = rushang()
    data['runways']=runways
    data['taxiways']=taxiways
    #data['year']=year
    data['sentence_an']=sentence_an
    print(pprint.pprint(data))
    return data

def extract_is_back(notam):
    lines = notam.split('\n')
    header = lines[0]
    clas = header[0]
    notam_no = header[1:5]
    year = header.split()[0][-2:]
    typ = header.split()[1]
    if typ == 'NOTAMR':
        reference_to = header.split()[-1]
    qcode = notam.split('Q)')[1].split('/')[1]
    fir = notam.split('Q)')[1].split('/')[0].strip()
    a = notam.split('A)')[1].split('B)')[0].strip()
    firOfac = ''
    if a[-1]=='F':
        firOfac='FIR'
    else:
        firOfac='FAC'
    
    b = notam.split('B)')[1].split('C)')[0].strip()
    c = notam.split('C)')[1].split('D)')[0].strip()
    start = '20'+b[0:2]+'/'+b[2:4]+'/'+b[4:6]+' '+b[6:8]+':'+b[8:10]
    end = '20'+c[0:2]+'/'+c[2:4]+'/'+c[4:6]+' '+c[6:8]+':'+c[8:10]
    d = notam.split('D)')[1].split('E)')[0].strip()
    e = notam.split('E)')[1].split('F)')[0].strip()
    if 'F)' in notam:
        f = notam.split('F)')[1].split('G)')[0].strip()
        g = notam.split('G)')[1]

    sentences = e.replace('.\n', '. ').replace('+\n', '. ').replace('-\n', '. ').split('. ')
    # print(sentences)
    radiim = []
    coordm = []
    sentence_an = []
    for sentence in sentences:
        runs = list(set(re.findall('RWY *[0-9][0-9A-Za-z/]+', sentence)))
        radii = list(set(re.findall('RADIUS (\w+){0,2}[0-9]+ *[A-Z]{0,2}', sentence)))
        radiim.extend(radii)
        taxis = list(set(re.findall('TWY *[0-9][0-9A-Za-z/]+', sentence)))
        # coords = re.findall('[0-9]{6,7}.[0-9]{1,2}[N|E|W|S]', sentence)
        coords = re.findall('[0-9.]{6,}[N|E|W|S]', sentence)
        san = {}
        san['content'] = sentence
        san['subject'] = getSubjects(' '+sentence.replace('\n', ' ')+' ')
        san['mod'] = getMod(' '+sentence.replace('\n', ' ')+' ')
        san['extra'] = getExtra(' '+sentence.replace('\n', ' ')+' ')
        san['runways'] = runs
        san['taxiways'] = taxis
        san['coords'] = coords
        coordm.extend(coords)
        
        sentence_an.append(san)
    
    data = {}
    data['notam']=notam
    data['class'] = clas
    data['notam_no'] = notam_no
    data['firOfac']=firOfac
    data['starttime']=start
    data['endtime']=end
    data['sentence_an']=sentence_an
    data['a']=a
    data['b']=b
    data['c']=c
    data['d']=d
    data['e']=e
    if 'F) ' in notam:
        data['lower_limit']=f
        data['upper_limit']=g
        data['f']=f
        data['g']=g
    if firOfac == 'FAC':
        airport = {
            'icao': a,
            'name': airportdata.data[a]['name'],
            'lat': airportdata.data[a]['lat'],
            'lng':airportdata.data[a]['lng']
        }
        data['airport'] = airport
    else:
        dfir = {'VABF':'VABB', 'VIDF':'VIDD', 'VOMF':'VOMM', 'VECF':'VECC'}
        amod = dfir[a]
        airport = {
            'icao': amod,
            'name': airportdata.data[amod]['name'],
            'lat': airportdata.data[amod]['lat'],
            'lng':airportdata.data[amod]['lng']
        }
        data['airport'] = airport
    data['coords'] = coordm
    data['radii'] = radiim
    pprint.pprint(data)

    return data
    
   




