
# -------------------------------------------------------------
# VERTICAL CANTILEVER
# -------------------------------------------------------------


# Import external libraries
import numpy as np
import matplotlib.pyplot as plt
from sys import platform
if platform == "darwin":
    from openseespymac.opensees import *
elif platform == "win32":
    from openseespy.opensees import *
else:
    print("Cannot handle this type of operating system")
    import sys
    sys.exit()


# Declare the function
def finiteElementModel(delta_t_gm, delta_t_analysis, duration_analysis, parameter, doPlotting):


    # Set the parameter that is given by the parametric study
    colDiameter = parameter

    # Clean up, set 2D structure, set 3 DOFs per node
    wipe()
    model('basic', '-ndm', 2, '-ndf', 3)


    # Column height and number of elements
    height = 10.0
    numEl = 20


    # Cross-section dimensions
    # colDiameter = [PARAMETRIC STUDY]
    cover = 0.04


    # Specify the reinforcement with area of no. 8 bars in m^2
    numBars = 8
    As = 0.000442395
    Gj = (np.pi * 0.6**4) / 32


    # Specify the nodes
    node(1, 0.0, 0.0)
    for i in range(numEl):
        node(i+2, 0.0, (i+1)*height/numEl)


    # Boundary conditions
    fix(1, 1, 1, 1)


    # Specify core concrete material as core concrete ((confined), tag, f'c, ec0, f'cu, ecu), unites N/m^2
    uniaxialMaterial('Concrete01', 1, -35.0e6, -0.004, -30.0e6, -0.014)


    # Specify the cover concrete material as cover concrete ((unconfined), tag, f'c, ec0, f'cu, ecu), unites N/m^2
    uniaxialMaterial('Concrete01', 2, -30.0e6, -0.002, 0.0, -0.006)


    # Specify the steel reinforcement material as reinforcing steel (tag, fy, E0, b)
    uniaxialMaterial('Steel01', 3, 500.0e6, 200000.0e6, 0.01)


    # Create reference linear material: Elastic $matTag $E <$eta> <$Eneg>
    uniaxialMaterial('Elastic', 4, 20000.0e6)


    # Specify the fibre-section with the following notes:
    #    The center of the reinforcing bars are placed at the inner radius
    #    The core concrete ends at the inner radius (same as reinforcing bars)
    #    The reinforcing bars are all the same size
    #    The center of the section is at (0,0) in the local axis system
    #    Zero degrees is along section y-axis

    # Inner raduis in case of hollow sections
    InnerRad = 0.0
    # The distance from the section z-axis to the edge of the cover concrete -- outer edge of cover concrete
    OuterRad = colDiameter / 2.0
    # Number of radial divisions in the core i.e. "rings"
    nfCoreR = 8
    # Number of angular divisions in the core i.e. "wedges"
    nfCoreT = 8
    # Number of radial divisions in the cover region
    nfCoverR = 4
    # Number of angular divisions in the cover region
    nfCoverT = 8
    # Core radius
    coreRad = OuterRad - cover


    # section('RCCircularSection', secTag, coreTag, coverTag, steelTag, colDiameter, cover, As, nfCoreR, nfCoverR, nfCoverT, numBars, '-GJ', Gj)
    section('RCCircularSection', 1, 1, 2, 3, colDiameter, cover, As, nfCoreR, nfCoverR, nfCoverT, numBars, '-GJ', Gj)


    # Core and cover fibres in the format patch('circ', matTag, numSubdivCirc, numSubdivRad, *center, *rad, *ang)
    patch('circ', 1, nfCoreT, nfCoreR, 0, 0, InnerRad, coreRad, 0, 360)
    patch('circ', 2, nfCoverT, nfCoverR, 0, 0, coreRad, OuterRad, 0, 360)


    # Lay out rebards in the format layer('circ', matTag,numFiber,areaFiber,*center,radius,*ang=[0.0,360.0-360/numFiber])
    theta = 360 / numBars
    layer('circ', 3, numBars, As, 0, 0, coreRad, theta, 360)


    # Use Lobatto integration
    numIntPoints = 5
    beamIntegration('Lobatto', 1, 1, numIntPoints)


    # Geometric transformation ("Linear" / "PDelta")
    geomTransf('Linear', 1)


    # Specify the element as, (Columns,tag, ndI, ndJ, transfTag, integrationTag)
    for i in range(numEl):
        element('forceBeamColumn', (i+1), (i+1), (i+2), 1, 1)


    # Create a plain load pattern with a linear time series
    timeSeries('Linear', 1)
    pattern('Plain', 1, 1)


    # Nodal mass
    rcDensity = 2500
    crossSecArea = np.pi * (0.5*colDiameter)**2.0
    elementLength = height / numEl
    m = rcDensity * crossSecArea * elementLength
    for i in range(numEl):
        mass((i+2), m, m, 0.0)


    # Set time series to be passed to uniform excitation
    timeSeries('Path', 2, '-filePath', 'gm_perp.txt', '-dt', delta_t_gm, '-factor', 9.81)


    # Set load pattern (UniformExcitation, load pattern, tag, dir)
    pattern('UniformExcitation', 2, 1, '-accel', 2)


    # Rayleigh damping
    Lambda = eigen('-fullGenLapack', 1)  # eigenvalue mode 1
    Omega = Lambda[0]**0.5
    Tn = 2 * np.pi / Omega
    omega1 = 0.8 * Omega
    omega2 = 1.2 * Omega
    damping = 0.05
    b = 2 * damping / (omega1 + omega2)
    a = omega1 * omega2 * b
    rayleigh(a, 0.0, b, 0.0)
    print('\n'"Rayleigh damping periods: %.2f and %.2f" % (2 * np.pi / omega2, 2 * np.pi / omega1))


    # Plot the variation in damping
    if doPlotting:
        periods = np.linspace(0.2*Tn, 2*Tn, 50)
        omegas = 2 * np.pi / periods
        damping = a / (2*omegas) + b * omegas / 2.0
        plt.ion()
        plt.figure(10)
        plt.grid("True")
        plt.plot(periods, damping, 'k-')
        plt.xlabel("Period")
        plt.title("Damping")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Create the analysis tools
    wipeAnalysis()
    system('BandGeneral')
    constraints('Plain')
    test('NormDispIncr', 1.0e-12, 10)
    algorithm('Newton')
    numberer('RCM')
    integrator('Newmark', 0.5, 0.25)
    analysis('Transient')


    # Run an eigenvalue analysis
    Lambda = eigen('-fullGenLapack', 1)  # eigenvalue mode 1
    Omega = Lambda[0]**0.5
    Tn = 2 * np.pi / Omega
    print('\n'"Natural period BEFORE shaking: %.2f" % Tn)


    # Run the dynamic analysis in a loop
    tCurrent = getTime()
    ok = 0
    time = [tCurrent]


    # Record force at the base and displacement at the top, using RECORDERS
    dispRecorderFile = "cantileverDispTop.out"
    recorder('Node', '-file', dispRecorderFile, '-closeOnWrite', '-node', numEl+1, '-dof', 1, 'disp')
    forceRecorderFile = "cantileverForceBase.out"
    recorder('Node', '-file', forceRecorderFile, '-closeOnWrite', '-node', 1, '-dof', 1, 'reaction')


    # Record moment and curvature at the base, using COMMANDS
    curvature = [0.0]
    bendingMoment = [0.0]


    while ok == 0 and tCurrent < duration_analysis:

        # Check analysis for one step
        ok = analyze(1, delta_t_analysis)

        # If the analysis fails try initial tangent iteration
        if ok != 0:

            print("Regular Newton failed. In Modified Newton, try an initial stiffness at this step.")
            test('NormDispIncr', 1.0e-12, 100, 0)

            # In modified Newton, set stiffness equal to the tangent at the initial guess
            algorithm('ModifiedNewton', '-initial')

            # Check the analysis again
            ok = analyze(1, delta_t_analysis)

            if ok == 0:
                print("The step with initial stiffness in the modified Newton worked.")

            test('NormDispIncr', 1.0e-12, 10)
            algorithm('Newton')

        tCurrent = getTime()


        # Record moment and curvature at the base, using COMMANDS
        time.append(tCurrent)
        bendingMoment.append(sectionForce(1, 1, 2))
        curvature.append(sectionDeformation(1, 1, 2))


    # Re-run the eigenvalue analysis to get dynamic properties after time-history analysis
    Lambda = eigen('-fullGenLapack', 1)  # eigenvalue mode 1
    Omega = Lambda[0]**0.5
    Tn = 2 * np.pi / Omega
    print('\n'"Natural period AFTER shaking: %.2f" % Tn)


    # Print if the analysis is successful with Newton algorithm or not
    if ok == 0:
        print('\n'"OpenSees dynamic analysis PASSED")
    else:
        print('\n'"OpenSees dynamic analysis FAILED")


    # Read the displacement recorder file, and establish the time axis
    disp = []
    count = 0
    f = open(dispRecorderFile, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        disp.append(float(splitline[0]))
        count += 1


    # Read the force recorder file
    force = []
    count = 0
    f = open(forceRecorderFile, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        force.append(float(splitline[0]))
        count += 1


    # Print the residual displacement
    print('\n'"Residual structure displacement: %.2f" % disp[len(disp)-1])


    # Plot the responses
    if doPlotting:

        # Displacement
        plt.ion()
        plt.figure(11)
        plt.plot(time[:-1], disp, 'k-')
        plt.xlabel("Time")
        plt.ylabel("Displacement")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()

        # Reaction force
        plt.ion()
        plt.figure(12)
        plt.plot(time[:-1], force, 'k-')
        plt.xlabel("Time")
        plt.ylabel("Reaction Force")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()

        # Moment-curvature
        plt.ion()
        plt.figure(13)
        plt.plot(curvature, bendingMoment, 'k-')
        plt.xlabel("Curvature")
        plt.ylabel("Moment")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Return the response used in the parametric study
    return max(np.abs(disp))
