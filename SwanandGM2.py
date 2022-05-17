
# -------------------------------------------------------------
# SPECTRAL SUM OF SINE WAVES (uni-directional at one location)
# -------------------------------------------------------------


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



# Declare the function that produces the ground motion
def groundMotion(delta_t, duration, parameterGM1, parameterGM2, parameterGM3, doPlotting, counter):

    # Print parameters
    print("The parameters for the ground motion model in this run are", "\nDamping=", parameterGM1, "\nFrequency=", parameterGM2, "\nSigma=", parameterGM3)


    # Frequency range
    minHz = 0
    maxHz = 20


    # Parameters of the Kanai-Tajimi spectrum
    sigma = parameterGM1
    omega_g = 2 * np.pi * parameterGM2
    zeta_g = parameterGM3


    # Divide the spectrum into "blocks"
    nblocks = 500
    delta_f = (maxHz-minHz)/nblocks


    # Modulating function
    rampTime = 5
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
    ignoreRandomness = True
    rvFileName = "rv_realizations.txt"
    A = []
    phi = []
    if counter == 1:

        # Generate uniform random numbers between 0 and 2*pi as phase angles
        phi = (2 * np.pi) * np.random.random_sample(nblocks)

        # Generate coefficients for each sine wave
        if ignoreRandomness:
            print('\n'"*************** NOTICE THAT THE GROUND MOTION AMPLITUDES ARE NOT RANDOM ***************")
            A = np.ones(nblocks)
        else:
            A = np.random.normal(0.0, 1.0, nblocks)

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


    # Create the time series
    t = np.arange(0, duration, delta_t)
    ax = np.zeros(len(t))
    for k in range(nblocks):
        ax += np.sqrt(2) * abs(A[k]) * np.cos(2 * np.pi * f[k] * t + phi[k])

    # # Plot stationary time history
    # aStationary = ax * 0.01
    # if doPlotting:
    #     plt.ion()
    #     fig0 = plt.figure(30)
    #
    #     plt.title('Ground Motion')
    #     plt.plot(t, aStationary, 'k-', linewidth=1.0)
    #     plt.ylabel('$\ddot{u}_g [m/s^2]$')
    #     plt.show()
    #     print('\n'"Press any key to continue...")
    #     plt.waitforbuttonpress()


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


    # Modulate the ground motion
    ax = ax * modFcn


    # Go from cm/sec^2 to m/sec^2
    ax = ax * 0.01


    # Create zero-value ground motions in the other directions
    ay = np.zeros(len(ax))
    az = np.zeros(len(ax))

    print("The ground motion is: \n", ax)

    # Integrate acceleration to obtain velocity
    vx = trapezoidalRecordIntegration(delta_t, ax)
    vy = trapezoidalRecordIntegration(delta_t, ay)
    vz = trapezoidalRecordIntegration(delta_t, az)


    # Integrate velocity to obtain displacement
    ux = trapezoidalRecordIntegration(delta_t, vx)
    uy = trapezoidalRecordIntegration(delta_t, vy)
    uz = trapezoidalRecordIntegration(delta_t, vz)


    # Plot the ground motion
    if doPlotting:
        plt.ion()
        fig1 = plt.figure(3)
        plt.axis('off')
        plt.title('Ground Motion')

        axes = fig1.add_subplot(311)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, ax, 'k-', linewidth=1.0)
        plt.ylabel('$\ddot{u}_g [m/s^2]$')

        axes = fig1.add_subplot(312)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, vx, 'k-', linewidth=1.0)
        plt.ylabel('$\dot{u}_g [m/s]$')

        axes = fig1.add_subplot(313)
        plt.plot(t, ux, 'k-', linewidth=1.0)
        plt.ylabel('${u}_g [m]$')
        plt.xlabel('Time [sec]')
        plt.savefig("SpectrumRepresentationTimeHistory")



    # Fourier transform
    if doPlotting:
        spectrum = np.fft.fft(ax)
        freq = np.fft.fftfreq(t.shape[-1])
        spectrum = abs(spectrum[:len(spectrum)//2])
        freq = freq[:len(freq)//2]/delta_t
        plt.ion()
        plt.figure(4)
        plt.plot(freq, spectrum.real, 'k-')
        plt.xlabel("Frequency")
        plt.title("Fourier Transform")
        plt.savefig('GM2FourierTransform')



    # Print the ground motion to file
    outFileID = open('gm_perp.txt', 'w')
    for step in range(len(t)):
        line = ("%12.6f" % ax[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    outFileID = open('gm_long.txt', 'w')
    for step in range(len(t)):
        line = ("%12.6f" % ay[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    outFileID = open('gm_vert.txt', 'w')
    for step in range(len(t)):
        line = ("%12.6f" % az[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()
