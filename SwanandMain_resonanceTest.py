
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
parameter2Name = "Mean Frequency"
parameter2List = np.array([2.004])
parameter3Name = "Target Variance"
parameter3List = np.array([11000.0])
NonStationarity = False

# Finite element model parameters
parameter4Name = "Column Diameter"
parameter4List = np.array([15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0])
parameter5Name = "Bearing Stiffness"
parameter5List = np.array([250.0])
parameter6Name = "Deck Area"
parameter6List = np.array([1500.0])

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


    # Increment counter
    counter += 1


    # Ground motion
    import SwanandGM3
    SwanandGM3.groundMotion(delta_t_gm,
                            duration_gm,
                            parameter1List[0],
                            parameter2List[i],
                            parameter3List[0],
                            doPlotting,
                            counter, NonStationarity)


    # # Remove residual velocity and displacement
    # import RemoveResiduals
    # RemoveResiduals.removeResiduals(delta_t_gm, doPlotting)


    for j in range(len(parameter4List)):
        # Finite element model
        import SwanandFEM4
        response[i, j] = SwanandFEM4.finiteElementModel(delta_t_gm,
                                                        delta_t_analysis,
                                                        duration_analysis,
                                                        parameter4List[j],
                                                        parameter5List[0],
                                                        parameter6List[0],
                                                        doPlotting)

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


# # Plot the response, varying a single variable
# plt.ion()
# plt.figure(100)
# plt.grid(True)
# plt.autoscale(True)
# colorList = ['k-', 'r-', 'g-', 'b-', 'y-', 'm-', 'c-']
# for i in range(len(parameter2List)):
#     plt.plot(parameter1List, response[:, i], colorList[i], linewidth=1.0, label=("%s = %.2f" % (parameter2Name, parameter2List[i])))
# plt.legend()
# plt.xlabel(parameter1Name)
# plt.ylabel(responseName)
# plt.title("%s vs. %s" % (parameter1Name, parameter2Name))
# plt.show()
# plt.savefig('2DParametricPlot')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()

# # Plot the response, varying a single variable
# plt.ion()
# plt.figure(100)
# plt.grid(True)
# plt.autoscale(True)
# colorList = ['k-', 'r-', 'g-', 'b-', 'y-', 'm-', 'c-']
# for i in range(len(parameter2List)):
#     plt.plot(parameter2List, response, colorList[i], linewidth=1.0, label=("%s = %.2f" % (parameter2Name, parameter2List[i])))
# # plt.legend()
# plt.xlabel(parameter2Name)
# plt.ylabel(responseName)
# # plt.title("%s vs. %s" % ("Damping", parameter2Name))
#
# plt.show()
# plt.savefig('2DParametricPlot')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()


# Plot moment curvature response of column section
colCurvature = []
count = 0
filePath1 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\curvatureColBottom.out'
f = open(filePath1, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    colCurvature.append(float(splitline[1]))
    count += 1

# Save moment at each time instant
colMoment = []
count = 0
filePath2 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\colBottomSF.frc'
f = open(filePath2, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    colMoment.append(float(splitline[1]))
    count += 1

# Save force at each time instant
colSForce = []
count = 0
filePath3 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\colBottomSF.frc'
f = open(filePath3, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    colSForce.append(float(splitline[2]))
    count += 1

# For bent 1 top disp
disp1 = []
count = 0
filePath4 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\plotTopNode1dof3.out'
f = open(filePath4, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    disp1.append(float(splitline[0]))
    count += 1

# For bearing force in 504
fxdBrgForce = []
count = 0
filePath5 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\fxdbrgForce.out'
f = open(filePath5, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    fxdBrgForce.append(float(splitline[2]))
    count += 1

# For bearing displacement in 504
fxdBrgDisp = []
count = 0
filePath6 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\fxdBrgDisp.out'
f = open(filePath6, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    fxdBrgDisp.append(float(splitline[2]))
    count += 1

# For plastic rotation in 1057
plasticRotation = []
count = 0
filePath7 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\plasticRotColBottom.out'
f = open(filePath7, "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    plasticRotation.append(float(splitline[1]))
    count += 1

# Convert to SI units
colMomentSI = [i * 0.11298 for i in colMoment]
colCurvatureSI = [i * 39.37 for i in colCurvature]
colSForceSI = [i * -4.4482 for i in colSForce]
colDispSI = [i * 0.0254 for i in disp1]
fxdBrgForceSI = [i * -4.4482 for i in fxdBrgForce]
fxdBrgDispSI = [i * 0.0254 for i in fxdBrgDisp]

# # Plot the moment-curvature response
# plt.ion()
# plt.figure(51)
# plt.grid(True)
# plt.autoscale(True)
# plt.plot(colCurvatureSI, colMomentSI, 'k-')
# plt.xlabel("Curvature [per m]")
# plt.ylabel("Moment [kNm]")
# plt.show()
# plt.savefig('MomentCurvature')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
# # Plot the force-deformation response
# plt.ion()
# plt.figure(61)
# plt.grid(True)
# plt.autoscale(True)
# plt.plot(colDispSI, colSForceSI, 'k-')
# plt.xlabel("Displacement [m]")
# plt.ylabel("Force [kN]")
# plt.show()
# plt.savefig('ForceDeformation')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
# # Plot the bearing force-deformation response
# plt.ion()
# plt.figure(71)
# plt.grid(True)
# plt.autoscale(True)
# plt.plot(fxdBrgDispSI, fxdBrgForceSI, 'k-')
# plt.xlabel("Displacement [m]")
# plt.ylabel("Force [kN]")
# plt.show()
# plt.savefig('BrgForceDeformation')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
# # Plot the moment-plastic rotation response
# plt.ion()
# plt.figure(81)
# plt.grid(True)
# plt.autoscale(True)
# plt.plot(plasticRotation, colMomentSI, 'k-')
# plt.xlabel("Plastic Rotation [rad]")
# plt.ylabel("Moment [kNm]")
# plt.show()
# plt.savefig('MomentPlasticRot')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
#
# # # Plot the response, varying two variables
# # plt.ion()
# # fig = plt.figure(101)
# # ax = fig.gca(projection='3d')
# # X, Y = np.meshgrid(parameter1List, parameter2List)
# # surf = ax.plot_surface(X, Y, np.transpose(response), linewidth=0, antialiased=False)
# # plt.xlabel(parameter1Name)
# # plt.ylabel(parameter2Name)
# # plt.show()
# # # print('\n'"Pausing until red button is pressed in PyCharm...")
# # # plt.pause(1e5)
# # plt.savefig('3DParametricPlot')
# # print('\n'"Press any key to continue...")
# # plt.waitforbuttonpress()

