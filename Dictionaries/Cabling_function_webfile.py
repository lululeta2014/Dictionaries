#!/usr/bin/env python
import re
import urllib
import os


def creaciontxt():
        archi=open('data_webfile.txt','w')
        archi.close()

def Dictionary(filename,userkey):

    FiletxtFEDs = open(filename,'r')

    Fd = "FedCrate/FedSlot/FedId/FeUnit/FeChan/FedCh"
    Fc = "FecCrate/FecSlot/FecRing/CcuAddr/CcuChan"
    D = "DcuId/DetId"
    Ll = "LldChan/APV0/APV1"
    pair = "pairNumber/nPairs/nStrips"
    DC = "DCU/MUX/PLL/LLD"

    CablingInfoDict={}

    # Creating lists
    FedCrateList = []
    FedSlotList = []
    FedIdList=[]
    FeUnitList=[]
    FeChanList=[]
    FedChList=[]

    FecCrateList=[]
    FecSlotList=[]
    FecRingList=[]
    CcuAddrList=[]
    CcuChanList=[]
    
    DcuIdList=[]
    DetIdList=[]

    LldChanList=[]
    APV0List=[]
    APV1List=[]
    pairNumberList=[]
    nPairsList=[]
    nStripsList=[]

    DCUList=[]
    MUXList=[]
    PLLList=[]
    LLDList=[]


    for line in FiletxtFEDs:
        if Fd in line:
            pattern = re.split('\W+',line)
            FedCrateList.append(pattern[7])
            FedSlotList.append(pattern[8])
            FedIdList.append(pattern[9])
            FeUnitList.append(pattern[10])
            FeChanList.append(pattern[11])
            FedChList.append(pattern[12])
        if Fc in line:
            pattern = re.split('\W+',line)
            FecCrateList.append(pattern[6])
            FecSlotList.append(pattern[7])
            FecRingList.append(pattern[8])
            CcuAddrList.append(pattern[9])
            CcuChanList.append(pattern[10])
        if D in line:
            pattern = re.split('\W+',line)
            DcuIdList.append(pattern[3])
            DetIdList.append(pattern[4])
        if Ll in line:
            pattern = re.split('\W+',line)
            LldChanList.append(pattern[4])
            APV0List.append(pattern[5])
            APV1List.append(pattern[6])
        if pair in line:
            pattern = re.split('\W+',line)
            pairNumberList.append(pattern[4])
            nPairsList.append(pattern[5])
            nStripsList.append(pattern[6])
        if DC in line:
            pattern = re.split('\W+',line)
            DCUList.append(pattern[6])
            MUXList.append(pattern[7])
            PLLList.append(pattern[8])
            LLDList.append(pattern[9])
        
    if userkey == ("a" or "c"):

        for fedcrate,fedslot,fedid,feunit,fechan,fedch,feccrate,fecslot,fecring,ccuaddr,ccuchan,dcuid,detid,lldchan,apv0,apv1,pairnumber,npairs,nstrips,dcu,mux,pll,lld  in zip(FedCrateList,FedSlotList,FedIdList,FeUnitList,FeChanList,FedChList,FecCrateList,FecSlotList,FecRingList,CcuAddrList,CcuChanList,DcuIdList,DetIdList,LldChanList,APV0List,APV1List,pairNumberList,nPairsList,nStripsList,DCUList,MUXList,PLLList,LLDList):

            if detid in CablingInfoDict.keys(): 
                CablingInfoDict[detid].update({pairnumber:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}})

            else:
                CablingInfoDict.update({detid:{pairnumber:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}}})


    if userkey == ("b" or "d"):

        for fedcrate, fedslot, fedid, feunit, fechan, fedch, feccrate, fecslot, fecring, ccuaddr, ccuchan, dcuid, detid, lldchan, apv0, apv1, pairnumber, npairs, nstrips, dcu, mux, pll, lld in zip(FedCrateList, FedSlotList, FedIdList, FeUnitList, FeChanList, FedChList, FecCrateList, FecSlotList, FecRingList, CcuAddrList, CcuChanList, DcuIdList, DetIdList, LldChanList, APV0List, APV1List, pairNumberList, nPairsList, nStripsList, DCUList, MUXList, PLLList, LLDList): 
  
            if fedid in CablingInfoDict.keys(): 
                CablingInfoDict[fedid].update({fedch:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}})
               
            else:
                 CablingInfoDict.update({fedid:{fedch:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}}})

    
    return CablingInfoDict
    


