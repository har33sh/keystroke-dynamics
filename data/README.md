
# Data

## Collection :

    We built a keystroke data-collection apparatus consisting of: (1) a laptop running Windows XP; (2) a software application for presenting stimuli to the subjects, and for recording their keystrokes; and (3) an external reference timer for timestamping those keystrokes. The software presents the subject with the password to be typed.

    As the subject types the password, it is checked for correctness. If the subject makes a typographical error, the application prompts the subject to retype the password. In this manner, we record timestamps for 50 correctly typed passwords in each session.

    Whenever the subject presses or releases a key, the software application records the event (i.e., keydown or keyup), the name of the key involved, and a timestamp for the moment at which the keystroke event occurred.

    An external reference clock was used to generate highly accurate timestamps. The reference clock was demonstrated to be accurate to within ±200 microseconds (by using a function generator to simulate key presses at fixed intervals).


    We recruited 51 subjects (typists) from within a university community; all subjects fully completed the study—we did not drop any subjects. All subjects typed the same password, and each subject typed the password 400 times over 8 sessions (50 repetitions per session). They waited at least one day between sessions, to capture some of the day-to-day variation of each subject's typing. The password (.tie5Roanl) was chosen to be representative of a strong 10-character password.


## Description
    The raw records of all the subjects' keystrokes and timestamps were analyzed to create a password-timing table. The password-timing table encodes the timing features for each of the 400 passwords that each subject typed.

    The data are arranged as a table with 34 columns. Each row of data corresponds to the timing information for a single repetition of the password by a single subject.

    The first column, subject, is a unique identifier for each subject (e.g., s002 or s057). Even though the data set contains 51 subjects, the identifiers do not range from s001 to s051; subjects have been assigned unique IDs across a range of keystroke experiments, and not every subject participated in every experiment. For instance, Subject 1 did not perform the password typing task and so s001 does not appear in the data set.

    The second column, sessionIndex, is the session in which the password was typed (ranging from 1 to 8).

    The third column, rep, is the repetition of the password within the session (ranging from 1 to 50).

    The remaining 31 columns present the timing information for the password. The name of the column encodes the type of timing information. Column names of the form H.key designate a hold time for the named key (i.e., the time from when key was pressed to when it was released). Column names of the form DD.key1.key2 designate a keydown-keydown time for the named digraph (i.e., the time from when key1 was pressed to when key2 was pressed). Column names of the form UD.key1.key2 designate a keyup-keydown time for the named digraph (i.e., the time from when key1 was released to when key2 was pressed). Note that UD times can be negative, and that H times and UD times add up to DD times.

    Consider the following one-line example of what you will see in the data:

      subject  sessionIndex  rep      H.period   DD.period.t   UD.period.t     ...
         s002             1    1        0.1491        0.3979        0.2488     ...

    The example presents typing data for subject 2, session 1, repetition 1. The period key was held down for 0.1491 seconds (149.1 milliseconds); the time between pressing the period key and the t key (keydown-keydown time) was 0.3979 seconds; the time between releasing the period and pressing the t key (keyup-keydown time) was 0.2488 seconds; and so on.
