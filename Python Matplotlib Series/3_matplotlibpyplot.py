# you can use argument marker to emphasize each point with specified marker.
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker= 'o') # kuch bhi de sakte hai jaise @, s, p
plt.show()

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker= '*') # same yha bhi
plt.show()

# format string "fmt" - marker|line|color
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])
plt.plot(ypoints, 'o:r') # o - circle , r - color
plt.show()

# line reference 
# - solid line 
# : dotted line
# -- dashed line
# -. dashline/dotted line

# color reference
# r red
# g green
# b blue
# c cyan
# m magenta
# y yellow
# k black
# w white 


# marker size 
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

#  marker edge color - mec
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()'''

# marker face color - mfc

import matplotlib.pyplot as plt
import numpy as np
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'y', mfc = 'r' )
plt.show()

# hum # value bhi de sakte hai color ka jaise red- #FF0000
