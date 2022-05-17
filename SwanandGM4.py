
# -------------------------------------------------------------
# SPECTRAL SUM OF SINE WAVES (uni-directional at one location)
# -------------------------------------------------------------


# TO DO LIST
# -- Apply incoherent ground motions at different locations in the finite element model
# -- Clean up recorders in the finite element models, and include dowel recorder
# -- Leave the attenuation effect included in the code, but let it be zero for our analyses
# -- In the code, properly label each effect: Attenuation, incoherency, wave passage, soil response
# -- Include the "tau" for modelling of the wave passage effect
# -- Include "another epsilon" to address the soil response effect (CHECK THAT *S* EQUALS *H*)
# -- In that phase shift, model "v_app" (the frequency-dependent velocity of ground motion waves)
# -- Understand what the "coherency function" gamma is, in ADKs paper
# -- High pass filter?
# -- Spectrum matching?






# Import external libraries
import numpy as np
import matplotlib.pyplot as plt


# Create a trapezoidal modulating function
def modulator(t, t1, t2, t3, t4):
    if t<t1:
        return 0.0
    elif t<t2:
        return (t-t1)/(t2-t1)
    elif t<t3:
        return 1.0
    elif t<t4:
        return 1.0-(t-t3)/(t4-t3)
    else:
        return 0.0


# Trapezoidal integration
def trapezoidalRecordIntegration(delta_t, record):

    integrated = [0]
    for i in range(1, len(record)):
        integrated.append(integrated[i-1] + delta_t * 0.5 * (record[i-1]+record[i]))

    return integrated


# Attenuation of ground motion with distance
def attenuation(distance, attenuationParameter):

    return np.exp(-distance/attenuationParameter)



# Declare the function that produces the ground motion
def groundMotion(delta_t, duration, parameter, doPlotting, counter):


    # Distance
    distance = 40.0


    # Frequency range
    minHz = 0
    maxHz = 25


    # Incoherency parameters
    incoherencyFrequency = 6.0
    incoherencyDistance = 100.0
    alphaIncoherencyConstant = 2.5e-4  # Called gamma/beta in Luco & Wong (1986) top of Page 894


    # Attenuation
    attenuationParameter = 1000
    attenuate = attenuation(distance, attenuationParameter)


    # Parameters of the Kanai-Tajimi spectrum
    sigma = 103
    omega_g = 2 * np.pi * 3
    zeta_g = parameter


    # Divide the spectrum into "blocks"
    nblocks = 100
    delta_f = (maxHz-minHz)/nblocks


    # Modulating function
    rampTime = 2
    t1 = 0
    t2 = rampTime
    t3 = duration - rampTime
    t4 = duration


    # Create list of frequency values
    f = np.linspace(minHz+0.5*delta_f, maxHz-0.5*delta_f, nblocks)


    # Define the Kanai-Tajimi spectrum
    S0 = sigma**2 * 2 * zeta_g / (np.pi * omega_g * (4 * zeta_g**2 + 1))
    K = 2 * zeta_g * omega_g * (2 * np.pi * f)
    S = (2 * np.pi) * S0 * (omega_g**4 + K**2) / ((omega_g**2 - (2 * np.pi * f)**2)**2 + K**2)


    # Plot the spectrum
    if doPlotting:
        plt.ion()
        plt.figure(1)
        plt.grid(True)
        plt.plot(f, S, 'k-')
        plt.xlabel("Frequency [Hz]")
        plt.title("Kanai-Tajimi Spectrum")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Calculate the standard deviation in each frequency interval
    intervalStdv = np.sqrt(delta_f * S)


    # Store realizations if this is first step of parametric study, otherwise just read A from file
    ignoreRandomness = False
    rvFileName = "rv_realizations.txt"
    A = []
    B = []
    phi = []
    if counter == 1:

        # Generate uniform random numbers between 0 and 2*pi as phase angles
        phi = (2 * np.pi) * np.random.random_sample(nblocks)

        # Generate coefficients for each sine wave
        if ignoreRandomness:
            print('\n'"*************** NOTICE THAT THE GROUND MOTION AMPLITUDES ARE NOT RANDOM ***************")
            A = np.ones(nblocks)
            B = np.ones(nblocks)
        else:
            A = np.random.normal(0.0, 1.0, nblocks)
            B = np.random.normal(0.0, 1.0, nblocks)

        # Store the random variable realizations
        outFileID = open(rvFileName, 'w')
        for i in range(nblocks):
            line = ("%.10f  %.10f" % (A[i], phi[i]))
            line += '\n'
            outFileID.write(line)
        outFileID.close()

    else:

        # Read the random variable realizations
        inFileID = open(rvFileName, "r")
        lines = inFileID.readlines()
        for oneline in lines:
            splitline = oneline.split()
            A.append(float(splitline[0]))
            phi.append(float(splitline[1]))


    # Scale the sine wave amplitudes to match the variance of the spectrum blocks
    for i in range(nblocks):
        A[i] = A[i] * intervalStdv[i]
        B[i] = B[i] * intervalStdv[i]


    # Create the time series
    t = np.arange(0, duration, delta_t)
    gmReference = np.zeros(len(t))
    gmDistance = np.zeros(len(t))
    for k in range(nblocks):
        beta = (np.arctan(f[k] / incoherencyFrequency) * np.arctan(distance / incoherencyDistance)) / (np.pi * 0.50)
        p = np.cos(beta)
        q = np.sin(beta)
        omega = 2 * np.pi * f[k]
        alpha = alphaIncoherencyConstant * omega * distance
        epsilon = np.random.normal(0.0, alpha)
        gmReference += np.sqrt(2) * abs(A[k]) * np.cos(omega * t + phi[k])
        gmDistance += attenuate * np.sqrt(2) * (p * abs(A[k]) + q * abs(B[k])) * np.cos(omega * t + phi[k] + epsilon)


    # Instantiate the modulating function
    modFcn = []
    for i in range(len(t)):
        modFcn.append(modulator(t[i],t1,t2,t3,t4))


    # Plot the modulating function
    if doPlotting:
        plt.ion()
        plt.figure(2)
        plt.plot(t, modFcn, 'k-')
        plt.xlabel("Time")
        plt.title("Modulating function")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Modulate the ground motion and go from cm/sec^2 to m/sec^2
    gmReference = gmReference * modFcn * 0.01
    gmDistance = gmDistance * modFcn * 0.01


    # Create zero-value ground motions in the other directions
    ay = np.zeros(len(gmReference))
    az = np.zeros(len(gmReference))


    # Integrate acceleration to obtain velocity
    vx = trapezoidalRecordIntegration(delta_t, gmReference)
    vy = trapezoidalRecordIntegration(delta_t, ay)
    vz = trapezoidalRecordIntegration(delta_t, az)


    # Integrate velocity to obtain displacement
    ux = trapezoidalRecordIntegration(delta_t, vx)
    uy = trapezoidalRecordIntegration(delta_t, vy)
    uz = trapezoidalRecordIntegration(delta_t, vz)


    # Plot the two ground accelerations
    if doPlotting:
        plt.ion()
        plt.figure(3)
        plt.plot(t, gmReference, 'k-')
        plt.plot(t, gmDistance, 'r-')
        plt.xlabel("Time")
        plt.title("Ground acceleration")
        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Print the ground motion to file
    outFileID = open('gm_perp.txt', 'w')
    for step in range(len(t)):
        line = ("%12.6f" % gmReference[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    outFileID = open('gm_perp_dist.txt', 'w')
    for step in range(len(t)):
        line = ("%12.6f" % gmDistance[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

