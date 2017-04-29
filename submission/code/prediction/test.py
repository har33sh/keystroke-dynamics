import numpy as np
import pickle
from try1 import Features, Features2, Main

print("Enter same pattern.. Do not use BackSpace or anything.. After entering pattern : two ENTERs and CTrl-C");


# Load Preivous Object 
f = open('xx', 'r')   # 'r' for reading; can be omitted
x = pickle.load(f)         # load file content as mydict
f.close()
#print (x.list_final)


##Create Matrix
mat_p, mat_d, arr_p, arr_d = x.createMatrix();

## Get the TEST DATA.
y = Main();
y.get_keys();
y.kill_weed();
y.analysis()		
#x.printFeatures();
y.diff_bw_key_downs();
#x.printKeyDowns();

## Create matrix for the same test data
mat_np, mat_nd, arr_np, arr_nd = y.createMatrix();

"""
print(mat_p)
print(np.median(mat_p, axis=0));
print (np.std(mat_p, axis=0));

print (np.cov(mat_p));

print(np.asarray(np.median(mat_p, axis=0)));
print(np.asarray(np.median(mat_p, axis=0)));
"""
#print (np.random.multivariate_normal(np.squeeze(np.median(mat_p, axis=0)), np.cov(mat_p)));

### 
#
#	MEDIANS
#

m_ = []	#KEY_PRESS_DURATION
for i in np.asarray(np.median(mat_p, axis=0))[0]:
	m_.append(i);

m__ = []	## KEY_DIFF_DURATION

for i in np.asarray(np.median(mat_d, axis=0))[0]:
	m__.append(i);
	
	


print ("Checking Correlation : Numpy.Correlation :");
"""
print (np.correlate(np.squeeze(np.asarray(mat_p)), np.squeeze(np.asarray(mat_np))))
print (np.correlate(np.squeeze(np.asarray(mat_d)), np.squeeze(np.asarray(mat_nd))));
"""

"""
n = np.median(mat_p, axis=0);
print (n);





#m= n.flatten();
m = n.reshape(-1);
print (m);
#print (np.correlate(, arr_np));
#print (np.correlate(np.median(mat_p, axis=0).ravel(), arr_nd));
"""


print ("CHECKING CORRELATION in KEY_PRESS");
print (arr_np)
print(m_)
print (np.correlate(m_, arr_np));



print ("CHECKING CORRELATION in KEY_DIFFERENCE_PRESS");
print (arr_nd)
print(m__)
print (np.correlate(m__, arr_nd));


print ("Prediction and other types of correlations pending.... ")
