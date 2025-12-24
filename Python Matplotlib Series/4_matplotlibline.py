# linestyple or ls - is used to chnage the styple of the plotted line.
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

# line color - c
import matplotlib.pyplot as plt 
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, color = '#4CAF50')
plt.show()

# line width - width of a line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()

# example for multiple line
import matplotlib.pyplot as plt
import numpy as np

xpoints = ([6, 2, 7, 11])
ypoints = ([3,8,1,10])
plt.plot(xpoints, ypoints, linewidth = '20.5')
plt.show()


# example for multiple line
import matplotlib.pyplot as plt
import numpy as np

# lines ko add kr diya xaxis bhi ayr axis bhi.
xpoints = ([3,8,1,10])
ypoints = ([6,2,7,11])
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()


