import os
import sys



if len(sys.argv) < 2:
  print(" Usage:python create_cmnd.py rinv alpha ")
  sys.exit(1)
    

rinv = sys.argv[1]
# alpha = sys.argv[2]
lambdas = sys.argv[2]

# fname = "/home/Storage/MG5_Study_Group/Cards/Scan_rinv_alpha_md5/SVJ_" + str(rinv) + "_" + str(lambdas) + ".cmnd"
fname = "/home/Storage/MG5_Study_Group/Cards/from_my_10/SVJ_" + str(rinv) + "_" + str(lambdas) + ".cmnd"



rinv = float(rinv)/10.
#fix mass of dark scalar mesons
mass = 20.0
# mass = 100.0
# mass = 200.0
lambdas = float(lambdas)
# lambdas = float(alpha)/10.

Nc = 2
NFf = 2
NBf = 0

n=6 # number of Decimal places you want

f = open(fname, 'w')
#--------------------------------------------------------------- Settings used in the main program.
f.write('Main:numberOfEvents = 20000 \n') # Number of events
f.write('Main:timesAllowErrors = 3 \n') # 
#---------------------------------------------------------------- Settings related to output in init(), next() and stat()      
# f.write('Init:showChangedSettings = on  \n')
# f.write('Init:showChangedParticleData = off \n')
# f.write('Random:seed = '+str((i+1)*100)+'\n') #change random seed
f.write('Next:numberCount = 1000 \n') # print the progress per 1000 events
f.write('Next:numberShowInfo = 1 \n') 
f.write('Next:numberShowProcess = 1 \n')
f.write('Next:numberShowEvent = 0 \n')
f.write(' \n')
#-------------------------------------------------------------   ignore these particle 
f.write('4900001:m0 = 50000 \n')
f.write('4900002:m0 = 50000 \n')
f.write('4900003:m0 = 50000 \n')
f.write('4900004:m0 = 50000 \n')
f.write('4900005:m0 = 50000 \n')
f.write('4900006:m0 = 50000 \n')
f.write('4900011:m0 = 50000 \n')
f.write('4900012:m0 = 50000 \n')
f.write('4900013:m0 = 50000 \n')
f.write('4900014:m0 = 50000 \n')
f.write('4900015:m0 = 50000 \n')
f.write('4900016:m0 = 50000 \n')
f.write('\n')
#-------------------------------------------------------------- Hidden Valley
f.write('HiddenValley:Ngauge = ' +str(Nc)+'\n') # Number of gauge
f.write('HiddenValley:alphaOrder = 1 \n') # alpha is running
f.write('HiddenValley:Lambda = ' +str(lambdas)+'\n') # lamda_d
f.write('HiddenValley:nFlav  = '+str(NFf)+' \n') # alpha is running
f.write('HiddenValley:spinFv = 0 \n')
# f.write('HiddenValley:alphaFSR = ' +str(lambdas)+' \n') 
f.write('HiddenValley:FSR = on \n')
f.write('HiddenValley:fragment = on \n')
f.write('HiddenValley:pTminFSR = '+ str(1.1 * lambdas)+ '\n')
f.write('HiddenValley:probVector = '+str(0.75)+ '\n')
f.write('\n')
#------------------------------------------------------------------------------ Dark Particle setting
f.write('4900101:m0 = '+str(mass / 2) +'\n')
f.write('4900101:mWidth = '+ str(mass / 100)+ '\n')
f.write('4900101:mMin = '+str(mass / 2 - mass / 100)+'\n')
f.write('4900101:mMax = '+str(mass / 2 + mass / 100)+'\n')

# f.write('\n')
# f.write('4900111:m0 = '+str(mass)+'\n')
# f.write('4900113:m0 = '+ str(mass)+'\n')

# #off-diagonal mesons
# #spin 0 diagonal 
# f.write('4900211:m0 = '+ str(mass)+'\n')
# #spin 1 diagonal 
# f.write('4900213:m0 = '+ str(mass)+'\n')


f.write('\n')
f.write('4900111:m0 = '+str(mass)+'\n')
f.write('4900113:m0 = '+ str(mass)+'\n')
f.write('4900211:m0 = '+ str(mass / 2.0 - 0.01)+'\n')
f.write('4900213:m0 = '+ str(mass / 2.0 - 0.01)+'\n')


f.write(' \n')
f.write('4900111:onechannel = 1 ' +str(1.0 - rinv) +' 91 -3 3 \n')
f.write('4900111:addchannel = 1 ' +str(rinv) +' 0 4900211 -4900211 \n')
f.write(' \n')
f.write('4900113:onechannel = 1 ' +str(round((1 - rinv) / 5.,n)) +' 91 -1 1 \n')
f.write('4900113:addchannel = 1 ' +str(round((1 - rinv) / 5.,n)) +' 91 -2 2 \n')
f.write('4900113:addchannel = 1 ' +str(round((1 - rinv) / 5.,n)) +' 91 -3 3 \n')
f.write('4900113:addchannel = 1 ' +str(round((1 - rinv) / 5.,n)) +' 91 -4 4 \n')
f.write('4900113:addchannel = 1 ' +str(round((1 - rinv) / 5.,n)) +' 91 -5 5 \n')
f.write('4900113:addchannel = 1 ' +str(rinv) +' 0 4900213 -4900213 \n')
f.write(' \n')
#------------------------------------------------------------------------------ Jet matching
f.write("JetMatching:merge = on \n")
f.write("JetMatching:setMad = on \n")
f.write('JetMatching:scheme = 1 \n')
f.write('JetMatching:jetAlgorithm = 2 \n')
f.write('JetMatching:exclusive = 2 \n')
f.write('JetMatching:nJetMax = 2 \n')
f.write(' \n')

## New Change 2020/08/09
# f.write('JetMatching:doMerge = ickkw \n') #ickkw
f.write('JetMatching:qCut = 100 \n') #xqcut ## New Change 2020/08/11
f.write('JetMatching:nQmatch = 5 \n') #maxjetflavor
f.write('JetMatching:clFact = 1.0 \n') #alpsfact
# f.write('LHEFInputs:nSubruns=1\n') 
f.write(' \n')


f.write('Beams:frameType = 4 \n')
# f.write('Beams:LHEF = /home/Storage/MG5_Study_Group/sig_schannel_wz_auto/Events/run_02/unweighted_events.lhe \n') # where your LHE file is
f.write('Beams:LHEF = /home/Storage/MG5_Study_Group/sig_schannel_up2jets_wz_auto_md10/Events/run_04/unweighted_events.lhe \n') 
# f.write('Beams:LHEF = /home/Storage/MG5_Study_Group/events_100_100000_0.lhe \n') 

f.close()