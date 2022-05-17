import numpy as np
import matplotlib.pyplot as plt
import eqsig.single

# Load Christchurch Ground Motions

dt = 0.005  # time step of acceleration time series

ax1 = []
f = open(r"GroundAccelerationX.txt", "r")
lines = f.readlines()
for oneline in lines:
    splitline = oneline.split()
    for j in range(len(splitline)):
        value = float(splitline[j]) * 1.2
        ax1.append(value)
# Create the time axis
numTimePointsAx1 = len(ax1)
tAx1 = np.linspace(0, dt * numTimePointsAx1, numTimePointsAx1)

# ax2 = []
# f = open(r"C:\Users\swan0075\Dropbox\Swanand-Terje\Thesis Figures\Christchurch NGA West 2 Data\RSN8066_CCHURCH_CHHCN01W.AT2", "r")
# lines = f.readlines()
# for oneline in lines:
#     splitline = oneline.split()
#     for j in range(len(splitline)):
#         value = float(splitline[j])
#         ax2.append(value)
# # Create the time axis
# numTimePointsAx2 = len(ax2)
# tAx2 = np.linspace(0, dt * numTimePointsAx2, numTimePointsAx2)
#
# ax3 = []
# f = open(r"C:\Users\swan0075\Dropbox\Swanand-Terje\Thesis Figures\Christchurch NGA West 2 Data\RSN8119_CCHURCH_PRPCS.AT2", "r")
# lines = f.readlines()
# for oneline in lines:
#     splitline = oneline.split()
#     for j in range(len(splitline)):
#         value = float(splitline[j])
#         ax3.append(value)
# # Create the time axis
# numTimePointsAx3 = len(ax3)
# tAx3 = np.linspace(0, dt * numTimePointsAx3, numTimePointsAx3)
#
# ax4 = []
# f = open(r"C:\Users\swan0075\Dropbox\Swanand-Terje\Thesis Figures\Christchurch NGA West 2 Data\RSN8123_CCHURCH_REHSN02E.AT2", "r")
# lines = f.readlines()
# for oneline in lines:
#     splitline = oneline.split()
#     for j in range(len(splitline)):
#         value = float(splitline[j])
#         ax4.append(value)
# # Create the time axis
# numTimePointsAx4 = len(ax4)
# tAx4 = np.linspace(0, dt * numTimePointsAx4, numTimePointsAx4)
#
#
# ax5 = []
# f = open(r"C:\Users\swan0075\Dropbox\Swanand-Terje\Thesis Figures\Christchurch NGA West 2 Data\RSN8157_CCHURCH_HVSCS26W.AT2", "r")
# lines = f.readlines()
# for oneline in lines:
#     splitline = oneline.split()
#     for j in range(len(splitline)):
#         value = float(splitline[j])
#         ax5.append(value)
# # Create the time axis
# numTimePointsAx5 = len(ax5)
# tAx5 = np.linspace(0, dt * numTimePointsAx5, numTimePointsAx5)



periods = np.linspace(0.01, 12, 100)  # compute the response for 100 periods between T=0.2s and 5.0s
record1 = eqsig.AccSignal((ax1), dt)
record1.generate_response_spectrum(response_times=periods)
times = record1.response_times
# record2 = eqsig.AccSignal((ax2), dt)
# record2.generate_response_spectrum(response_times=periods)
#
# record3 = eqsig.AccSignal((ax3), dt)
# record3.generate_response_spectrum(response_times=periods)
#
# record4 = eqsig.AccSignal((ax4), dt)
# record4.generate_response_spectrum(response_times=periods)
#
# record5 = eqsig.AccSignal((ax5), dt)
# record5.generate_response_spectrum(response_times=periods)

plt.ion()
plt.figure(1)
plt.grid(True)
plt.autoscale(True)
plt.xscale("log")
plt.yscale("log")
plt.plot((times), (record1.s_a), color = "black")
# plt.plot((times), (record2.s_a), label = "CHHC")
# plt.plot((times), (record3.s_a), label = "PRPC")
# plt.plot((times), (record4.s_a), label = "REHS")
# plt.plot((times), (record5.s_a), label = "HVSC")
plt.xlabel('Period [s]')
plt.ylabel('Sa [g]')
#plt.legend()
plt.show()
plt.savefig('Chapter5Spectrum')
print('\n'"Press any key to continue...")
plt.waitforbuttonpress()

