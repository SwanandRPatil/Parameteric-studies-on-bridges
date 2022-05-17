
# -------------------------------------------------------------
# FILTERED WHITE NOISE (uni-directional at one location)
# -------------------------------------------------------------


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


# Nonstationarity function
def nonstationarity(t, duration, startValue, endValue):
    if t < 0 or t > duration:
        return 0.0
    else:
        return startValue + t * (endValue-startValue) / duration


# Trapezoidal integration
def trapezoidalRecordIntegration(delta_t, record):
    integrated = [0]
    for i in range(1, len(record)):
        integrated.append(integrated[i-1] + delta_t * 0.5 * (record[i-1]+record[i]))
    return integrated


# Define the shape of the impulse response function (constants removed)
def filter(omega_n, damping, t):
    if t<= 0.0:
        return 0.0
    else:
        mySqrt = np.sqrt(1.0 - damping**2)
        return -np.exp(-omega_n*damping*t) * (2 * damping * mySqrt * np.cos(omega_n * mySqrt * t) + (1 - 2 * damping**2) * np.sin(omega_n * mySqrt * t))


# Declare the function that produces the ground motion
def groundMotion(delta_t, duration, GMparameter1, GMparameter2, GMparameter3, doPlotting, counter, NonStationarity):


    # Input nonstationary frequency range
    if NonStationarity == True:
        startOmega = 2 * np.pi * (GMparameter2 + 1.0)
        endOmega = 2 * np.pi * (GMparameter2 - 1.0)
        targetVariance = GMparameter3

    else:
        startOmega = 2 * np.pi * GMparameter2
        endOmega = 2 * np.pi * GMparameter2
        targetVariance = GMparameter3

    # Normalise the targetVariance based on the frequency
    if GMparameter2 == 1.0:
        targetVariance = GMparameter3 * 4.0
    elif GMparameter2 == 2.0:
        targetVariance = GMparameter3 * 0.453489688 * 4.0
    elif GMparameter2 == 3.0:
        targetVariance = GMparameter3 * 0.272348375 * 4.0
    elif GMparameter2 == 4.0:
        targetVariance = GMparameter3 * 0.182576966 * 4.0
    else:
        targetVariance = GMparameter3

    # Other parameters of the model
    damping = GMparameter1
    pulseRate = 50


    # Modulating function
    rampTime = 10
    t1 = 0
    t2 = rampTime
    t3 = duration - rampTime
    t4 = duration


    # Issue a message, because this will take some time
    print('\n'"Starting to generate the white noise ground motion...")


    # Variance of unfactored time history
    pulseSpacing = 1.0 / pulseRate
    totalNumPulses = duration * pulseRate
    summedVariance = 0
    for i in range(totalNumPulses):
        kickTime = i * pulseSpacing
        summedVariance += (filter(startOmega, damping, 0.5*duration-kickTime))**2


    # Scaling factor to reach target variance
    varianceScaling = targetVariance / summedVariance
    print("Variance Scaling:", varianceScaling)


    # Generate the time history
    sampleRate = int(1.0 / delta_t)
    nintervals = duration * sampleRate
    ax = np.zeros(nintervals)
    t = np.zeros(nintervals)
    for i in range(totalNumPulses):
        pulse = np.random.normal(0.0, np.sqrt(varianceScaling))
        kickTime = i * pulseSpacing
        for j in range(nintervals):
            t[j] = j * delta_t
            ax[j] += pulse * filter(nonstationarity(t[j], duration, startOmega, endOmega), damping, t[j]-kickTime)


    # Plot the nonstationary function (notice ad-hoc conversion to Hz)

    nonstatFcn = []
    # for i in range(len(t)):
    #     nonstatFcn.append(nonstationarity(t[i], duration, startOmega, endOmega)/(2*np.pi))
    # plt.ion()
    # plt.figure(1)
    # plt.plot(t, nonstatFcn, 'k-')
    # plt.xlabel("Time")
    # plt.title("Variation in Kanai-Tajimi frequency")
    # plt.savefig('GM3NanstationarityFunction')



    # Instantiate and plot the modulating function
    modFcn = []
    for i in range(len(t)):
        modFcn.append(modulator(t[i],t1,t2,t3,t4))
    # if doPlotting:
    #     plt.ion()
    #     plt.figure(2)
    #     plt.plot(t, modFcn, 'k-')
    #     plt.xlabel("Time")
    #     plt.title("Modulating function")
    #     plt.show()



    # Modulate the ground motion
    ax = ax * modFcn


    # Go from cm/sec^2 to m/sec^2
    ax = ax * 0.01


    # Create zero-value ground motions in the other directions
    ay = np.zeros(len(ax))
    az = np.zeros(len(ax))


    # Integrate acceleration to obtain velocity
    vx = trapezoidalRecordIntegration(delta_t, ax)
    vy = trapezoidalRecordIntegration(delta_t, ay)
    vz = trapezoidalRecordIntegration(delta_t, az)


    # Integrate velocity to obtain displacement
    ux = trapezoidalRecordIntegration(delta_t, vx)
    uy = trapezoidalRecordIntegration(delta_t, vy)
    uz = trapezoidalRecordIntegration(delta_t, vz)


    # Print the residual displacement
    print('\n'"Residual ground displacement: %.2f" % ux[len(ux)-1])


    # # Plot
    # if doPlotting:
    #
    #     plt.ion()
    #     fig1 = plt.figure(3)
    #     plt.axis('off')
    #     plt.title('Ground Motion')
    #
    #     axes = fig1.add_subplot(311)
    #     axes.get_xaxis().set_visible(False)
    #     plt.plot(t, ax, 'k-', linewidth=1.0)
    #     plt.ylabel('$\ddot{u}_g [m/s^2]$')
    #
    #     axes = fig1.add_subplot(312)
    #     axes.get_xaxis().set_visible(False)
    #     plt.plot(t, vx, 'k-', linewidth=1.0)
    #     plt.ylabel('$\dot{u}_g [m/s]$')
    #
    #     axes = fig1.add_subplot(313)
    #     plt.plot(t, ux, 'k-', linewidth=1.0)
    #     plt.ylabel('${u}_g [m]$')
    #     plt.xlabel('Time [sec]')
    #     plt.savefig('GM3TimeHistories')



    # # Fourier transform
    #
    # spectrum = np.fft.fft(ax)
    # freq = np.fft.fftfreq(t.shape[-1])
    # spectrum = abs(spectrum[:len(spectrum)//2])
    # freq = freq[:len(freq)//2]/delta_t
    #
    # plt.ion()
    # plt.figure(4)
    # plt.grid(True)
    # plt.plot(freq, spectrum.real, 'k-')
    # plt.xlabel("Frequency")
    # plt.title("Fourier Transform")
    # plt.savefig('GM3FourierTransform')



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
