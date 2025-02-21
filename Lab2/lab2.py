import numpy as np
import matplotlib as plt
import scipy as sp
from pydub import AudioSegment
from pydub.playback import play

print("Hello world")

cantina = AudioSegment.from_wav("CantinaBand3.wav")

play(cantina)