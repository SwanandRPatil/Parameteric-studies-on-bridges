
# -------------------------------------------------------------
# SIMPLY SUPPORTED BEAM
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
def finiteElementModel(delta_t_gm, delta_t, duration, parameter, doPlotting):


    # Initialize the model
    wipe()
    model('basic', '-ndm', 2, '-ndf', 3)


    # Input (N, kg, m)
    length = 10.0
    M = 1000
    E = 200E9
    b = 0.2
    h = parameter
    A = b * h
    I = b * h**3 / 12.0


    # Nodes
    node(1, 0.0,        0.0)
    node(2, 0.5*length, 0.0)
    node(3, length,     0.0)


    # Mass
    mass(2, M, M, 0.0)


    # Supports
    fix(1, 1, 1, 0)
    fix(3, 0, 1, 0)


    # Specify core concrete material as core concrete ((confined), tag, f'c, ec0, f'cu, ecu), unites N/m^2
    uniaxialMaterial('Concrete01', 1, -35.0e6, -0.004, -30.0e6, -0.014)


    # Specify the cover concrete material as cover concrete ((unconfined), tag, f'c, ec0, f'cu, ecu), unites N/m^2
    uniaxialMaterial('Concrete01', 2, -30.0e6, -0.002, 0.0, -0.006)


    # Specify the steel reinforcement material as reinforcing steel (tag, fy, E0, b)
    uniaxialMaterial('Steel01', 3, 500.0e6, 200000.0e6, 0.01)


    # Create reference linear material: Elastic $matTag $E <$eta> <$Eneg>
    uniaxialMaterial('Elastic', 4, E)


    # Define section as
    # section('RCSection2d', secTag, coreMatTag, coverMatTag, steelMatTag, d, b, cover_depth, Atop, Abot, Aside, Nfcore, Nfcover, Nfs)
    coverDepth = 0.03
    numLayerBars = 4
    diaBars = 0.016
    Atop = numLayerBars * np.pi * 0.25 * diaBars**2
    Abot = numLayerBars * np.pi * 0.25 * diaBars**2
    Aside = 0.0
    Nfcore = 8
    Nfcover = 2
    Nfsteel = 4
    section('RCSection2d', 1, 1, 2, 3, h, b, coverDepth, Atop, Abot, Aside, Nfcore, Nfcover, Nfsteel)


    # Use Lobatto integration
    numIntPoints = 5
    beamIntegration('Lobatto', 1, 1, numIntPoints)

    # Geometric transformation
    geomTransf('Linear', 1)


    # Elements
    element('forceBeamColumn', 1, 1, 2, 1, 1)
    element('forceBeamColumn', 2, 2, 3, 1, 1)


    # Set time series to be passed to uniform excitation
    factor = 1.0
    timeSeries('Path', 1, '-filePath', 'gm_perp.txt', '-dt', delta_t_gm, '-factor', factor)


    # UniformExcitation load pattern ($patternTag $dir -accel $timeSeriesTag)
    pattern('UniformExcitation', 1, 2, '-accel', 1)


    # Eigenvalue analysis
    TnAnalytical = 2 * np.pi / np.sqrt(48 * E * I / length**3/M)
    Lambda = eigen('-fullGenLapack', 1)
    TnOpenSees = 2 * np.pi / Lambda[0]**0.5
    print('\n'"Period (analytical) = %.2f / Period (OpenSees) = %.2f / Frequency (Hz) = %.2f" % (TnAnalytical , TnOpenSees, 1.0/TnOpenSees))


    # Rayleigh damping
    period2 = 1.5*TnOpenSees
    period1 = 0.5*TnOpenSees
    omega1 = 2 * np.pi / period1
    omega2 = 2 * np.pi / period2
    damping = 0.05
    b = 2 * damping / (omega1 + omega2)
    a = omega1 * omega2 * b
    rayleigh(a, 0.0, b, 0.0)
    print('\n'"Rayleigh damping periods: %.2f and %.2f" % (period1, period2))


    # Plot the variation in damping
    if doPlotting:
        periods = np.linspace(0.2*TnOpenSees, 2*TnOpenSees, 50)
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


    # Analysis setup
    system('BandGeneral')
    constraints('Plain')
    test('NormDispIncr', 1.0e-12, 10)
    algorithm('Newton')
    numberer('RCM')
    integrator('Newmark', 0.5, 0.25)
    analysis('Transient')


    # Create recorder
    recorderFile = "terjesSimplySupported.out"
    recorder('Node', '-file', recorderFile, '-closeOnWrite', '-node', 2, '-dof', 2, 'disp')


    # Run the analysis
    tCurrent = getTime()
    ok = 0
    time = [tCurrent]
    u = [0.0]
    while ok == 0 and tCurrent < duration:

        ok = analyze(1, delta_t)

        # if the analysis fails try initial tangent iteration
        if ok != 0:
            print("regular newton failed .. lets try an initial stiffness for this step")
            test('NormDispIncr', 1.0e-12, 100, 0)
            algorithm('ModifiedNewton', '-initial')
            ok = analyze(1, delta_t)
            if ok == 0:
                print("that worked .. back to regular newton")
            test('NormDispIncr', 1.0e-12, 10)
            algorithm('Newton')

        tCurrent = getTime()

        time.append(tCurrent)
        u.append(nodeDisp(2, 2))


    # Read the recorder file
    disp = []
    time = []
    count = 0
    f = open(recorderFile, "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        value = float(splitline[0])
        disp.append(value)
        time.append(count * delta_t)
        count += 1


    # Print the residual displacement
    print('\n'"Residual structure displacement: %.2f" % disp[len(disp)-1])


    # Plot the response
    if doPlotting:
        plt.ion()
        plt.figure(11)
        plt.plot(time, disp, 'k-')
        plt.xlabel("Time")
        plt.title("Response")
        plt.show()

        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Return the response used in the parametric study
    return max(np.abs(disp))