# Fourier transform

spectrum = np.fft.fft(ax1)
freq = np.fft.fftfreq(tAx1.shape[-1])
spectrum = abs(spectrum[:len(spectrum)//5])
freq = freq[:len(freq)//5]/dt

plt.ion()
plt.figure(4)
plt.grid(True)
plt.plot(freq, spectrum.real, 'k-')
plt.xlabel("Frequency")
plt.title("Fourier Transform")
plt.savefig('FourierTransform')

plt.ion()
plt.figure(2)
plt.grid(True)
plt.autoscale(True)
plt.title("CCCC")
plt.plot(tAx1, ax1, 'k-')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration [g]')
plt.show()
plt.savefig('Chapter5CCCC')
print('\n'"Press any key to continue...")
plt.waitforbuttonpress()

# plt.ion()
# plt.figure(3)
# plt.grid(True)
# plt.autoscale(True)
# plt.title("CHHC")
# # plt.plot(tAx2, ax2, 'k-')
# # plt.xlabel('Time (s)')
# # plt.ylabel('Acceleration [g]')
# # plt.show()
# # plt.savefig('Chapter5CHHC')
# # print('\n'"Press any key to continue...")
# # plt.waitforbuttonpress()
#
# plt.ion()
# plt.figure(4)
# plt.grid(True)
# plt.autoscale(True)
# plt.title("PRPC")
# plt.plot(tAx3, ax3, 'k-')
# plt.xlabel('Time (s)')
# plt.ylabel('Acceleration [g]')
# plt.show()
# plt.savefig('Chapter5PRPC')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
# plt.ion()
# plt.figure(5)
# plt.grid(True)
# plt.autoscale(True)
# plt.title("REHS")
# plt.plot(tAx4, ax4, 'k-')
# plt.xlabel('Time (s)')
# plt.ylabel('Acceleration [g]')
# plt.show()
# plt.savefig('Chapter5REHS')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
# plt.ion()
# plt.figure(6)
# plt.grid(True)
# plt.autoscale(True)
# plt.title("HVSC")
# plt.plot(tAx5, ax5, 'k-')
# plt.xlabel('Time (s)')
# plt.ylabel('Acceleration [g]')
# plt.show()
# plt.savefig('Chapter5HVSC')
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()
#
# # Plot
#
# plt.ion()
# fig1 = plt.figure(100)
# plt.grid(True)
# plt.autoscale(True)
# plt.axis('off')
#
# axes = fig1.add_subplot(511)
# axes.get_xaxis().set_visible(False)
# plt.plot(tAx1, ax1, 'k-', linewidth=1.0)
#
#
# axes = fig1.add_subplot(512)
# axes.get_xaxis().set_visible(False)
# plt.plot(tAx2, ax2, 'k-', linewidth=1.0)
#
# axes = fig1.add_subplot(513)
# axes.get_xaxis().set_visible(False)
# plt.plot(tAx3, ax3, 'k-', linewidth=1.0)
#
# axes = fig1.add_subplot(514)
# axes.get_xaxis().set_visible(False)
# plt.plot(tAx4, ax4, 'k-', linewidth=1.0)
#
# axes = fig1.add_subplot(515)
# axes.get_xaxis().set_visible(False)
# plt.plot(tAx5, ax5, 'k-', linewidth=1.0)
#
# plt.tight_layout()
# plt.show()
# plt.savefig("Chapter5Records")
# print('\n'"Press any key to continue...")
# plt.waitforbuttonpress()

# plt.loglog([0, 0.05,0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0], [0.365, 0.447,0.680,0.840, 0.844, 0.748, 0.422, 0.255, 0.081, 0.028], 'r')
# plt.loglog([0,.05,0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0], [0.347,0.8684,0.8684,0.8684, 0.8684, 0.8684, 0.536362, 0.3385, 0.1121, 0.0378], 'g')




