from pyo import *

s = Server()
s.boot()
s.setAmp(0.2)



low = LFO(freq = 220, sharp = 1, type = 2)

fmap =SLMap(1,5,'lin','freq',2)
mmap =SLMap(0,0.1,'lin','mul',1)
smap =SLMap(0,7,'lin','type',1,'int',0.025,True)

trem = LFO(freq = 2,sharp = 1,add = 1)
trem.ctrl(map_list=[fmap,mmap,smap], title = 'Tremolo')
#trem.ctrl()
low *= trem

r = Reson(low, freq = [1000,1200,1400],q = 10)

r = Biquad(r)

ffmap=SLMap(0,20000,'lin','freq',1000)
fqmap=SLMap(1,500,'lin','q',10)


r.ctrl(map_list=[ffmap,fqmap],title='LP Filter')

r.out()
Scope(r)
Spectrum(r)
s.gui(locals())
