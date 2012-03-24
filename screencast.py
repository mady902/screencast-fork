import time, gtk.gdk, os, thread

DUR=0.5

i=1
thread.start_new_thread( os.system, ('arecord -f cd -c 1 -t wav > teste.wav',)  )
anterior=time.time()
while 1:
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    #print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        name="screenshot%05d.png" % (i,)
        pb.save(name ,"png")
        #print "Screenshot saved to %s." % (name,)
        lag=(time.time()-anterior)
        #correction = DUR - lag
        dur2 = DUR -lag
        j=2
        while (dur2 < 0):
            i+=1
            name2="screenshot%05d.png" % (i,)
            os.system('cp %s %s' % (name,name2))

            lag=(time.time()-anterior)
            dur2=j*DUR -lag; j+=1

        #print "lag=%.3f dur2=%.3f tot=%.3f" % (lag, dur2, lag+dur2)
        time.sleep(dur2)
        anterior=time.time()
        i+=1
    else:
        print "Unable to get the screenshot."
