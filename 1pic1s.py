import time, gtk.gdk

i=1
while 1:
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        name="screenshot%03d.png" % (i,)
        pb.save(name ,"png")
        print "Screenshot saved to %s." % (name,)
        time.sleep(1)
        i+=1
    else:
        print "Unable to get the screenshot."
