
# -------------------------------------------------------------
# PARAMETRIC STUDY (orchestrating algorithm)
# -------------------------------------------------------------
#
#   GM1: Recorded ground motion
#   GM2: Spectral approach
#   GM3: Filtered white noise
#
#   FEM1: Cantilever
#   FEM2: Simply supported beam
#   FEM3: T-frame
#   FEM4: Padgett bridge
#
# -------------------------------------------------------------


# Import external libraries
import matplotlib.pyplot as plt
import numpy as np


# # Spectral representation model parameters
# # parameter1Name = "Kanai-Tajimi Damping"
# # parameter1List = np.array([0.2])
# parameter2Name = "Kanai-Tajimi Frequency"
# parameter2List = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
# parameter3Name = "Kanai-Tajimi Sigma"
# parameter3List = np.array([200.0])
# ktDamping = []


# White noise based model parameters
parameter1Name = "Damping"
parameter1List = np.array([0.6])
parameter2Name = "Mean Frequency" # target variance for frequency other than 1, 2, 3, and 4 Hz in NOT normalised
# parameter2List = np.array([1.5])
parameter2List = np.array([0.5, 1.0, 1.5, 2.0131684841794817, 2.5, 3.0, 3.5])
parameter3Name = "Target Variance"
parameter3List = np.array([20000.0])
NonStationarity = False

# Finite element model parameters
parameter4Name = "Stiffness"
parameter4List = np.array([16000.0])
parameter5Name = "Mass"
parameter5List = np.array([100.0])


responseName = "Column Top Displacement"

# # Parameter for GM3 (the filtered white noise based ground motion)
# parameter1Name = "Damping"
# parameter1List = np.array([0.2])
# parameter2Name = "Kanai-Tajimi Frequency"
# parameter2List = np.array([1.0])
# parameter3Name = "Kanai-Tajimi Sigma"
# parameter3List = np.array([200.0])

# Create storage for the response from each run
response = np.ones((len(parameter2List), len(parameter4List)))

# Define delta-t for the finite element analysis (not necessarily equal to delta-t for the ground motion)
delta_t_analysis = 0.05
delta_t_gm = 0.01
duration_gm = 30
duration_analysis = 31
doPlotting = False


# Conduct the parametric study
counter = 0
for i in range(len(parameter2List)):

    # for j in range(len(parameter2List)):

    # # Express damping in terms of the frequency
    # zeta_g = (parameter2List[i] * 2.0 * 3.14) / 25.0
    # ktDamping.append(zeta_g)





    # Ground motion
    import SwanandGM3_SDOFTest
    SwanandGM3_SDOFTest.groundMotion(delta_t_gm,
                            duration_gm,
                            parameter1List[0],
                            parameter2List[i],
                            parameter3List[0],
                            doPlotting,
                            counter,
                            NonStationarity)

    # Increment counter
    counter += 1

    # # Remove residual velocity and displacement
    # import RemoveResiduals
    # RemoveResiduals.removeResiduals(delta_t_gm, doPlotting)


    for j in range(len(parameter4List)):
        # Finite element model
        import SwanandFEM_SDOF
        response[i, j] = SwanandFEM_SDOF.finiteElementModel(delta_t_gm,
                                                        delta_t_analysis,
                                                        duration_analysis,
                                                        parameter4List[j],
                                                        parameter5List[0])

    # Print status of this step
    # # print('\n'"%s = %.2f and %s = %.2f (grid point %i %i) gave response: %.5f" % (parameter1Name,
    #                                                                               parameter1List[i],
    #                                                                               parameter2Name,
    #                                                                               parameter2List[j],
    #                                                                               i+1,
    #                                                                               j+1,
    #                                                                               response[i, j]))

    # print('\n'"%s = %.2f and %s = %.2f gave response: %.5f" % ("Kanai-Tajimi damping", zeta_g, parameter2Name, parameter2List[i], response[i]))
    print('\n'"*****************************************")
    print('\n'"The current response matrix is:", '\n', response)



    # # Don't proceed with the parametric study if this is just a "watch-the-plots" session
    # if doPlotting:
    # import sys
    # sys.exit()

# Print response
print("The response matrix is:", response)