print "\n\n You can find the name of the .txt Cabling file on this web page:\n https://test-stripdbmonitor.web.cern.ch/test-stripdbmonitor/CondDBMonitoring/cms_orcoff_prod/CMS_COND_31X_STRIP/DBTagCollection/SiStripFedCabling/SiStripFedCabling_GR10_v1_hlt/CablingLog/ \n"

print "Type the name:\n"

input1 = raw_input(">")

url='https://test-stripdbmonitor.web.cern.ch/test-stripdbmonitor/CondDBMonitoring/cms_orcoff_prod/CMS_COND_31X_STRIP/DBTagCollection/SiStripFedCabling/SiStripFedCabling_GR10_v1_hlt/CablingLog/'

#urllib.urlretrieve(url, filename='CablingInfo_Run100356.txt')
urllib.urlretrieve(url+input1, filename= input1)


print "Select one of the following options:\n"

print " a) A list of all DetId's of the file dumped in a txt file (and a trackermap) \n "
print " b) A list of DetId(s) connected to some FED(s) dumped in a txt file (and a trackermap) \n"
print " c) Information about a certain module or modules \n"
print " d) Information about a certain FED or FED's \n"
input2 = raw_input(">")

ourdictionary = Dictionary(input1,input2)

creaciontxt()
archi=open('data_webfile.txt','w')

if input2== "a":
	print "data_webfile.txt for tracker map done "
	for a in ourdictionary.keys():
	    archi.write(str(int(a,16)))
	    archi.write("  5")
	    archi.write('\n')

	archi.close
	os.system('print_TrackerMap data_webfile.txt TrackerMap TrackermapDetIds.png 2400 False True 999 -999')
		

if input2== "b":
	input3=raw_input( "Type the Fedid's numbers separated by a single space (at most 9)\n ")

	inputfedid_list=input3.split(' ')

	print "data_webfile.txt for tracker map done"


	j=0
	for p in inputfedid_list:
		j+=1
                #print j 
		for q in ourdictionary[p].keys():
			#print ourdictionary["164"][cha]["DetId"]
			archi.write(str(int(ourdictionary[p][q]["DetId"],16)))
			archi.write(" ")
			archi.write(str(j))
			archi.write('\n')
        
        archi.close()
        os.system('print_TrackerMap data_webfile.txt TrackerMap TrackermapDetIdtoFeds.png 2400 False True 999 -999')


			
if input2=="c":
      input3 = raw_input("Enter the DetId's separated by a single space\n > ")
      input_list3=input3.split(' ')
      
      input4 = raw_input("Enter the pairNumber corresponding to each DetId separated by a single space\n >")
      input_list4=input4.split(' ')
      
      input5=raw_input( "Enter the data you need separated by comas (FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD)?: \n ")
      input_list5=input5.split(',')

      for i,j in zip(input_list3,input_list4):
          print "For DetID : %r with pairNumber: %r "%(i,j)
	  for k in input_list5:
	      print " %r is:%r "%(k,ourdictionary[i][j][k])

if input2=="d":
      input3 = raw_input("Enter the FedId's separated by a single space\n > ")
      input_list3=input3.split(' ')

      input4 = raw_input("Enter each FedCh's corresponding to each FedId separated by a single space\n >")
      input_list4=input4.split(' ')

      input5=raw_input( "Enter the data you need separated by a single space (FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAd\dr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD)?: \n ")
      input_list5=input5.split(' ')

      for i,j in zip(input_list3,input_list4):
	  print "For FedId : %r with FedCh : %r "%(i,j)
	  for k in input_list5:
	      print " %r is:%r "%(k,ourdictionary[i][j][k])
									    

#print "in order to get tracker map type the following command in the window: print_TrackerMap data_webfile.txt TITLE figureNAME.png 2400 False True 999 -999"
       
#archi.close()

