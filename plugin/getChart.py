import numpy as np
import matplotlib.pyplot as plt

def do(records):
    x=[0.0]
    y=[0.0]
    z=[0.0]
    for i in range(len(records)):
        x.append(i+1)
        y.append(records[i].change)
        z.append(records[i].balance)
    
    plt.figure()
    plt.plot(x,y,label="$delta$",color="red",linewidth=2)
    plt.plot(x,z,"b--",label="$balance$")
    plt.plot([0],[0])
    plt.legend()
    plt.show()
    


