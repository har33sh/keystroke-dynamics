import numpy as np
import pickle


## Class for having (Keystroke, DurationOfPress, Overlap) : example, 'A press', 'D press', 'A release'
class Features:
	
	def __init__(self, name, time_press, overlap):
		self.name = name;
		self.time_press= time_press;
		self.overlap = overlap;
		
	def __str__(self):
		return str([self.name, self.time_press, self.overlap]);



## Class for having (Key1, Key2, DifferenceInKeyDown)
class Features2:
	
	def __init__(self, name1, name2, time_press):
		self.name1 = name1;
		self.name2 = name2
		self.time_press= time_press;

		
	def __str__(self):
		return str([self.name1, self.name2, self.time_press]);

	def retList (self):
		
		return [self.name1, self.name2, self.time_press];


## Main class.
class Main:
	
	def __init__ (self):
		self.temp = [];			#	temp list and classes for getting and managing keystrokes. Some bugs here
		self.list_keys = [];	#
		self.list_final = [];	#	Final list of keys here. 
		self.list_analysis_object = []	# List of KEY_PRESS_DURATION
		
		self.list_diff_bw_keydowns = []; # List of KEY1_KEY2_DIFF
		
		
		
	def printFeatures (self):
		
		for i in self.list_analysis_object:
			print i;
			
	def printKeyDowns (self):
		
		for i in self.list_diff_bw_keydowns:
			print i;
		
	## Callback done in capture_keys file.
	def on_key(self, key, event_type, time_ms):
		self.temp.append( [key, event_type, time_ms] )
		
	#
	#	Capture Keys file is taken from github. Used for capturing keys using Xlib. requires python-xllib for working.
	#	Usage: start(callback)
	#
	def get_keys (self):
		try:
			import capture_keys
			capture_keys.start(self.on_key)
		except KeyboardInterrupt:
			pass
	
	#	This is for removing some issues in the cptured keys.
	##
	def kill_weed (self):
		new = []
		for i in range(0, len(self.temp)):
			
			if ( self.temp[i][0] == 36 ):
				self.list_keys.append(new);
				new = [];
			
			else:
				new.append(self.temp[i]);
				
		#self.list_keys.append(new);
		for i in range(0, len(self.list_keys)):
			
							
			if len(self.list_keys[i]) > 2:
				self.list_final.append( self.list_keys[i] )
			
		#print(self.list_keys);
		#print(self.list_final);
		
	
	#
	#	Get keypress duration.
	#
	def analysis (self):
		
		
		for k in range(0, len(self.list_final)):
			i =0;
			skipn = []
			while (i < (len(self.list_final[k]) - 1)):
			#for i in range (0, len(self.list_final[k]) - 1):
				# if first one and second one have same ID, substract to get time_press
				time_press = 0
				overlap = 0;
				
				if ( (self.list_final[k][i][0] == self.list_final[k][i+1][0]) and (self.list_final[k][i][1] != self.list_final[k][i+1][1]) ):
					
					#print("Continuous... " +  str(self.list_final[k][i][0]) + str(i));
					#print("Continuous... " +  str(self.list_final[k][i][0]) + str(i+1));
					time_press = self.list_final[k][i+1][2] - self.list_final[k][i][2];
					overlap = 0;
					
					#print (str(self.list_final[k][i][0]) , str(i), str(time_press), str(overlap));
					
					if ( i < len(self.list_final[k])):	
						analysis_obj = Features(self.list_final[k][i][0], time_press, overlap )
						self.list_analysis_object.append(analysis_obj);
						
					
					
					if ( i < (len(self.list_final[k]) - 1)):
						i = i+2;
					
				else:
					
					if i not in skipn:
						
						overlap = 1;
						
						## find the first occurence for it again.
						
						for j in range(i+1, len(self.list_final[k])):
							
							if ( self.list_final[k][j][0] == self.list_final[k][i][0] ):
								break;
						#print ("MAYBE OVERLAP: " +  str(self.list_final[k][i][0]) + str(i))
						#print ("Overlapped at : " +  str(self.list_final[k][i][0]) + str(j));
						skipn.append(j);
						
						time_press = self.list_final[k][j][2] - self.list_final[k][i][2];
						
						#print (str(self.list_final[k][i][0]) , str(i), str(time_press), str(overlap));
						
						if ( i < len(self.list_final[k])):	
							analysis_obj = Features(self.list_final[k][i][0], time_press, overlap )
							self.list_analysis_object.append(analysis_obj);
								
						
						i = i+1;
						
					else:
						
						#print("skipping..");
						i= i+1;
						
				"""if ( i < len(self.list_final[k])):	
					analysis_obj = Features(self.list_final[k][i][0], time_press, overlap )
					self.list_analysis_object.append(analysis_obj);"""
				
			
		print(self.list_diff_bw_keydowns)
		
		
	#
	#	Get differnce between Keypresses of two keys.
	#
	def diff_bw_key_downs (self):
		
		
		for k in range(0, len(self.list_final)):
			i =0;
			skipn = []
			while (i < (len(self.list_final[k]) - 1)):
			#for i in range (0, len(self.list_final[k]) - 1):
				# if first one and second one have same ID, substract to get time_press
				time_press = 0
				"""overlap = 0;
				
				if ( (self.list_final[k][i][0] == self.list_final[k][i+1][0]) and (self.list_final[k][i][1] != self.list_final[k][i+1][1]) ):
					
					print("Continuous... " +  str(self.list_final[k][i][0]) + str(i));
					print("Continuous... " +  str(self.list_final[k][i][0]) + str(i+1));
					time_press = self.list_final[k][i+1][2] - self.list_final[k][i][2];
					overlap = 0;
					
					print (str(self.list_final[k][i][0]) , str(i), str(time_press), str(overlap));
					
					if ( i < len(self.list_final[k])):	
						analysis_obj = Features(self.list_final[k][i][0], time_press, overlap )
						self.list_analysis_object.append(analysis_obj);
						
					
					
					if ( i < (len(self.list_final[k]) - 1)):
						i = i+2;
					
				else:"""
					
				if i not in skipn:
					
					#overlap = 1;
					
					## find the first occurence for it again.
					
					for j in range(i+1, len(self.list_final[k])):
						
						if ( (self.list_final[k][j][0] != self.list_final[k][i][0])  and (self.list_final[k][j][1] == self.list_final[k][i][1])):
							break;
					#print ("1st " +  str(self.list_final[k][i][0]) + str(i))
					#print ("2nd : " +  str(self.list_final[k][j][0]) + str(j));
					#skipn.append(j);
					
					time_press = self.list_final[k][j][2] - self.list_final[k][i][2];
					
					#print (str(self.list_final[k][i][0]), str(self.list_final[k][j][0]) , str(time_press), str(self.list_final[k][j][1]));
					
					if ( i < len(self.list_final[k]) and (self.list_final[k][j][1] == 0)):	
						analysis_obj = Features2( self.list_final[k][i][0], self.list_final[k][j][0],  time_press )
						self.list_diff_bw_keydowns.append(analysis_obj);
							
					
					i = i+1;
					
				else:
					
					#print("skipping..");
					i= i+1;
					
				"""if ( i < len(self.list_final[k])):	
					analysis_obj = Features(self.list_final[k][i][0], time_press, overlap )
					self.list_analysis_object.append(analysis_obj);"""
				
			
		#print(self.list_analysis_object)
			
			
	#
	#	This returns a matrix_key_press_curation, matrix_key_difference, arr_key_press_duration, arr_key_difference
	#
	def createMatrix (self):
		
		#get the length of innput:
		length = len(max(self.list_final, key=len));
		num = len(self.list_final);
		num = len(self.list_final);
		
		if (length % 2 == 0 ):
			length = length /2;
			print(length)
		else:
			length = length /2;
			print(length)
		
		#put it in matrix
		arr0 = []
		for i in self.list_analysis_object:
			arr0.append(i.time_press);
		
		arr00 = np.reshape(arr0, (num, length));
		mat_press = np.asmatrix(arr00);
		
		print (mat_press);
		
		arr1 = []
		for i in self.list_diff_bw_keydowns:
			arr1.append(i.time_press);
		
		arr11 = np.reshape(arr1, (num, length-1));
		mat_diff = np.asmatrix(arr11);
		
		print (mat_diff);
		
		
		return mat_press, mat_diff, arr0, arr1
		
	#
	#	Dumps object to file to pass it to test.py
	#
	def savePattern(self):
		
		f = open('xx', 'w')   # Pickle file is newly created where foo1.py is
		pickle.dump(self, f)          # dump data to f
		f.close()
		



		
		
if __name__ == "__main__":	
	print("Type any phrase.... Please press enter for entering 2nd phrase and two enters + ctrl-C to end it.");
	x = Main();
	x.get_keys();
	x.kill_weed();
	x.analysis()		
	#x.printFeatures();
	x.diff_bw_key_downs();
	#x.printKeyDowns();
	x.savePattern();
	
	#mat_p, mat_d = x.createMatrix();
	
	
	
	print("Pattern Learned. To Test,please run test.py");
	
	
