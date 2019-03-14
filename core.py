"""
Initialize
    and import
"""
import sys
import csv
import os
import glob
import random
import math

def tConvert(time1, unit1):

    if unit1=='s':
        m, s = divmod(time1, 60)
        h, m = divmod(m, 60)
        # print( "%d:%02d:%02d" % (h, m, s))
    else:
        h, m = divmod(time1, 60)
        # print ("%d:%02d" % (h, m))
    return h, m

def MakeArray(var1):
    ArrayL = []
    for i in range(var1): # This creates a list with index of 0 to var1-1
        ArrayL.append(i)
    return ArrayL


def main():
    """
    Main program entry.  This program returns random on/off intervals for on/off
    periods of a programble timer
    """
    print ('hello')
    print ('you need four arguments')
    print('format: <num of intervals> <Max on time> <max off itme> <min on and off time> ')


    if len(sys.argv) < 4:
        print('ERROR: Not enough arguments')
        exit()
    else:
        in1 = sys.argv[1]
        in2 = sys.argv[2]
        in3 = sys.argv[3]
        in4 = sys.argv[4]
        # you call the function by using the function name and pass a parameter
        print('You entered:',in1,in2,in3,in4)


        """
        Logic:
        in1=Number of time intervals
        in2=Max On-Time in minutes
        in3=Max Off-Time in minutes
        in4=Min on/off time in minute

        for all intervals generate a random number from min to Max on-time and
        one for max off-time then build array and display it
        """
        All_max_ONtimes  = MakeArray(int(in1))
        All_max_OFFtimes = MakeArray(int(in1))

        x = 0
        TotalOffTime = 0
        TotalOnTime = 0
        while  x < int(in1):
            All_max_OFFtimes [x] = random.randint(int(in4),int(in3))
            TotalOffTime = TotalOffTime + All_max_OFFtimes [x]
            All_max_ONtimes [x] = random.randint(int(in4),int(in2))
            TotalOnTime = TotalOnTime + All_max_ONtimes [x]
            x+=1
        # print(All_max_ONtimes)
        # print(All_max_OFFtimes)

        for z in range(len(All_max_ONtimes)):
            print ('Timer',z+1,' (ON=',All_max_ONtimes[z],'\tOFF=',All_max_OFFtimes[z],')')
            hon, mon = tConvert(All_max_ONtimes[z],'m')
            hoff, moff  = tConvert(All_max_OFFtimes[z],'m')
            print ('Timer',z+1,' (ON=',"%d:%02d" % (hon, mon),'\tOFF=', "%d:%02d)\n" % (hoff, moff))
        print('On=',TotalOnTime,' off=', TotalOffTime)
        TotalTime = TotalOnTime + TotalOffTime

        hon, mon = tConvert(TotalOnTime,'m')
        hoff, moff= tConvert(TotalOffTime,'m')
        print ('All = ', TotalTime, 'All ON=',"%d:%02d" % (hon, mon),'\t All OFF=', "%d:%02d\n" % (hoff, moff))
        #AdjustTime = (1440-TotalTime)/(2*int(in1))
        AdjustTime = (1440-TotalTime)/(int(in1))
        print('Need to adjust by ',AdjustTime, 'minutes per divsion')

        TotalOffTime = 0
        TotalOnTime = 0
        Previous1 = 0
        Previous2 = 0
        for z in range(len(All_max_ONtimes)):
            All_max_ONtimes[z] = All_max_ONtimes[z] + AdjustTime 
            #All_max_OFFtimes[z] = All_max_OFFtimes[z] + AdjustTime
            TotalOffTime = TotalOffTime + All_max_OFFtimes [z]
            TotalOnTime = TotalOnTime + All_max_ONtimes [z]
            if z >= 1:
                All_max_ONtimes[z] = All_max_ONtimes[z] + All_max_OFFtimes[z-1]
                All_max_OFFtimes[z] = All_max_OFFtimes[z] + All_max_ONtimes[z]
            else:
                All_max_OFFtimes[z] = All_max_OFFtimes[z] + All_max_ONtimes[z]

            # print ('Timer',z+1,' (ON=',All_max_ONtimes[z],'\tOFF=',All_max_OFFtimes[z],')')
            hon, mon = tConvert(All_max_ONtimes[z],'m')
            hoff, moff  = tConvert(All_max_OFFtimes[z],'m')
            print ('Timer',z+1,' (ON=',"%d:%02d" % (hon, mon),'\tOFF=', "%d:%02d)\n" % (hoff, moff))
        print('On=', math.floor(TotalOnTime),' off=',  math.floor(TotalOffTime))
        TotalTime = TotalOnTime + TotalOffTime
        hon, mon = tConvert(TotalOnTime,'m')
        hoff, moff  = tConvert(TotalOffTime,'m')
        print ('All in minutes = ', math.floor(TotalTime), '\nAll ON=',"%d:%02d" % (hon, mon),'\t All OFF=', "%d:%02d\n" % (hoff, moff))


if __name__=='__main__':
    main()
else:
    print(__name__)
