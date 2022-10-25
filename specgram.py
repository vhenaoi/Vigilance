import matplotlib.pyplot as plt
import mne
from scipy import signal as signal 
import numpy as np

raw = mne.io.read_epochs_eeglab(r'D:\Vigilance\Nold\EEGLab\Nold 6\vigilance 19ch\07 T7 interpolated.set',verbose='error')
amp = 2 * np.sqrt(2)
nM = 7
fs = raw.info['sfreq']

f,t,Zxx = signal.stft(raw._data[:100],fs,nperseg=1000)
plt.pcolormesh(t,f,np.abs(Zxx),vmin=0,vmax=amp)
Pxx,freqs,bins,im = plt.specgram(raw._data[:100],NFFT=512,Fs=fs)
plt.colorbar(im).set_label('Itensity(dB)')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')