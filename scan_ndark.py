import uproot
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


def MyFunction(file):
    GenParticle = np.array([file["Particle.Status"].array(),
                            file["Particle.PID"].array(),
                            file["Particle.M1"].array(),
                            file["Particle.M2"].array(),
                            file["Particle.D1"].array(),
                            file["Particle.D2"].array(),
                            file["Particle.PT"].array(),
                            file["Particle.Eta"].array(),
                            file["Particle.Phi"].array(),
                            file["Particle.Mass"].array()])

    Jet = np.array([file["Jet.PT"].array(),
                            file["Jet.Eta"].array(),
                            file["Jet.Phi"].array(),
                            file["Jet.Mass"].array()
                           ])

    Event_Weight = np.array(file["Event.Weight"].array())

    return GenParticle, Jet, Event_Weight


def Preselection(Jet):
    twojet_invariantmass = []
    survived_list = []
    for i in range(len(Jet[0])):
        if len(Jet[0][i]) < 2:
            continue

        if Jet[0][i][0] < 440 or Jet[0][i][1] < 60:
            continue

        if np.abs(Jet[1][i][0]-Jet[1][i][1]) > 1.2:
            continue

        twojet_invariantmass.append(M(Jet[0][i][0],Jet[1][i][0],Jet[2][i][0],Jet[3][i][0],Jet[0][i][1],Jet[1][i][1],Jet[2][i][1],Jet[3][i][1]))

        survived_list.append(i)

    print("There are {} events.".format(len(twojet_invariantmass)))
    
    return np.array(twojet_invariantmass), np.array(survived_list)


def Check_r_inv(GenParticle):
    invis_count, vis_count = 0, 0
    Ndark = 0
    for i in range(len(GenParticle[1])):
        for j in range(len(GenParticle[0][i])):
            PID = GenParticle[1][i][j]
            M1 = GenParticle[2][i][j]
            M2 = GenParticle[3][i][j]
            D1 = GenParticle[4][i][j]
            D2 = GenParticle[5][i][j]
            status = GenParticle[0][i][j]
            
            if (abs(PID) == 4900111) and (abs(GenParticle[1][i][D1]) != 4900111) and (abs(GenParticle[1][i][D2]) != 4900111):
                if (abs(GenParticle[1][i][D1]) != 3) and (abs(GenParticle[1][i][D2]) != 3):
                    invis_count += 1

            if (abs(PID) == 4900111) and (abs(GenParticle[1][i][D1]) != 4900111) and (abs(GenParticle[1][i][D2]) != 4900111):
                if (abs(GenParticle[1][i][D1]) == 3) or (abs(GenParticle[1][i][D2]) == 3):
                    vis_count += 1

            if (abs(PID) == 4900113) and (abs(GenParticle[1][i][D1]) != 4900113) and (abs(GenParticle[1][i][D2]) != 4900113):
                if (abs(GenParticle[1][i][D1]) > 490000) or (abs(GenParticle[1][i][D2]) > 490000):
                    invis_count += 1
#                     print("{:^5}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^8.5}{:^8.5}{:^8.5}{:^8.5}".format( \
#         j, GenParticle[0][i][j],  GenParticle[1][i][j], GenParticle[2][i][j], GenParticle[3][i][j],
#         GenParticle[4][i][j], GenParticle[5][i][j], GenParticle[6][i][j], GenParticle[7][i][j] ,GenParticle[8][i][j], GenParticle[9][i][j]))




            if (abs(PID) == 4900113) and (abs(GenParticle[1][i][D1]) != 4900113) and (abs(GenParticle[1][i][D2]) != 4900113):
                if (abs(GenParticle[1][i][D1]) < 6) or (abs(GenParticle[1][i][D2]) < 6):
                    vis_count += 1

                    
#             if (abs(PID) == 4900211) and (( abs(GenParticle[1][i][M1])== 4900101) or (abs(GenParticle[1][i][M2]) == 4900101)):
#                     Ndark += 1

#             if (abs(PID) == 4900213) and (( abs(GenParticle[1][i][M1])== 4900101) or (abs(GenParticle[1][i][M2]) == 4900101)):
#                     Ndark += 1
                    
#             if (abs(PID) == 4900111) and (( abs(GenParticle[1][i][M1])== 4900101) or (abs(GenParticle[1][i][M2]) == 4900101)):
#                     Ndark += 1
                    
#             if (abs(PID) == 4900113) and (( abs(GenParticle[1][i][M1])== 4900101) or (abs(GenParticle[1][i][M2]) == 4900101)):
#                     Ndark += 1

            if (abs(PID) == 4900211) and (status == 1):
                    Ndark += 1

            if (abs(PID) == 4900213) and (status == 1):
                    Ndark += 1
                    
                    
    print("There are {} events.".format(len(GenParticle[0])))
    print("There are Dark meson {}  decay into invisible particle.".format(invis_count))
    print("There are Dark meson {}  decay into visible particle.".format(vis_count))
    print("r_inv = {:^4.4f} ".format(invis_count/(invis_count+vis_count)))
    
    print("There are {} stable Dark mesons.".format(Ndark))
    print("Average = {:^4.4f} ".format(Ndark/len(GenParticle[0])))
    return invis_count/(invis_count+vis_count), Ndark/len(GenParticle[0])



ndark = np.zeros((8,11))
lambda_d = [10,50,100,150,200,250,300,350]
for i in range(0,11):
    for j, element in enumerate(lambda_d):
        roor_file_path = "/home/Storage/MG5_Study_Group/ROOT/Scan_rinv_alpha/SVJ_"+str(i)+"_"+str(element)+".root"
        file = uproot.open(roor_file_path)["Delphes;1"]
        GenParticle, _, _ = MyFunction(file)
        ndark[j,i] = Check_r_inv(GenParticle)[1]
np.save("./ndark_10", ndark)