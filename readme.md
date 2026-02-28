
# Finding the n and o values

In the moving Window analysis technique, we used to include Supernovae from the preceding bin and the succeeding bin. Then, finding the possible combinations of overlap (o), and number of Supernovae in each bin (n), keeping the bin equipopulated is the only way to do it properly,

The equation to do is,

$$ o = \frac{((n * N) - T)}{(N -1)}$$

Where, 

o --> Overlap 

n --> number of SNe in each bin (We assume a possible value) 

T --> Total number of Supernovae in the sample 

N --> Number of bins 

If we do it manually, we need the answer to be an integer, and even if we get one combination, we should try other combinations if the current one doesn't generate a better result. (Decreasing trend) 

So, to compute it manually, only with the possible integer combination of 'o' and 'n'. Here I created a code to do it.

  

# Bin seperation

Even if we choose a combinations of 'n' and 'o', it is hard to accommodate them in each bin equipopulated manually. I created another code that give you the start and end values of the number of SNe in all the bins for the given 'n' and 'o' value.

It is did using the equation,

$$x_i = (y_i + 1) + o , \ \ \ \ \ \ \ \ \text{where}, \ x_1 = 1 \ \text{, and i = 2,....N}$$

$$y_i = (x_i - 1) + n , \ \ \ \ \ \ \ \ \text{where}, \ y_1 = n \ \text{, and i = 1,....N}$$

N = number of bins 

n = Total no. of SNe 

o = Overlap 

Example: 

If we have 1829 supernovae (T = 1829) in a sample and we need to equipopulate in 3 bin (N = 3) to do the moving window. Using the code, we find the possible n and o values. So we have the following value, 

T = 1829 

N = 3 

n = 649 

o = 59 

Then,

the possible bin ranges  using the equations are, 

Bin 1: (1-649) 

Bin 2: (591-1239) 

Bin 3: (1181-1829) 
