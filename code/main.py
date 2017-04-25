import json
from core import KeystrokeCaptureData

conf = json.load(open("config.json"))

data_dir=conf['data_dir']
text_to_type=conf['text_to_type']


def get_some_keystrokes():
    print ("Please write the following text. When you're finished, press Ctrl-C")
    print ("------------------")
    print (text_to_type)
    data= KeystrokeCaptureData()
    try:
        import capture_keys
        capture_keys.start(data.on_key)
    except KeyboardInterrupt:
        pass
    print ("\n")
    return data


def create_fingerprint():
    username= input("What's your name? ")
    data= get_some_keystrokes()
    data.save_to_file( data_dir+username )
    fingerprint= create_fingerprint_from_capture_data( username, data )
    fingerprint.save_to_file( DATA_DIR+username )
    print ("Finished creating fingerprint!")


if __name__=='__main__':
    print ("Select a option:\n  1) Create Fingerprint\n  2) Predict User \n  3) Check for authenticity")

    try:
        option= int(input())
        print ("\n\n")
        if option==1:
            create_fingerprint()
        elif option==2:
            predict_user()
        elif option==3:
            check_auth()
        else:
            raise Exception("Invalid Option Choosen")

    except Exception as error:
        print ("Error " +str(error))
        exit()
