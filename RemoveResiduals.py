
# -------------------------------------------------------------
# REMOVE RESIDUAL VELOCITY AND DISPLACEMENT FROM GROUND MOTION
# -------------------------------------------------------------


# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Camel-shaped correction function
def correction(t, duration, residualDisp, residualVel):

    if t <= 0 or t >= duration:
        return 0.0
    else:
        amp1 = (np.pi * residualVel)/(2 * duration)
        amp2 = (np.pi * (2 * residualDisp - duration * residualVel))/duration**2
        return amp1 * np.sin(np.pi * t / duration) + amp2 * np.sin(2*np.pi * t / duration)


# Trapezoidal integration
def trapezoidalRecordIntegration(delta_t, record):

    integrated = [0]
    for i in range(1, len(record)):
        integrated.append(integrated[i-1] + delta_t * 0.5 * (record[i-1]+record[i]))

    return integrated


# Declare the function that does the work
def removeResiduals(delta_t, doPlotting):


    # Load x-direction acceleration
    ax = []
    f = open("gm_perp.txt", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = float(splitline[j])
            ax.append(value)
    f.close()


    # Also address the ground motion at a distance, if that is present
    axDist = []
    f = open("gm_perp_dist.txt", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = float(splitline[j])
            axDist.append(value)
    f.close()


    # Load y-direction acceleration
    ay = []
    f = open("gm_long.txt", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = float(splitline[j])
            ay.append(value)
    f.close()


    # Load z-direction acceleration
    az = []
    f = open("gm_vert.txt", "r")
    lines = f.readlines()
    for oneline in lines:
        splitline = oneline.split()
        for j in range(len(splitline)):
            value = float(splitline[j])
            az.append(value)
    f.close()


    # Calculate duration and create time axis
    numPoints = len(ax)
    duration = delta_t * numPoints
    t = np.linspace(0, duration, numPoints)


    # Integrate acceleration to obtain velocity
    vx = trapezoidalRecordIntegration(delta_t, ax)
    #vxDist = trapezoidalRecordIntegration(delta_t, axDist)
    vy = trapezoidalRecordIntegration(delta_t, ay)
    vz = trapezoidalRecordIntegration(delta_t, az)


    # Integrate velocity to obtain displacement
    ux = trapezoidalRecordIntegration(delta_t, vx)
    #uxDist = trapezoidalRecordIntegration(delta_t, vxDist)
    uy = trapezoidalRecordIntegration(delta_t, vy)
    uz = trapezoidalRecordIntegration(delta_t, vz)


    # Determine residuals
    residualVelocityX = vx[numPoints-1]
    #residualVelocityXDist = vxDist[numPoints-1]
    residualVelocityY = vy[numPoints-1]
    residualVelocityZ = vz[numPoints-1]

    residualDisplacementX = ux[numPoints-1]
    #residualDisplacementXDist = uxDist[numPoints-1]
    residualDisplacementY = uy[numPoints-1]
    residualDisplacementZ = uz[numPoints-1]


    # Print residuals
    print('\n'"Original residual ground velocity %.6f and displacement %.6f" % (residualVelocityX, residualDisplacementX))


    # Plot the correction function
    if doPlotting:
        corrFcn = []
        for i in range(numPoints):
            corrFcn.append(correction(t[i], duration, residualDisplacementX, residualVelocityX))
        plt.ion()
        plt.figure(20)
        plt.plot(t, corrFcn, 'k-')
        plt.xlabel("Time")
        plt.title("Acceleration Correction")
        plt.show()


    # Produce new acceleration time histories
    for i in range(numPoints):
        ax[i] -= correction(t[i], duration, residualDisplacementX, residualVelocityX)
        #axDist[i] -= correction(t[i], duration, residualDisplacementXDist, residualVelocityXDist)
        ay[i] -= correction(t[i], duration, residualDisplacementY, residualVelocityY)
        az[i] -= correction(t[i], duration, residualDisplacementZ, residualVelocityZ)


    # Integrate acceleration to obtain velocity
    vx = trapezoidalRecordIntegration(delta_t, ax)
    #vxDist = trapezoidalRecordIntegration(delta_t, axDist)
    vy = trapezoidalRecordIntegration(delta_t, ay)
    vz = trapezoidalRecordIntegration(delta_t, az)


    # Integrate velocity to obtain displacement
    ux = trapezoidalRecordIntegration(delta_t, vx)
    #uxDist = trapezoidalRecordIntegration(delta_t, vxDist)
    uy = trapezoidalRecordIntegration(delta_t, vy)
    uz = trapezoidalRecordIntegration(delta_t, vz)


    # Print residuals
    print('\n'"New residual ground velocity %.6f and displacement %.6f" % (vx[numPoints-1], ux[numPoints-1]))


    # Plot
    if doPlotting:
        plt.ion()
        fig1 = plt.figure(100)
        plt.axis('off')
        plt.title('Ground Motion without Residuals')

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

        plt.show()
        plt.savefig("GM3MotionsWithoutResidual")

        # print('\n'"Press any key to continue...")
        # plt.waitforbuttonpress()


    # Print the ground motions to file
    outFileID = open('gm_perp.txt', 'w')
    for step in range(numPoints):
        line = ("%12.6E" % ax[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    # outFileID = open('gm_perp_dist.txt', 'w')
    # for step in range(numPoints):
    #     line = ("%12.6E" % axDist[step])
    #     line += '\n'
    #     outFileID.write(line)
    # outFileID.close()

    outFileID = open('gm_long.txt', 'w')
    for step in range(numPoints):
        line = ("%12.6E" % ay[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()

    outFileID = open('gm_vert.txt', 'w')
    for step in range(numPoints):
        line = ("%12.6E" % az[step])
        line += '\n'
        outFileID.write(line)
    outFileID.close()
