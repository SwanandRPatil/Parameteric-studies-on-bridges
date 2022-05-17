import numpy as np
import matplotlib.pyplot as plt
import eqsig.single


bf, sub_fig = plt.subplots()
numGM = 22

for i in range(numGM):
    a = np.loadtxt(r"C:\Users\swan0075\Dropbox\DesignSafeProject\gmRectified500_5_0.2\gm"+str(i)+"_500_5_0.2.dat")
    #print(a)
    dt = 0.01  # time step of acceleration time series
    periods = np.linspace(0.01, 12, 100)  # compute the response for 100 periods between T=0.2s and 5.0s
    record = eqsig.AccSignal((a / 9.81), dt)
    record.generate_response_spectrum(response_times=periods)
    times = record.response_times
    plt.xscale("log")
    plt.yscale("log")
    plt.plot((times), (record.s_a), 'k-')
    plt.xlabel('T (s)')
    plt.ylabel('Spectral acceleration [g]')
    plt.pause(0.01)


# plt.plot(([0, 0.05,0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0]), ([0.365, 0.447,0.680,0.840, 0.844, 0.748, 0.422, 0.255, 0.081, 0.028]), 'r', label='Sa(T)')
# plt.plot(([0,.05,0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0]), ([0.347,0.8684,0.8684,0.8684, 0.8684, 0.8684, 0.536362, 0.3385, 0.1121, 0.0378]), 'g', label='S(T)')

# plt.legend()
plt.savefig('Spectra_firm200')
plt.show()

# plt.loglog([0, 0.05,0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0], [0.365, 0.447,0.680,0.840, 0.844, 0.748, 0.422, 0.255, 0.081, 0.028], 'r')
# plt.loglog([0,.05,0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0], [0.347,0.8684,0.8684,0.8684, 0.8684, 0.8684, 0.536362, 0.3385, 0.1121, 0.0378], 'g')




