

# -------------------------------------------------------------
# JAMIE PADGETT BRIDGE
# -------------------------------------------------------------


# Import external libraries
import os
from sys import platform
import matplotlib.pyplot as plt
import numpy as np
import openseespy.opensees as ops


# Declare the function
def finiteElementModel(delta_t_gm, delta_t_analysis, duration, parameterFEM1, parameterFEM2):


    ops.wipe()
    ops.model('basic','-ndm',1,'-ndf',1)

    f_fun = ((parameterFEM1 / parameterFEM2)**0.5) / (2 * np.pi)

    print("The fundamental frequency of the structure is:", f_fun)

    ops.node(1,0); ops.fix(1,1)
    ops.node(2,0); ops.mass(2, parameterFEM2)

    # ops.uniaxialMaterial('Elastic', 1, parameterFEM1)
    # Specify the elastic-perfectly plastic material ('mat', tag, E, yieldStrainTensile)
    # ops.uniaxialMaterial('ElasticPP', 1, parameterFEM1, 0.05)

    # Specify the steel reinforcement material as reinforcing steel (tag, fy, E0, b)
    ops.uniaxialMaterial('Steel01', 1, 5000.0, parameterFEM1, 0.01)

    ops.element('zeroLength', 1, 1, 2, '-mat', 1, '-dir', 1)

    # Set time series to be passed to uniform excitation
    ops.timeSeries('Path', 1, '-filePath', 'gm_perp.txt', '-dt', delta_t_gm, '-factor', 9.81)

    ops.pattern('UniformExcitation', 1, 1, '-accel', 1)

    Nsteps = int(duration/delta_t_analysis)


    ops.recorder('Node','-file','SDFresponse.out', '-closeOnWire', '-node', 2, '-dof', 1, 'disp')

    #recorder Element -file  MSC-Concrete_1/fxdBrgForce.out -closeOnWrite -ele  504  force
    # recorder('Node', '-file', forceRecorderFile, '-closeOnWrite', '-node', 1, '-dof', 1, 'reaction')
    # ops.recorder('Element', '-file', 'SDFForce.out', '-closeOnWire', '-ele', 1, 'force')
    ops.recorder('Node', '-file', 'SDFForce.out', '-closeOnWrite', '-node', 1, '-dof', 1, 'reaction')

    # Create the analysis tools
    ops.wipeAnalysis()
    ops.system('BandGeneral')
    ops.constraints('Plain')
    ops.test('NormDispIncr', 1.0e-12, 10)
    ops.algorithm('Newton')
    ops.numberer('RCM')
    ops.integrator('Newmark', 0.5, 0.25)
    ops.analysis('Transient')


    # Run an eigenvalue analysis
    # Rayleigh damping
    Lambda = ops.eigen('-fullGenLapack', 1)  # eigenvalue mode 1
    Omega = Lambda[0]**0.5
    Tn = 2 * np.pi / Omega
    omega1 = 0.8 * Omega
    omega2 = 1.2 * Omega
    damping = 0.05
    b = 2 * damping / (omega1 + omega2)
    a = omega1 * omega2 * b
    ops.rayleigh(a, 0.0, b, 0.0)
    print('\n'"Natural period BEFORE shaking: %.2f" % Tn)


    # Run the dynamic analysis in a loop
    elementForce = []
    nodeDisplacement = []
    tCurrent = ops.getTime()
    ok = 0
    time = [tCurrent]


    while ok == 0 and tCurrent < duration:

        # Check analysis for one step
        ok = ops.analyze(1, delta_t_analysis)

        # If the analysis fails try initial tangent iteration
        if ok != 0:

            print("Regular Newton failed. In Modified Newton, try an initial stiffness at this step.")
            ops.test('NormDispIncr', 1.0e-12, 100, 0)

            # In modified Newton, set stiffness equal to the tangent at the initial guess
            ops.algorithm('ModifiedNewton', '-initial')

            # Check the analysis again
            ok = ops.analyze(1, delta_t_analysis)

            if ok == 0:
                print("The step with initial stiffness in the modified Newton worked.")

            ops.test('NormDispIncr', 1.0e-12, 10)
            ops.algorithm('Newton')

        tCurrent = ops.getTime()


        # Record moment and curvature at the base, using COMMANDS
        time.append(tCurrent)
        elementForce.append(ops.eleForce(1,1))
        nodeDisplacement.append(ops.nodeDisp(2, 1))


    # # Re-run the eigenvalue analysis to get dynamic properties after time-history analysis
    LambdaAfter = ops.eigen('-fullGenLapack', 1)  # eigenvalue mode 1
    OmegaAfter = LambdaAfter[0]**0.5
    TnAfter = 2 * np.pi / OmegaAfter
    print('\n'"Natural period AFTER shaking: %.2f" % TnAfter)


    # Print if the analysis is successful with Newton algorithm or not
    if ok == 0:
        print('\n'"OpenSees dynamic analysis PASSED")
    else:
        print('\n'"OpenSees dynamic analysis FAILED")

    # For top disp
    disp1 = []
    count = 0
    filePath1 = r'SDFresponse.out'
    f = open(filePath1, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        disp1.append(float(splitline[0]))
        count += 1
    print("Displacement = ", disp1)
    # Covert back to meter from inch
    peakDisp1 = max(np.abs(disp1))
    print("The peak transverse displacement is", peakDisp1, " meter.")

    # For element force
    force = []
    count = 0
    filePath2 = r'SDFForce.out'
    f = open(filePath2, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        force.append(float(splitline[0]))
        count += 1
    print("Force = ", force)
    # Covert back to meter from inch
    peakForce = max(np.abs(force))
    print("The peak force", peakForce, " Newtons")

    print("Element Force = ", elementForce)
    print('Length of elementForce =', len(elementForce))
    print("Nodal displacement = ", nodeDisplacement)
    print('Length of nodeDisplacement =', len(nodeDisplacement))

    # Plot the force-deformation response
    plt.ion()
    plt.figure(501)
    plt.grid(True)
    plt.autoscale(True)
    plt.plot(nodeDisplacement, elementForce, 'k-')
    plt.xlabel("Displacement [m]")
    plt.ylabel("Force [N]")
    plt.savefig('SDOF_ForceDeformation')



    return peakDisp1

