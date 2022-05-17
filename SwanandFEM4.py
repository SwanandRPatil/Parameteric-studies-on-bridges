

# -------------------------------------------------------------
# JAMIE PADGETT BRIDGE
# -------------------------------------------------------------


# Import external libraries
import os
from sys import platform
import numpy as np
import matplotlib.pyplot as plt


# Declare the function
def finiteElementModel(delta_t_gm, delta_t_analysis, duration, parameterFEM1, parameterFEM2, parameterFEM3, doPlotting):


    # Create a file to store the parameters that should be read at the start of the OpenSees run
    outFileID = open('parameterValues.tcl', 'w')


    # Give the delta-t of the analysis to OpenSees
    line = ("set dt %12.6f" % delta_t_analysis)
    line += '\n'
    outFileID.write(line)


    # Give the delta-t of the ground motion to OpenSees
    line = ("set delta_t_gm %12.6f" % delta_t_gm)
    line += '\n'
    outFileID.write(line)


    # Calculate the length of the ground motion record and give it to OpenSees
    record_length = int(duration/delta_t_gm)
    print("Calculated record length:", record_length)

    line = ("set record_length %i" % record_length)
    line += '\n'
    outFileID.write(line)


    # Set the diameter/deck area/bearing stiffness as a parameter and give it to OpenSees
    line = ("set parameterFEM1 %12.6f" % parameterFEM1)
    line += '\n'
    outFileID.write(line)


    line = ("set parameterFEM2 %12.6f" % parameterFEM2)
    line += '\n'
    outFileID.write(line)


    line = ("set parameterFEM3 %12.6f" % parameterFEM3)
    line += '\n'
    outFileID.write(line)
    outFileID.close()


    # Run OpenSees with tcl file in Imperial units
    if platform == "darwin":
        os.system('/Users/terjehaukaas/Dropbox/DOCUMENTS/WORK/OpenSees/OpenSees3.2.2/bin/opensees ForColumnDia_3-Span_Imperial.tcl')
    elif platform == "win32":
        os.system(r'C:\Users\swan0075\Dropbox\OpenSeesTest\OpenSees3.2.2-x64\bin\OpenSees.exe ForColumnDia_3-Span_Imperial.tcl')
    else:
        print("Cannot handle this type of operating system")


    # Plots for FEM4
    # For bent 1
    disp1 = []
    count = 0
    filePath1 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\plotTopNode1dof3.out'
    f = open(filePath1, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        disp1.append(0.0254 * float(splitline[0]))
        count += 1
    print("Displacement = ", disp1)
    # Covert back to meter from inch
    peakDisp1 = max(np.abs(disp1))
    print("The peak transverse displacement is", peakDisp1, " meter.")
    f.close()

    # For bent 2
    disp2 = []
    count = 0
    filePath2 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\plotTopNode2dof3.out'
    f = open(filePath2, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        disp2.append(0.0254 * float(splitline[0]))
        count += 1
    print("Displacement = ", disp2)
    # Covert back to meter from inch
    peakDisp2 = max(np.abs(disp2))
    print("The peak transverse displacement is", peakDisp2, " meter.")
    f.close()

    # For bent 1
    curvature = []
    count = 0
    filePath3 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\CurvatureColBottom.out'
    f = open(filePath3, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        curvature.append(float(splitline[1]))
        count += 1
    print("Curvature per inch = ", curvature)
    # Covert back to SI units
    peakCurvature = max(np.abs(curvature)) / 0.0254
    print("The peak curvature is", peakCurvature, " per meter.")
    f.close()

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
    print("Bearing deformation in inch = ", fxdBrgDisp)
    # Covert back to SI units
    peakBrgDisp = max(np.abs(fxdBrgDisp)) * 0.0254
    print("The peak fixed bearing displacement is", peakBrgDisp, " meter.")
    f.close()

    # For period after shaking
    periodBeforeShaking = []
    count = 0
    filePath12 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\fundamentalPeriod.out'
    f = open(filePath12, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        periodBeforeShaking.append(float(splitline[0]))
        count += 1
    print("Period before shaking in seconds = ", periodBeforeShaking)
    # Get the peak
    periodBeforeShakingShaking = max(np.abs(periodBeforeShaking))

    # Plots for FEM4
    # For bent 1
    driftTransverse = []
    count = 0
    filePath10 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\col_drift_t.out'
    f = open(filePath10, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        driftTransverse.append(float(splitline[0]))
        count += 1
    print("Transverse drift is ", driftTransverse)
    # Covert back to meter from inch
    # peakDisp1 = 0.0254 * max(np.abs(disp1))
    # print("The  is", peakDisp1, " meter.")
    f.close()



    # # For period after shaking
    # periodAfterShaking = []
    # count = 0
    # filePath10 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\MSC-Concrete_1.eig'
    # f = open(filePath10, "r")
    # lines = f.readlines()
    # for oneline in lines:
    #     splitline = oneline.split()
    #     periodAfterShaking.append(float(splitline[0]))
    #     count += 1
    # print("Period after shaking in seconds = ", periodAfterShaking)
    #
    # # Get the peak
    # periodAfterShaking = max(np.abs(periodAfterShaking))
    # changeInPeriod = 100 * (periodAfterShaking - periodBeforeShaking) / (periodBeforeShaking)
    # print("The elongation in period due to shaking is:", changeInPeriod, "%.")
    # f.close()

    # Save force at each time instant
    colSForce = []
    count = 0
    filePath13 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\colBottomSF.frc'
    f = open(filePath13, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        colSForce.append(float(splitline[2]))
        count += 1

    # Record cumulative hysterysis energy
    cumulativeEnergyDissipation = np.trapz(colSForce, disp1)
    print("the cumulative energy dissipated is:", cumulativeEnergyDissipation)

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
    maxPlasticRotation = max(np.abs(plasticRotation))
    print("The maximum plastic rotation at the base of column is:", maxPlasticRotation)


    # Set the response as zero when the analysis has failed to converge
    ok = 0
    filePath7 = r'C:\Users\swan0075\Dropbox\Swanand-Terje\Python Parametric Study\MSC-Concrete_1\nonconvergenceFile.out'
    f = open(filePath7, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        ok = int(splitline[0])

        count += 1
    f.close()

    # Return the response to be used in the parametric study
    if ok != 0:
        return 0
    else:
        return maxPlasticRotation
