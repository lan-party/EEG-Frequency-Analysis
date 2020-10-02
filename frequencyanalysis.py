import numpy as np
import matplotlib.pyplot as p
import wave as wave


filename = "OpenBCI-RAW-2020-10-01_12-54-26.txt"

filedata = open(filename, "r").read().splitlines()

nodes = np.array([np.array([float(a) for a in filedata[6].split(", ")[1:9]])])
print(nodes)

samplerate = 250

for a in range(7, len(filedata)-1):
    nodes = np.append(nodes, np.array([np.array([float(b) for b in filedata[a].split(", ")[1:9]])]), axis=0)
nodes = nodes.T

for a in range(0, len(nodes)):
    node = nodes[a]
    nodet = np.arange(0, len(node)/samplerate, len(node)/samplerate/len(node))

    f, (plt1, plt2, plt3) = p.subplots(3, 1)
    plt1.plot(nodet,node)
    plt1.set_xlabel('Time (s)')
    plt1.set_ylabel('Amplitude (Hz)')

    Pxx, freqs = plt2.psd(node,NFFT=2048,Fs=samplerate)

    Pxx, freqs, bins, im = plt3.specgram(node,NFFT=256, Fs=samplerate)
    plt3.set_xlabel('Time')
    plt3.set_ylabel('Frequency')

    p.gcf().set_size_inches(10, 10)
    p.savefig("node"+str(a)+".png", dpi=(300))
    print("node"+str(a)+".png created.")
