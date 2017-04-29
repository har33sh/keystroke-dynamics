#!/usr/bin/python
from scipy.stats import norm
from numpy import mean,std
from abc import ABCMeta, abstractmethod
import pickle

#Serialization object to load and store the objects
class Serialization( object ):
    __metaclass__=ABCMeta
    FILE_TYPE=".pickle"
    ID= -1

    def __init__(self, *args, **kwargs):
        self._id= self.ID

    def save_file(self, filename):
        f= open(filename+self.FILE_TYPE, 'wb')
        pickle.dump( self, f)
        f.close()

    @classmethod
    def load_file( cls, filename):
        try:
            f= open(filename, 'rb')
        except Exception:
            f=open(filename+cls.FILE_TYPE, 'rb')
        pickle_file= pickle.load(f)
        f.close()
        return pickle_file



#defing KeyUp and KeyDown if we need to add UpDown, DownDown, Hold etc, it can be modified here
class KeypressEventReceiver(object):
    __metaclass__=ABCMeta
    KEY_DOWN, KEY_UP= 0, 1

    @abstractmethod
    def on_key(self, key, event_type, time_ms):
        pass


#To get the features from the given key presses, this also needs the the help of KeypressEventReceiver
class TimingExtractor(KeypressEventReceiver):
    def __init__(self, timing_threshold=500):
        self.pt=0
        self.pk=0
        self.press_time={}
        self.timing_threshold= timing_threshold
        self.dwell_times=[[] for i in range(256)]
        self.flight_times_before=[[] for i in range(256)]
        self.flight_times_after=[[] for i in range(256)]


    def on_key(self, key, type, time):
        if type==self.KEY_DOWN:
            flight_time= time - self.pt
            if flight_time<self.timing_threshold:
                self.flight_times_before[key].append(flight_time)
                self.flight_times_after[self.pk].append(flight_time)
            self.press_time[key]=time
            self.pt=time
            self.pk=key

        if type==self.KEY_UP:
            try:
                dwell_time= time - self.press_time.pop(key)
            except KeyError:
                return
            if dwell_time<self.timing_threshold:
                self.dwell_times[key].append(dwell_time)



#Recorded data of actual keystrokes pressed by a user
class KeystrokeCaptureData(KeypressEventReceiver, Serialization):
    FILE_TYPE=".keypresses"
    ID= 0

    def __init__(self):
        super(KeypressEventReceiver, self).__init__()
        self.log= []

    #append all the keypress to the log
    def on_key(self, key, event_type, time_ms):
        self.log.append( (key, event_type, time_ms) )

    #Data is given to the KeypressEventReceiver
    def feed(self, event_receiver):
        for event in self.log:
            event_receiver.on_key( *event )
        return event_receiver


#Perform ML algorithms and get somthing out here
class Signature(Serialization):
    FILE_TYPE=".sign"
    ID= 0
    def __init__(self, data):
        super(Signature, self).__init__()
        self.data= data

    @staticmethod
    def create(keystroke_capture_data, sample_number_threshold=4, std_dev_threshold=-1):
        snt, sdt= sample_number_threshold, std_dev_threshold
        times= keystroke_capture_data.feed( TimingExtractor() ).dwell_times
        data={}
        for key,key_times in enumerate(times):
            if(mean(key_times) >0 ):
                data[key]= (mean(key_times), std(key_times) )
        return Signature(data)

    def similarity( self, other_fingerprint ):
        def feature_similarity(f1, f2):
            stddev= f1[1]
            difference= abs(f1[0]-f2[0])
            return norm.cdf(-difference/stddev)
        sign1, sign2= self.data, other_fingerprint.data
        score=1
        common_features= set(sign1.keys()) & set(sign2.keys())
        for feature in common_features:
            f1,f2= sign1[feature], sign2[feature]
            probability= feature_similarity( f1, f2 )
            if probability!=0 :
                score += 2*probability
            else:
                score += 2 *000001
            print 'analising key %d, mean: %f, stddev: %f, given mean: %f, probability %f'% (feature,f1[0],f1[1], f2[0], probability)
        return score
