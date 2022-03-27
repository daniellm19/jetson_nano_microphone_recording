import noisereduce

temp = noisereduce.reduce_noise(noise_clip="noise_1sec_sample.wav",audio_clip="output13.wav",verbose=True)

signal, fs = librosa.load(path)
signln = len(signal)
avg_energy = np.sum(signal ** 2) / float(signln) #avg_energy of acual signal
f_d = 0.02 #frame duration
perc = 0.01

flag = True
j = 0
f_length = fs * f_d #frame length is `frame per second(fs) * frame_duration(f_d)` 
signln = len(signal)
retsig = []
noise = signal[0:441] # just considering first little part as noise
avg_energy = np.sum(signal ** 2) / float(signln)
while j < signln:
      subsig = signal[int(j): int(j) + int(f_length)]
      average_energy = np.sum(subsig ** 2) / float(len(subsig)) # avg energy of current frame
      if average_energy <= avg_energy: #if enegy of the current frame is less than actual signal then then we can confirm that this frame as silence or noise part
            if flag: #to get first noise or silence appearing on the signal 
                  noise = subsig #if you want to get all the noise frame, then just create a list and append it(noise_list.append(subsig)) and also don't use the flag condition
                  flag = False
            
      else: # if avg energy of current frame is grater than actual signal energy then this frame contain the data 
           retsig.append(subsig) # so you need to add that frame to new variable
      j += f_length