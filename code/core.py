import pickle
import numpy as np
import scipy.stats
from abc import ABCMeta, abstractmethod

class KeypressEventReceiver(object):
    '''A class that receives keypress events through a callback'''
    __metaclass__=ABCMeta
    KEY_DOWN, KEY_UP= 0, 1

    @abstractmethod
    def on_key(self, key, event_type, time_ms):
        '''key is a integer
        event_type is in (KEY_DOWN, KEY_UP)
        time_ms is the time when the key was (de/)pressed
        '''
        pass

class VersionedSerializableClass( object ):
    __metaclass__=ABCMeta
    FILE_EXTENSION=".pickle"
    CLASS_VERSION= -1

    def __init__(self, *args, **kwargs):
        self._class_version= self.CLASS_VERSION

    def save_to_file(self, filename):
        with open(filename+self.FILE_EXTENSION, 'wb') as f:
            self._serialize_to_file( f )

    @classmethod
    def load_from_file( cls, filename):
        import os
        if not os.path.exists(filename):
            filename+=cls.FILE_EXTENSION
        with open(filename, 'rb') as f:
            instance= cls._deserialize_from_file( f )

        load_error=None
        if not isinstance( instance, cls ):
            load_error= 'Unexpected instance type'
        elif instance._class_version!=cls.CLASS_VERSION:
            load_error= 'Class version mismatch (expected "{}", got "{}")'.format( cls.CLASS_VERSION, instance._class_version)
        if load_error:
            raise TypeError("Failed to load serialized data from {}: {}".format(filename, load_error))

        return instance

    @classmethod
    def load_from_dir( cls, directory ):
        import os
        d= directory
        filenames= [f for f in os.listdir(d) if f.endswith(cls.FILE_EXTENSION)]
        path_names= [os.path.join(d,f) for f in filenames]
        bare_names= [fn.rstrip(cls.FILE_EXTENSION) for fn in filenames] #without extension
        instances= map( cls.load_from_file, path_names)
        return dict(zip(bare_names, instances))

    def _serialize_to_file( self, f ):
        pickle.dump(self, f)

    @classmethod
    def _deserialize_from_file( cls, f ):
         return pickle.load(f)


class KeystrokeCaptureData(KeypressEventReceiver, VersionedSerializableClass):
    '''Recorded data of actual keystrokes pressed by a user'''
    FILE_EXTENSION=".keypresses"
    CLASS_VERSION= 0

    def __init__(self, existing_data=None):
        VersionedSerializableClass.__init__(self)
        self.log= list(existing_data) if existing_data else []

    def on_key(self, key, event_type, time_ms):
        '''Append a keypress event to this capture data'''
        self.log.append( (key, event_type, time_ms) )

    def feed(self, event_receiver):
        '''feeds this data into a KeypressEventReceiver.
        Returns the event_receiver'''
        for event in self.log:
            event_receiver.on_key( *event )
        return event_receiver

    def _serialize_to_file( self, f ):
        f.write( str(self.log) )

    @classmethod
    def _deserialize_from_file( self, f ):
        from ast import literal_eval
        data= literal_eval(f.read())
        return KeystrokeCaptureData(data)
