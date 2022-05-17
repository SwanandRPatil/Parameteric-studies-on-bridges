
# -------------------------------------------------------------
# RECORDED GROUND MOTION
# -------------------------------------------------------------


# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Trapezoidal integration
def trapezoidalRecordIntegration(delta_t, record):

    integrated = [0]
    for i in range(1, len(record)):
        integrated.append(integrated[i-1] + delta_t * 0.5 * (record[i-1]+record[i]))

    return integrated


# Declare the function that produces the ground motion
def groundMotion(delta_t, duration, parameter, doPlotting, counter):


    # Load x-direction acceleration
    ax = []
    f = open("RSN8064_CCHURCH_CCCCN26W.AT2", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = 9.81 * float(splitline[j])
            ax.append(value)


    # Load y-direction acceleration
    ay = []
    f = open("GroundAccelerationY.txt", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = 9.81 * float(splitline[j])
            ay.append(value)


    # Load z-direction acceleration
    az = []
    f = open("GroundAccelerationZ.txt", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = 9.81 * float(splitline[j])
            az.append(value)


    # Create the time axis
    numTimePoints = len(ax)
    t = np.linspace(0, delta_t * numTimePoints, numTimePoints)


    # Integrate acceleration to obtain velocity
    vx = trapezoidalRecordIntegration(delta_t, ax)
    vy = trapezoidalRecordIntegration(delta_t, ay)
    vz = trapezoidalRecordIntegration(delta_t, az)


    # Integrate velocity to obtain displacement
    ux = trapezoidalRecordIntegration(delta_t, vx)
    uy = trapezoidalRecordIntegration(delta_t, vy)
    uz = trapezoidalRecordIntegration(delta_t, vz)


    # Plot
    if doPlotting:
        plt.ion()
        fig1 = plt.figure(1)
        plt.axis('off')
        plt.title('Ground Motion')

        axes = fig1.add_subplot(331)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, ax, 'k-', linewidth=1.0)
        plt.ylabel('$\ddot{u}_g [m/s^2]$')

        axes = fig1.add_subplot(332)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, ay, 'k-', linewidth=1.0)

        axes = fig1.add_subplot(333)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, az, 'k-', linewidth=1.0)

        axes = fig1.add_subplot(334)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, vx, 'k-', linewidth=1.0)
        plt.ylabel('$\dot{u}_g [m/s]$')

        axes = fig1.add_subplot(335)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, vy, 'k-', linewidth=1.0)

        axes = fig1.add_subplot(336)
        axes.get_xaxis().set_visible(False)
        plt.plot(t, vz, 'k-', linewidth=1.0)

        axes = fig1.add_subplot(337)
        plt.plot(t, ux, 'k-', linewidth=1.0)
        plt.ylabel('${u}_g [m]$')
        plt.xlabel('Time [sec]')

        axes = fig1.add_subplot(338)
        plt.plot(t, uy, 'k-', linewidth=1.0)
        plt.xlabel('Time [sec]')

        axes = fig1.add_subplot(339)
        plt.plot(t, uz, 'k-', linewidth=1.0)
        plt.xlabel('Time [sec]')

        plt.show()
        print('\n'"Press any key to continue...")
        plt.waitforbuttonpress()


    # Print the ground motions to file
    outFileID = open('gm_long.txt', 'w')
    for step in range(numTimePoints):
        line = ("%12.6E" % ax[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    outFileID = open('gm_perp.txt', 'w')
    for step in range(numTimePoints):
        line = ("%12.6E" % ay[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    outFileID = open('gm_vert.txt', 'w')
    for step in range(numTimePoints):
        line = ("%12.6E" % az[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()
