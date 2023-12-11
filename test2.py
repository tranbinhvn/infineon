import numpy as np
import matplotlib.pyplot as plt

def cfar_ca1D_square(Xcube, noiseWin, guardLen, Pfa, wrapMode, ord_stat):
    N = noiseWin * 2
    alpha = N * (Pfa ** (-1/N) - 1)
    alpha_oneside = noiseWin * (Pfa ** (-1/noiseWin) - 1)
    Xcube = Xcube ** 2
    Xlength = len(Xcube)
    Detect = []
    numOfDet = 0

    if wrapMode == 0:
        for i in range(1, Xlength + 1):
            if i < noiseWin + guardLen + 1:
                Xcube_select = np.sort(Xcube[i + guardLen:i + guardLen + noiseWin])[::-1]
                num_filter = round(len(Xcube_select) * (1 - ord_stat))
                noiseWin_len = noiseWin - num_filter
                if num_filter > 0:
                    Xcube_select[:num_filter] = 0
                noise_estimate = np.sum(Xcube_select) / noiseWin_len
                if Xcube[i - 1] > alpha_oneside * noise_estimate:
                    numOfDet += 1
                    Detect.append([i, Xcube[i - 1], noise_estimate])
            elif i < Xlength - noiseWin - guardLen + 1:
                Xcube_select = np.sort(Xcube[i + guardLen:i + guardLen + noiseWin])[::-1]
                Xcube_select2 = np.sort(Xcube[i - guardLen - noiseWin:i - guardLen - 1])[::-1]
                num_filter = round(len(Xcube_select) * (1 - ord_stat))
                noiseWin_len = noiseWin - num_filter
                if num_filter > 0:
                    Xcube_select[:num_filter] = 0
                    Xcube_select2[:num_filter] = 0
                noise_estimate = (np.sum(Xcube_select) + np.sum(Xcube_select2)) / (2 * noiseWin_len)
                if Xcube[i - 1] > alpha * noise_estimate:
                    numOfDet += 1
                    Detect.append([i, Xcube[i - 1], noise_estimate])
            else:
                Xcube_select = np.sort(Xcube[i - guardLen - noiseWin:i - guardLen - 1])[::-1]
                num_filter = round(len(Xcube_select) * (1 - ord_stat))
                noiseWin_len = noiseWin - num_filter
                if num_filter > 0:
                    Xcube_select[:num_filter] = 0
                noise_estimate = np.sum(Xcube_select) / noiseWin_len
                if Xcube[i - 1] > alpha_oneside * noise_estimate:
                    numOfDet += 1
                    Detect.append([i, Xcube[i - 1], noise_estimate])
    else:
        for i in range(1, Xlength + 1):
            if i < noiseWin + guardLen + 1:
                if i <= guardLen:
                    noise_estimate = (np.sum(Xcube[i + guardLen:i + guardLen + noiseWin]) +
                                      np.sum(Xcube[Xlength + i - guardLen - noiseWin:Xlength + i - guardLen - 1])) / N
                else:
                    noise_estimate = (np.sum(Xcube[i + guardLen:i + guardLen + noiseWin]) +
                                      np.sum(Xcube[Xlength + i - guardLen - noiseWin:Xlength]) +
                                      np.sum(Xcube[:i - 1 - guardLen])) / N

                if Xcube[i - 1] > alpha * noise_estimate:
                    numOfDet += 1
                    Detect.append([i, Xcube[i - 1], noise_estimate])

            elif i < Xlength - noiseWin - guardLen + 1:
                noise_estimate = (np.sum(Xcube[i + guardLen:i + guardLen + noiseWin]) +
                                  np.sum(Xcube[i - guardLen - noiseWin:i - guardLen - 1])) / N

                if Xcube[i - 1] > alpha * noise_estimate:
                    numOfDet += 1
                    Detect.append([i, Xcube[i - 1], noise_estimate])

            else:
                if i >= Xlength - guardLen + 1:
                    noise_estimate = (np.sum(Xcube[i - guardLen - noiseWin:i - guardLen - 1]) +
                                      np.sum(Xcube[guardLen + i - Xlength + 1:guardLen + i - Xlength + noiseWin])) / N
                else:
                    noise_estimate = (np.sum(Xcube[i - guardLen - noiseWin:i - guardLen - 1]) +
                                      np.sum(Xcube[guardLen + i + 1:Xlength]) +
                                      np.sum(Xcube[:noiseWin - Xlength + i + guardLen])) / N

                if Xcube[i - 1] > alpha * noise_estimate:
                    numOfDet += 1
                    Detect.append([i, Xcube[i - 1], noise_estimate])

    return np.array(Detect)

def generate_example_data():
    # Generate example data (simulated radar signal)
    np.random.seed(42)
    signal_length = 200
    signal = np.zeros(signal_length)
    signal[50:80] = 5  # Add a signal between indices 50 and 80

    # Add Gaussian noise to the signal
    noise = np.random.normal(0, 1, signal_length)
    noisy_signal = signal + noise

    return noisy_signal

def main():
    # Generate example data
    noisy_signal = generate_example_data()

    # Set parameters for CFAR algorithm
    noise_win = 10
    guard_len = 5
    pfa = 0.01
    wrap_mode = 0
    ord_stat = 0.7

    # Apply CFAR algorithm
    detections = cfar_ca1D_square(noisy_signal, noise_win, guard_len, pfa, wrap_mode, ord_stat)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(noisy_signal, label='Noisy Signal')
    plt.scatter(detections[0], detections[1], color='red', marker='x', label='Detections')
    plt.title('CFAR Detection Results')
    plt.xlabel('Index')
    plt.ylabel('Signal Power')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
