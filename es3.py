from pyo import *

s = Server().boot()
s.setAmp(0.6)

a = Input(chnl = 0, mul = 1)
p = Pan(a,outs=2,pan=0.5)


fmap=SLMap(50,200,'lin','freq',50)
mmap=SLMap(0,1.2,'lin','mul',0.5)
rm = Sine(freq = 100)
rm.ctrl(map_list=[fmap,mmap])

y = ButLP(rm*p,freq= 1000, mul = 1)
y.ctrl()



y.out()

s.gui(locals())