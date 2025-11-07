# import relevant packages
import os
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

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