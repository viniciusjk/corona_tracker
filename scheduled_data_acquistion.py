import time
import data_acquisition

def scheduled_run():
    i=1
    print('Program Running \n\n\n')
    data_acquisition.main()
    print('Data acquistion #'+str(i)+' done.')

    while(True):
        i=i+1
        print('You can leave now\n')        
        time.sleep(10800)
        print('Program Running \n\n\n')
        data_acquisition.main()
        print('Data acquistion #'+str(i)+' done.')
        

if __name__=='__main__':
    scheduled_run()