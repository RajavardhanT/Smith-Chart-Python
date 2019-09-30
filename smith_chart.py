from pylab import *
def plot_smith():
    
    theta = linspace(0,2*pi,1024)
    figure(figsize=(8,8))
    for r in [0,0.2,0.5,1,2,10]:
        plot( 1/(1+r)*cos(theta) + r/(1+r), 1/(1+r) * sin(theta),'r' ,alpha=0.2,label=r)
        # Reistance numbers
        text( -1/(1+r) + r/(1+r),0.02,r'%0.1f'%r)

    for r in [0.1,0.3,0.7,5]:
        plot( 1/(1+r)*cos(theta) + r/(1+r), 1/(1+r) * sin(theta),'r' ,alpha=0.05,label=r)
        # Reistance numbers
        text( -1/(1+r) + r/(1+r),0.02,r'%0.1f'%r)


    # For mpl cursor visibility of the r value    
    for r in logspace(0,1,64):
        plot( 1/(1+r)*cos(theta) + r/(1+r), 1/(1+r) * sin(theta),'r' ,alpha=0.005,label='r=%0.2f'%r)

    for r in logspace(-3,0,64):
        plot( 1/(1+r)*cos(theta) + r/(1+r), 1/(1+r) * sin(theta),'r' ,alpha=0.005,label='r=%0.2f'%r)
    


    
    for x in [-5,-2,-1,-0.5,-0.2,0.2,0.5,1,2,5]:
        # To plot only inside the circle
        xx = cos(theta)/x + 1
        yy = 1/x * sin(theta) + 1/x
        mag = (xx**2 + yy**2)**0.5
        # Those values with magnitude less than 1 are selected
        xx[mag>1] = NaN
        yy[mag>1] = NaN
        plot( xx,yy,'g',alpha=0.2)


        
    # Impedance numbers
    text(-0.88,0.417,'0.2')
    text(-0.56,0.803,'0.5')
    text(0.01,0.97,'1')
    text(0.6,0.732,'2')
    text(0.830,0.381,'5')

    # For mpl cursor visibility of the x value    
    for x in logspace(0,1,64):
        # To plot only inside the circle
        xx = cos(theta)/x + 1
        yy = 1/x * sin(theta) + 1/x
        mag = (xx**2 + yy**2)**0.5        
        xx[mag>1] = NaN
        yy[mag>1] = NaN
        plot( xx,yy,'y',alpha=0.05,label='x=%0.2f'%x)

    for x in logspace(-2,0,64):
        # To plot only inside the circle
        xx = cos(theta)/x + 1
        yy = 1/x * sin(theta) + 1/x
        mag = (xx**2 + yy**2)**0.5        
        xx[mag>1] = NaN
        yy[mag>1] = NaN
        plot( xx,yy,'y',alpha=0.05,label='x=%0.2f'%x)

    for x in -1*logspace(0,1,64):
        # To plot only inside the circle
        xx = cos(theta)/x + 1
        yy = 1/x * sin(theta) + 1/x
        mag = (xx**2 + yy**2)**0.5        
        xx[mag>1] = NaN
        yy[mag>1] = NaN
        plot( xx,yy,'y',alpha=0.05,label='x=%0.2f'%x)

    for x in -1*logspace(-2,0,64):
        # To plot only inside the circle
        xx = cos(theta)/x + 1
        yy = 1/x * sin(theta) + 1/x
        mag = (xx**2 + yy**2)**0.5        
        xx[mag>1] = NaN
        yy[mag>1] = NaN
        plot( xx,yy,'y',alpha=0.05,label='x=%0.2f'%x)

    #####################################################
    
    axhline(y=0,color='k',alpha=0.2)
    axvline(x=0,color='k',alpha=0.2)

    phi = linspace(0,360,37)
    for p in phi:
        plot(1.01*cos(p*pi/180),1.01*sin(p*pi/180),marker=(3,0,p+90),c='k',linestyle='None')
        text(1.08*cos(p*pi/180),1.08*sin(p*pi/180),r'%d$^\circ$'%p
             ,horizontalalignment='center'
             ,verticalalignment='center')

        # Yellow patch
        #plot(1.02*cos(theta),1.015*sin(theta),c='ivory',lw=4,alpha=0.4)
        # Ticks on the outer circle
    phi = linspace(0,360,181)
    for p in phi:
        plot(1.01*cos(p*pi/180),1.01*sin(p*pi/180),marker=(2,0,p+90),c='k',linestyle='None',alpha=0.3)
            

            

    #for r in [0,0.2,0.5,0.8]:
    #    plot(r*cos(theta),r*sin(theta),'m--',lw=0.5,alpha=0.1)
    
    text(1.05,0.05,'OC')
    text(-1.1,0.05,'SC')
        
    xlim(-1.15,1.15)
    ylim(-1.15,1.15)


    xticks([])
    yticks([])

    box(False)
