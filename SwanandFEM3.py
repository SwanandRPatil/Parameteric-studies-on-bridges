
# -------------------------------------------------------------
# T-FRAME
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
    model('basic', '-ndm', 3, '-ndf', 6)


    # Nodes that lie in the x-y-plane
    node(10007, 3.4000, 0.0000, 7.8000)
    node(10014, 6.8000, 0.0000, 7.8000)
    node(10021, 10.2000, 0.0000, 7.8000)
    node(10028, 13.6000, 0.0000, 7.8000)
    node(10035, 17.0000, 0.0000, 7.8000)
    node(10042, 23.8000, 0.0000, 7.8000)
    node(10049, 27.3000, 0.0000, 7.8000)
    node(10056, 30.7000, 0.0000, 7.8000)
    node(10063, 34.1000, 0.0000, 7.8000)
    node(10070, 37.5000, 0.0000, 7.8000)
    node(10077, 44.3000, 0.0000, 7.8000)
    node(10084, 47.7000, 0.0000, 7.8000)
    node(10091, 51.1000, 0.0000, 7.8000)
    node(10098, 54.5000, 0.0000, 7.8000)
    node(10105, 57.9000, 0.0000, 7.8000)
    node(10112, 64.7000, 0.0000, 7.8000)
    node(10119, 68.1000, 0.0000, 7.8000)
    node(10126, 71.5000, 0.0000, 7.8000)
    node(10133, 75.0000, 0.0000, 7.8000)
    node(10140, 78.4000, 0.0000, 7.8000)
    node(10147, 85.2000, 0.0000, 7.8000)
    node(10154, 88.6000, 0.0000, 7.8000)
    node(10161, 92.0000, 0.0000, 7.8000)
    node(10168, 95.4000, 0.0000, 7.8000)
    node(10175, 98.8000, 0.0000, 7.8000)
    node(10182, 105.6000, 0.0000, 7.8000)
    node(10189, 109.0000, 0.0000, 7.8000)
    node(10196, 112.4000, 0.0000, 7.8000)
    node(10203, 115.8000, 0.0000, 7.8000)
    node(10210, 119.2000, 0.0000, 7.8000)
    node(10217, 126.1000, 0.0000, 7.8000)
    node(10224, 129.5000, 0.0000, 7.8000)
    node(10231, 132.9000, 0.0000, 7.8000)
    node(10238, 136.3000, 0.0000, 7.8000)
    node(10245, 139.7000, 0.0000, 7.8000)
    node(10252, 146.5000, 0.0000, 7.8000)
    node(10259, 149.9000, 0.0000, 7.8000)
    node(10266, 153.3000, 0.0000, 7.8000)
    node(10273, 156.7000, 0.0000, 7.8000)
    node(10280, 160.1000, 0.0000, 7.8000)
    node(10287, 166.9000, 0.0000, 7.8000)
    node(10294, 170.4000, 0.0000, 7.8000)
    node(10301, 173.8000, 0.0000, 7.8000)
    node(10308, 177.2000, 0.0000, 7.8000)
    node(10315, 180.6000, 0.0000, 7.8000)
    node(12007, 0.0000, 0.0000, 7.8000)
    node(12014, 20.4000, 0.0000, 7.8000)
    node(12021, 20.4000, 0.0000, 7.8000)
    node(12028, 40.9000, 0.0000, 7.8000)
    node(12035, 40.9000, 0.0000, 7.8000)
    node(12042, 61.3000, 0.0000, 7.8000)
    node(12049, 61.3000, 0.0000, 7.8000)
    node(12056, 81.8000, 0.0000, 7.8000)
    node(12063, 81.8000, 0.0000, 7.8000)
    node(12070, 102.2000, 0.0000, 7.8000)
    node(12077, 102.2000, 0.0000, 7.8000)
    node(12084, 122.7000, 0.0000, 7.8000)
    node(12091, 122.7000, 0.0000, 7.8000)
    node(12098, 143.1000, 0.0000, 7.8000)
    node(12105, 143.1000, 0.0000, 7.8000)
    node(12112, 163.5000, 0.0000, 7.8000)
    node(12119, 163.5000, 0.0000, 7.8000)
    node(12126, 184.0000, 0.0000, 7.8000)
    node(507, 0.0000, 0.0000, 7.8000)
    node(514, 0.0000, 0.0000, 7.8000)
    node(521, 20.4000, 0.0000, 7.8000)
    node(528, 20.4000, -3.3000, 7.8000)
    node(535, 40.9000, 0.0000, 7.8000)
    node(542, 40.9000, -3.3000, 7.8000)
    node(549, 61.3000, 0.0000, 7.8000)
    node(556, 61.3000, -3.3000, 7.8000)
    node(563, 81.8000, 0.0000, 7.8000)
    node(570, 81.8000, -3.3000, 7.8000)
    node(577, 102.2000, 0.0000, 7.8000)
    node(584, 102.2000, -3.3000, 7.8000)
    node(591, 122.7000, 0.0000, 7.8000)
    node(598, 122.7000, -3.3000, 7.8000)
    node(605, 143.1000, 0.0000, 7.8000)
    node(612, 143.1000, -3.3000, 7.8000)
    node(619, 163.5000, 0.0000, 7.8000)
    node(626, 163.5000, -3.3000, 7.8000)
    node(633, 184.0000, 0.0000, 7.8000)
    node(640, 184.0000, 0.0000, 7.8000)
    node(8007, 20.4000, -54.4000, 7.8000)
    node(8008, 20.4000, -54.4000, 7.8000)
    node(8015, 40.9000, -54.4000, 7.8000)
    node(8016, 40.9000, -54.4000, 7.8000)
    node(8023, 61.3000, -54.4000, 7.8000)
    node(8024, 61.3000, -54.4000, 7.8000)
    node(8031, 81.8000, -54.4000, 7.8000)
    node(8032, 81.8000, -54.4000, 7.8000)
    node(8039, 102.2000, -54.4000, 7.8000)
    node(8040, 102.2000, -54.4000, 7.8000)
    node(8047, 122.7000, -54.4000, 7.8000)
    node(8048, 122.7000, -54.4000, 7.8000)
    node(8055, 143.1000, -54.4000, 7.8000)
    node(8056, 143.1000, -54.4000, 7.8000)
    node(8063, 163.5000, -54.4000, 7.8000)
    node(8064, 163.5000, -54.4000, 7.8000)
    node(1200, 20.4000, -3.3000, 7.8000)
    node(1201, 20.4000, -6.6000, 7.8000)
    node(1202, 20.4000, -7.6000, 7.8000)
    node(1203, 20.4000, -8.7000, 7.8000)
    node(1204, 20.4000, -8.9000, 7.8000)
    node(1205, 20.4000, -9.1000, 7.8000)
    node(1206, 20.4000, -9.3000, 7.8000)
    node(1207, 20.4000, -9.5000, 7.8000)
    node(1208, 20.4000, -9.7000, 7.8000)
    node(1400, 40.9000, -3.3000, 7.8000)
    node(1401, 40.9000, -6.6000, 7.8000)
    node(1402, 40.9000, -7.6000, 7.8000)
    node(1403, 40.9000, -8.7000, 7.8000)
    node(1404, 40.9000, -8.9000, 7.8000)
    node(1405, 40.9000, -9.1000, 7.8000)
    node(1406, 40.9000, -9.3000, 7.8000)
    node(1407, 40.9000, -9.5000, 7.8000)
    node(1408, 40.9000, -9.7000, 7.8000)
    node(1600, 61.3000, -3.3000, 7.8000)
    node(1601, 61.3000, -6.6000, 7.8000)
    node(1602, 61.3000, -7.6000, 7.8000)
    node(1603, 61.3000, -8.7000, 7.8000)
    node(1604, 61.3000, -8.9000, 7.8000)
    node(1605, 61.3000, -9.1000, 7.8000)
    node(1606, 61.3000, -9.3000, 7.8000)
    node(1607, 61.3000, -9.5000, 7.8000)
    node(1608, 61.3000, -9.7000, 7.8000)
    node(1800, 81.8000, -3.3000, 7.8000)
    node(1801, 81.8000, -6.6000, 7.8000)
    node(1802, 81.8000, -7.6000, 7.8000)
    node(1803, 81.8000, -8.7000, 7.8000)
    node(1804, 81.8000, -8.9000, 7.8000)
    node(1805, 81.8000, -9.1000, 7.8000)
    node(1806, 81.8000, -9.3000, 7.8000)
    node(1807, 81.8000, -9.5000, 7.8000)
    node(1808, 81.8000, -9.7000, 7.8000)
    node(2000, 102.2000, -3.3000, 7.8000)
    node(2001, 102.2000, -6.6000, 7.8000)
    node(2002, 102.2000, -7.6000, 7.8000)
    node(2003, 102.2000, -8.7000, 7.8000)
    node(2004, 102.2000, -8.9000, 7.8000)
    node(2005, 102.2000, -9.1000, 7.8000)
    node(2006, 102.2000, -9.3000, 7.8000)
    node(2007, 102.2000, -9.5000, 7.8000)
    node(2008, 102.2000, -9.7000, 7.8000)
    node(2200, 122.7000, -3.3000, 7.8000)
    node(2201, 122.7000, -6.6000, 7.8000)
    node(2202, 122.7000, -7.6000, 7.8000)
    node(2203, 122.7000, -8.7000, 7.8000)
    node(2204, 122.7000, -8.9000, 7.8000)
    node(2205, 122.7000, -9.1000, 7.8000)
    node(2206, 122.7000, -9.3000, 7.8000)
    node(2207, 122.7000, -9.5000, 7.8000)
    node(2208, 122.7000, -9.7000, 7.8000)
    node(2400, 143.1000, -3.3000, 7.8000)
    node(2401, 143.1000, -6.6000, 7.8000)
    node(2402, 143.1000, -7.6000, 7.8000)
    node(2403, 143.1000, -8.7000, 7.8000)
    node(2404, 143.1000, -8.9000, 7.8000)
    node(2405, 143.1000, -9.1000, 7.8000)
    node(2406, 143.1000, -9.3000, 7.8000)
    node(2407, 143.1000, -9.5000, 7.8000)
    node(2408, 143.1000, -9.7000, 7.8000)
    node(2600, 163.5000, -3.3000, 7.8000)
    node(2601, 163.5000, -6.6000, 7.8000)
    node(2602, 163.5000, -7.6000, 7.8000)
    node(2603, 163.5000, -8.7000, 7.8000)
    node(2604, 163.5000, -8.9000, 7.8000)
    node(2605, 163.5000, -9.1000, 7.8000)
    node(2606, 163.5000, -9.3000, 7.8000)
    node(2607, 163.5000, -9.5000, 7.8000)
    node(2608, 163.5000, -9.7000, 7.8000)
