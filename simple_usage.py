from time import process_time
  
n = 150
  
t1_start = process_time() 
   
for i in range(n):
    print( i+1*n/1+n , end =' ')
  
print() 
  
t1_stop = process_time()
   
print("Elapsed time:", t1_stop, t1_start) 
   
print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start)