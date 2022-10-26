#Open raw and visual signal

import mne

path_raw = r'D:\Veronica\Data\01_NOLD\Nold 6\HealthyControl019.vhdr'
raw = mne.io.read_raw_brainvision(path_raw,preload=True)