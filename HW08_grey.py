# import relevant packages
import os
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

bp_low = 0.5
bp_upp = 6
electrode_num = 16
electrode_name_ls = ['F3', 'Fz', 'F4', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP3', 'CP4', 'P3', 'Pz', 'P4', 'PO7', 'PO8', 'Oz']

parent_dir = os.getcwd()
parent_data_dir = '{}/data'.format(parent_dir)
time_index = np.linspace(0, 800, 25) # This is a hypothetic time range up to 800 ms after each stimulus.

subject_name = 'K114'
session_name = '001_BCI_TRN'

if os.path.exists("{}/subject_name".format(parent_dir)):
    pass
else:
    os.mkdir("{}/subject_name".format(parent_dir))

file_mat = "./data/K114_001_BCI_TRN_Truncated_Data_0.5_6.mat"
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

### function produce_trun_mean_cov
def produce_trun_mean_cov(input_signal, input_type, E_val):
    len01 = input_signal.shape[1]
    len02 = len01 // E_val

    signal_t = input_signal[input_type == 1, :]
    signal_nt = input_signal[input_type == -1, :]

    signal_t_mean = np.zeros((E_val, len02))
    signal_nt_mean = np.zeros((E_val, len02))
    signal_t_cov = np.zeros((E_val, len02, len02))
    signal_nt_cov = np.zeros((E_val, len02, len02))
    signal_cov = np.zeros((E_val, len02, len02))

    for i in range(E_val):
        s = i * len02
        e = (i + 1) * len02

        t_electrode = signal_t[:, s:e]
        nt_electrode = signal_nt[:, s:e]
        electrode = input_signal[:, s:e]

        signal_t_mean[i, :] = np.mean(t_electrode, axis=0)
        signal_nt_mean[i, :] = np.mean(nt_electrode, axis=0)

        signal_t_cov[i, :, :] = np.cov(t_electrode.T)
        signal_nt_cov[i, :, :] = np.cov(nt_electrode.T)
        signal_cov[i, :, :] = np.cov(electrode.T)

    return [signal_t_mean, signal_nt_mean, signal_t_cov, signal_nt_cov, signal_cov]

### function plot_trunc_mean
def plot_trunc_mean(
        eeg_tar_mean, eeg_ntar_mean, subject_name, time_index, E_val, electrode_name_ls,
        y_limit=np.array([-5, 8]), fig_size=(12, 12)
):
    fig, axes = plt.subplots(4, 4, figsize=fig_size)

    fig.suptitle(f'Subject: {subject_name} - Mean ERP Signals')

    for i in range(E_val):
        r = i // 4
        c = i % 4

        ax = axes[r, c]

        ax.plot(time_index, eeg_tar_mean[i, :],
                'r-',
                label='Target',
                linewidth=2)

        ax.plot(time_index, eeg_ntar_mean[i, :],
                'b-',
                label='Non-Target',
                linewidth=2)

        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Amplitude (muV)')
        ax.set_title(electrode_name_ls[i])
        ax.set_ylim(y_limit)
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

### function plot_trunc_cov
def plot_trunc_cov(
        eeg_cov, cov_type, time_index, subject_name, E_val, electrode_name_ls, fig_size=(14, 12)
):
    fig, axes = plt.subplots(4, 4, figsize=fig_size)

    fig.suptitle(f'Subject: {subject_name} - {cov_type} Covariance')

    X, Y = np.meshgrid(time_index, time_index)

    for i in range(E_val):
        r = i // 4
        c = i % 4
        ax = axes[r, c]

        cont = ax.contourf(X, Y, eeg_cov[i, :, :],
                           levels=20,
                           cmap='viridis')

        ax.invert_yaxis()

        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Time (ms)')
        ax.set_title(electrode_name_ls[i])

        plt.colorbar(cont, ax=ax)

    plt.tight_layout()
    plt.show()

#May cause an error
results = produce_trun_mean_cov(eeg_trunc_signal, eeg_trunc_type, electrode_num)

signal_tar_mean, signal_ntar_mean, signal_tar_cov, signal_ntar_cov, signal_all_cov = results


# Write your own code: (only call plot_trunc_mean in this code section)
plot_trunc_mean(
    signal_tar_mean,
    signal_ntar_mean,
    subject_name,
    time_index,
    electrode_num,
    electrode_name_ls
)

# Write your own code: call plot_trunc_cov for target covariance only
plot_trunc_cov(
    signal_tar_cov,
    'Target',
    time_index,
    subject_name,
    electrode_num,
    electrode_name_ls
)

# Write your own code: call plot_trunc_cov for non-target covariance only
plot_trunc_cov(
    signal_ntar_cov,
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



