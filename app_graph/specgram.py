import matplotlib.pyplot as plt
import mne
from scipy import signal as signal 
import numpy as np

raw = mne.io.read_raw_eeglab(r'D:\Veronica\Data\01_NOLD\Vertex\Nold11\Vertex Nold11 256.set',verbose='error')
raw.plot_psd_topomap()
amp = 2 * np.sqrt(2)
nM = 7
fs = raw.info['sfreq']

eeg= raw[:]
eeg[0][16]
f,t,Zxx = signal.stft(eeg[1],fs,nperseg=256)
plt.pcolormesh(t,f,np.abs(Zxx),vmin=0,vmax=amp)
Pxx,freqs,bins,im = plt.specgram(eeg[1],NFFT=512,Fs=fs)
plt.colorbar(im).set_label('Itensity(dB)')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')