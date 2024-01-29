import wave
import numpy as np

def text2id(str,dict):
    ls = []
    for i in str:
        if i == ' ':
            ls.append(dict['|'])
        else:
            ls.append(dict[i])
    return ls

def wav_read(wav_path):
    with wave.open(wav_path, 'rb') as f:
        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[0:4]
        strdata = f.readframes(nframes)
        data = np.frombuffer(strdata, dtype=np.int16)
        data = data / 32768
    return data

def wav_write(wav_path,data):
    nchannels=1
    sampwidth=2
    framerate=16000
    nframes=len(data)
    comptype='NONE'
    compname='not compressed'
    with wave.open(wav_path, 'wb') as fw:
        fw.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
        data=(data*32768).astype(np.int16)
        fw.writeframes(data.tobytes())

def SNR_singlech(clean, adv):
    length = min(len(clean), len(adv))
    est_noise = adv[:length] - clean[:length]
    SNR = 10*np.log10((np.sum(clean**2))/(np.sum(est_noise**2)))
    return SNR