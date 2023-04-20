from pyo import *

s = Server()
s.boot()
s.setAmp(0.2)

path = './sirenmono.wav'

amps = [0.9,1,0.5]

sh = SfPlayer(path, speed= 0.5, loop= True) * amps[0]
sf = SfPlayer(path, speed= 1, loop= True) * amps[1]
sd = SfPlayer(path, speed= 2, loop= True) * amps[2]

cf = MoogLP(sh+sh+sd,1000,0.5)
cf.ctrl()


nmap =SLMap(0.001,0.05,'lin','mul',0.01)
fmap =SLMap(0.05,0.2,'lin','freq',0.1)
mmap =SLMap(0,0.5,'lin','mul',0)

noise = PinkNoise()
noise.ctrl(map_list=[nmap],title='Pink Noise')
mod =Sine(freq = 0.1,add=1)
mod.ctrl(map_list=[fmap,mmap],title='Modulating wave')
n = noise * mod
Scope([cf,n,mod])


cf = Pan(cf, outs= 2,pan = 0.5).out()
n =  Pan(n, outs= 2,pan = 0.5).out()


s.gui(locals())


