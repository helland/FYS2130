import numpy as np

class streng():
    
    def __init__(self, m, k, N, I, dt, y_minus, y_0):        
        self.y = np.zeros(N)     # current y-positions 
        self.m = np.zeros(N)     # point masses
        self.k = np.zeros((N)-1) # springs between points of mass
        self.dt = dt             # Time interval
        self.t = I*self.dt       # Total time of all iterations
        
        #Convert simple initial conditions to specified conditions if proper values have been assigned
        if (not isinstance(m, float)) and len(m) == len(self.m):            # if m is an array of numbers
            for i in range(0, len(self.m)): 
                self.m[i] = m[i]              
        elif isinstance(m, float):          # if m is a single value, assign it to all point masses
            for i in range(0, len(self.m)): 
                self.m[i] = m      
        if (not isinstance(k, float)) and len(k) == range(len(self.k)):     # if k is an array of numbers
            for i in range(0, len(self.k)): 
                self.k[i] = k[i]               
        elif isinstance(k, float):          # if k is a single value, assign it to all spring constants
            for i in range(0, len(self.k)): 
                self.k[i] = k               

        # initialize arrays for saving data for each point in time 
        if I > 1:                               
            self.y_history = np.zeros((I, N))   # Store all I iterations  for each point mass N
            self.y_history[0] = y_minus         # initial condition:  first y-positions (y_minus)                
            self.y_history[1] = y_0             # initial condition: second set of y-positions (y_zero)     
        else:                                   # If we don't know how many iterations we are going to run through
            self.y_history = np.array(y_minus)   # make room for the two initial conditions
            self.y_history = np.vstack((self.y_history, np.array(y_0)))
            

    # execute movement of point masses over time            
    def __call__(self, boundary, P, x):                
        i_max = len(self.y_history[0])-1            

        if boundary == True:                 # add weights M >> m at the ends if we want a bound string
            self.m[0] = 1000000000.0*self.m[0]
            self.m[len(self.m)-1] = 1000000000.0*self.m[len(self.m)-1]

        if P == 0:                           # if you have a predetermined number of iterations            
            # Find y values over time for all point masses
            for t in range(2,len(self.y_history)):      # N times, every dt time-interval (except the two initial conditions)                                
                #handle boundaries - at 0, force from the left = 0, at N-1, force from the right = 0        
                self.y_history[t][0] = (self.ForceRight(0,t-1)/self.m[0])*self.dt**2 + 2*self.y_history[t-1][i_max] - self.y_history[t-2][i_max]              
                self.y_history[t][i_max] = (self.ForceLeft(i_max,t-1)/self.m[len(self.m)-1])*self.dt**2 + 2*self.y_history[t-1][i_max] - self.y_history[t-2][i_max]              
                # non-boundary values
                for i in range(1, i_max):                       # For every point mass i find its y position   
                    self.y_history[t][i] = self.y_next(i, t-1)  # t-1 = y0 time interval, t = y+

        elif P != 0:      # if you want the string to move a certain number of periods P  [oppgave 5, P=10, x=99]
            t, periods = 2,0     
            # calculate new y-values until position x has passed its initial position P times                        
            while periods < P:                           
                # non-boundary values
                for i in range(1, i_max):             # For every point mass i find its y position   
                    self.y[i] = self.y_next(i, t-1)   # t-1 = y0 time interval, t = y+

                #handle boundaries - at 0, force from the left = 0, at N-1, force from the right = 0        
                self.y[0] = (self.ForceRight(0,t-1)/self.m[0])*self.dt**2 + 2*self.y_history[t-1][i_max] - self.y_history[t-2][i_max]              
                self.y[i_max] = (self.ForceLeft(i_max,t-1)/self.m[len(self.m)-1])*self.dt**2 + 2*self.y_history[t-1][i_max] - self.y_history[t-2][i_max]              
                # check if position x of the string has traveled a period (period++ if so)
                if (self.y[x] <= self.y_history[0][x] and self.y[x-1] >= self.y_history[0][x]) or (self.y[x] >= self.y_history[0][x] and self.y[x-1] <= self.y_history[0][x]):    
                    periods = periods +1                                                      
                self.y_history = np.vstack((self.y_history, np.array(self.y))) 
                t = t+1
            self.t = (t+2)*self.dt                        # Store the total time the string has been in motion
    
    
    # returns y-position in the next time interval y+_i
    def y_next(self, i,t):
        return (self.Force(i,t)/self.m[i])*self.dt**2 + 2*self.y_history[t][i] - self.y_history[t-1][i]

    #returns Force from the left spring
    def ForceLeft(self, i, t):  #where t is the current time interval we're dealing with and i is position along the string
        return -self.k[i-1]*(self.y_history[t][i]-self.y_history[t][i-1])
                                
    #returns force from the right spring    
    def ForceRight(self, i, t):     #where t is the current time interval we're dealing with and i is position along the string
        return -self.k[i]*(self.y_history[t][i]-self.y_history[t][i+1])
         
    #returns total force from springs
    def Force(self,i,t):
        return (self.ForceRight(i, t) + self.ForceLeft(i, t)) 








