#!/usr/bin/python
import smbus
import time

#==============================
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
from matplotlib import animation
#===============================

class L3G4200D(object):

    # Minimal constants carried over from Arduino library
    L3G4200D_ADDRESS = 0x69   #t0110100x
    address = L3G4200D_ADDRESS

    L3G4200D_REGISTER_WHO_AM_I = 0x0F
    L3G4200D_REGISTER_CTRL_REG1 = 0x20
    L3G4200D_REGISTER_CTRL_REG2 = 0x21
    L3G4200D_REGISTER_CTRL_REG3 = 0x22
    L3G4200D_REGISTER_CTRL_REG4 = 0x23
    L3G4200D_REGISTER_CTRL_REG5 = 0x24
    L3G4200D_REGISTER_OUT_X_L = 0x28
    L3G4200D_REGISTER_OUT_X_H = 0x29
    L3G4200D_REGISTER_OUT_Y_L = 0x2A
    L3G4200D_REGISTER_OUT_Y_H = 0x2B
    L3G4200D_REGISTER_OUT_Z_L = 0x2C
    L3G4200D_REGISTER_OUT_Z_H = 0x2D

    g = [0., 0., 0.]

    def __init__(self, debug=False, hires=False):

        # addresses, so invoke a separate I2C instance for each
        self.bus = smbus.SMBus(1)  # if rev 1, use SMBus(0)

        if self.bus.read_byte_data(self.address,
                self.L3G4200D_REGISTER_WHO_AM_I)&0xFF is not 0xD3:
            print "error"
        # Enable x, y, z and bandwidth 800Hz, cutoff 30Hz and turn off power down
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG1, 0xCF)
        # adjust/use the HPF cutoff 30Hz
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG2, 0x01)
        # No interrupts used on INT1, Data Ready on INT2
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG3, 0x08)
        # full-scale range
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG4, 0x00)
        # output selection 
        self.bus.write_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG5, 0x02)


    def gyro16(self, high, low):
        n = (high << 8) | low   # High, low bytes
        return n # 2's complement signed

    def read(self):
        # Read the gyroscope
        low = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_X_L)
        high = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_X_H)
        x = self.gyro16(high, low)
        low = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Y_L)
        high = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Y_H)
        y = self.gyro16(high, low)
        low = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Z_L)
        high = self.bus.read_byte_data(self.address,
          self.L3G4200D_REGISTER_OUT_Z_H)
        z = self.gyro16(high, low)
        if x & 0x8000: x -= 65536
        if y & 0x8000: y -= 65536
        if z & 0x8000: z -= 65536

        fs=self.bus.read_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG4)&0x30
        c1=self.bus.read_byte_data(self.address,
            self.L3G4200D_REGISTER_CTRL_REG1)

        s = 0.
        if fs == 0x00: s=8.75
        elif fs == 0x10: s=17.5
        elif fs == 0x20: s=70
        elif fs == 0x30: s=70
        self.g[0] = float(x) * s / 1000.
        self.g[1] = float(y) * s / 1000.
        self.g[2] = float(z) * s / 1000.

        return self.g

#======================================================
class Scope(object):
    
    # Initialization
    def __init__(self, ax,fn, xmax=10,ymax =200,xstart=0, ystart=-200,title='Angular Velocity',xlabel='Time [ms]',ylabel='Roll velocity'):


        self.xmax = xmax #x axis length
        self.xstart = xstart # x axis starting pt
        self.ymax = ymax #y axis length 
        self.ystart = ystart # y axis starting

        # Graph setting
        self.ax = ax 
        self.ax.set_xlim((self.xstart,self.xmax))
        self.ax.set_ylim((self.ystart,self.ymax))

        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

        self.x = [0] # x axis info 
#       self.y = [0] # y axis info
        self.y1 = [0] # y axis info
        self.y2 = [0] # y axis info
        self.y3 = [0] # y axis info

        self.value = [0,0,0] # Axis value
        self.fn = fn
        self.line1, = ax.plot([],[],'r-',label='Roll Vel.')
        self.line2, = ax.plot([],[],'y--',label='Pitch Vel.')
        self.line3, = ax.plot([],[],'b-.',label='Yaw Vel.')

#       Set legend
        ax.legend([self.line1,self.line2,self.line3],[self.line1.get_label(),self.line2.get_label(),self.line3.get_label()])


        self.ti = time.time() # Current time
        print("Init OK")

    # graph setting
    def update(self, i):
        # time difference
        tempo = time.time()-self.ti
        self.ti = time.time() # time update

        # value insert
        self.value = self.fn() # Call y function 
        self.x.append(tempo + self.x[-1]) # x insert
        self.y1.append(self.value[0]) # y insert
        self.y2.append(self.value[1]) # y insert
        self.y3.append(self.value[2]) # y insert
#        self.x.append(tempo + self.x[-1]) # x insert
        self.line1.set_data(self.x,self.y1)
        self.line2.set_data(self.x,self.y2)
        self.line3.set_data(self.x,self.y3)

        # x range update
        if self.x[-1] >= self.xstart + self.xmax :
             # half of x to the one side
            self.xstart = self.xstart + self.xmax/2
            self.ax.set_xlim(self.xstart,self.xstart + self.xmax)

            self.ax.figure.canvas.draw()

#        return (self.line, )
        return [self.line1, self.line2, self.line3]
  

fig, ax = plt.subplots()
ax.grid(True)

# value return to y axis and declaration before decl. of objec scope 
def insert():
#    value = np.random.randint(1,9) # random value between 1~$
#==================================
    l3d4200d = L3G4200D()
    data = l3d4200d.read()
#    value = data[0] 
    value = data

#==================================
    return value 

# Creation of object
scope = Scope(ax,insert, ystart = -200, ymax = 200)
    
# Call update method
ani = animation.FuncAnimation(fig, scope.update,interval=100,blit=True)
plt.show()
#======================================================

#if __name__ == '__main__':

#    l3d4200d = L3G4200D()

#    while True:
#        data = l3d4200d.read()
#        print("read value is %f,\t %f,\t %f" % (data[0], data[1], data[2]))
#        time.sleep(1)

#    l3d4200d.close()
