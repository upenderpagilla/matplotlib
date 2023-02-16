'''
What is Matplotlib?
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

Where is the Matplotlib Codebase?
The source code for Matplotlib is located at this github repository https://github.com/matplotlib/matplotlib



'''

''''

Installation of Matplotlib
If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

Install it using this command:

C:\Users\Your Name>pip install matplotlib
If this command fails, then use a python distribution that already has Matplotlib installed,  like Anaconda, Spyder etc.

Import Matplotlib
Once Matplotlib is installed, import it in your applications by adding the import module statement:

'''

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()