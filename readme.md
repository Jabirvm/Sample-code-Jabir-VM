Finding the n and o values
 
 In the moving Window analysis technique, we used to include Supernovae from the preceding bin and the succeeding bin. Then, finding the possible combinations of overlap (o), and number of Supernovae in each bin (n), keeping the bin equipopulated is the only way to do it properly, 
 The equation to do is, 
 
 $$ o = \frac{((n * N) - T)}{(N -1)}$$
 
 Where, 
 o --> Overlap
 n --> number of SNe in each bin  (We assume a possible value)
 T --> Total number of Supernovae in the sample
 N --> Number of bins
 
 If we do it manually, we need the answer to be an integer, and even if we get one combination, we should try other combinations if the current one doesn't generate a better result. (Decreasing trend)
 So, to compute it manually, only with the possible integer combination of 'o' and 'n'. Here I created a code to do it.