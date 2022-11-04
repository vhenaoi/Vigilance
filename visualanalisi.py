#Open raw and visual signal

import mne

path_raw = r"C:\Users\veroh\Downloads\Nold 11 Vigilance 61 ch.edf"
raw = mne.io.read_raw(path_raw,preload=True)