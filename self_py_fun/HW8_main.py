import os
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

#import functions
from HW8Fun import *

bp_low = 0.5
bp_upp = 6
electrode_num = 16
electrode_name_ls = ['F3', 'Fz', 'F4', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP3', 'CP4', 'P3', 'Pz', 'P4', 'PO7', 'PO8', 'Oz']

parent_dir = os.getcwd()
parent_data_dir = '{}/data'.format(parent_dir)
time_index = np.linspace(0, 800, 25)

subject_name = 'K114'
session_name = '001_BCI_TRN'

if os.path.exists("{}/subject_name".format(parent_dir)):
    pass
else:
    os.mkdir("{}/subject_name".format(parent_dir))

file_mat = f"{parent_data_dir}/{subject_name}_{session_name}_Truncated_Data_{bp_low}_{bp_upp}.mat"

eeg_trunc_obj = sio.loadmat(file_mat)

print("Keys:")
print(eeg_trunc_obj.keys())

eeg_trunc_signal = eeg_trunc_obj["Signal"]
eeg_trunc_type = eeg_trunc_obj["Type"]

print("Signal Shape:")
print(eeg_trunc_signal.shape)
print("Type Shape:")
print(eeg_trunc_type.shape)

eeg_trunc_type = np.squeeze(eeg_trunc_type, axis=1)
print(eeg_trunc_type)

print(eeg_trunc_type.shape)

print("Total Stimuli:")
print(len(eeg_trunc_type))


plot_trunc_mean(
    signal_t_mean,
    signal_nt_mean,
    subject_name,
    time_index,
    electrode_num,
    electrode_name_ls
)

# Write your own code: call plot_trunc_cov for non-target covariance only
plot_trunc_cov(
    signal_nt_cov,
    'Non-Target',
    time_index,
    subject_name,
    electrode_num,
    electrode_name_ls
)

# Write your own code: call plot_trunc_cov for all covariance only
plot_trunc_cov(
    signal_all_cov,
    'All',
    time_index,
    subject_name,
    electrode_num,
    electrode_name_ls
)

print(f"Done. Figures saved under ./{subject_name}/ :")
print(" - Mean.png")
print(" - Covariance_Target.png")
print(" - Covariance_Non-Target.png")
print(" - Covariance_All.png")
