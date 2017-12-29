#!/usr/bin/python
import sys
import pymysql
import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
tempCPN = sys.argv[1]

db = pymysql.connect("willits.cisco.com","cadlibportal_vpl","fAVqWE7C2ECMPBYu","cadlibportal")
cursor = db.cursor()

def getVerifiedFps(cpn):
    #print("select PACKAGE_NAME, REVISION, PART_SOURCE from vpls where PART_NUM = '%s'" %(cpn))
    cursor.execute("select PACKAGE_NAME, REVISION, PART_SOURCE from vpls where PART_NUM = '%s' and PART_STATUS = 'Active'" %(cpn))
    results = cursor.fetchall()
    verifiedList=[]
    for row in results:
        dictFp={}
        dictFp['footprint'] = row[0]
        dictFp['revision'] = row[1]
        dictFp['source'] = row[2]
        dictFp['verified'] = "Yes"
        verifiedList.append(dictFp)
    #print(verifiedList)
    return verifiedList

def getAllegroFps(cpn):
    cursor.execute("select jedec_type, alt_jedec_type from partdata where partnumber = '%s'" %(cpn))
    results = cursor.fetchall()
    allegroList = []

    allegroNameList = []
    for row in results:
        allegroNameList.append(row[0].upper())
        if not row[1].strip()=="":
            alts = row[1].split(',')
            for alt in alts:
                allegroNameList.append(alt.strip().upper())
    allegroNameList = list(set(allegroNameList))

    for item in allegroNameList:
        dictFp={}
        dictFp['footprint'] = item
        dictFp['revision'] = getFpsRev(item)
        dictFp['source'] = "ALLEGRO"
        dictFp['verified'] = "No"
        allegroList.append(dictFp)

    #print(allegroList)
    return allegroList

def getFpsRev(fp):
    cursor.execute("select revision from jedecrevs where jedecinfo_id = \
        (select id from jedecinfos where jedec ='%s') and current_rev='1'" %(fp))
    result = cursor.fetchone()
    revision = ""
    if not str(result) == "None":
        revision = result[0]
    return revision.upper()

def getV2AFps(cpn):
    dbV2A = pymysql.connect("dxdb-rtp.cisco.com","v2auser","readonly","v2a_dxdb")
    cursorV2A = dbV2A.cursor()
    cursorV2A.execute("select pkgType, rev from MCAD_INFO where ciscoPN = '%s'" %(cpn))
    results = cursorV2A.fetchall()

    view2allList=[]
    for row in results:
        dictFp={}
        dictFp['footprint'] = row[0].upper()
        dictFp['revision'] = row[1].upper()
        dictFp['source'] = "VIEW2ALL"
        dictFp['verified'] = "No"
        view2allList.append(dictFp)
    #print(view2allList)
    dbV2A.close()
    return view2allList

def mergeFps(cpn):
    verifiedList = getVerifiedFps(cpn)
    # allegroList = getAllegroFps(cpn)
    # view2allList = getV2AFps(cpn)

    allList = getAllegroFps(cpn) + getV2AFps(cpn)
    #print(allList)
    for itemVL in verifiedList:
        for itemAL in allList:
            if itemAL['footprint'] == itemVL['footprint'] and itemAL['revision'] == itemVL['revision']:
                allList.remove(itemAL)
    allList = verifiedList + allList
    for item in allList:
        print(item)      
    #view2allList = getV2AFps(cpn)


mergeFps(tempCPN)
#getV2AFps("15-13376-01")
#getFpsRev('QFN-22-S0')
#getAllegroFps("15-13376-01")
#getVerifiedFps("29-1998-01")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
db.close()

