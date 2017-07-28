f1 = open('/u/sklyar/Dropbox/Thesis/create-speaker-mixtures/mix_2_spk_tr.txt','r')
f2 = open('/u/sklyar/Dropbox/Thesis/create-speaker-mixtures/mix_2_spk_tt.txt','r')
f3 = open('/u/sklyar/Dropbox/Thesis/create-speaker-mixtures/mix_2_spk_cv.txt','r')

output = open('new-filenames.txt','w')
for line in f1:
    list = line.split()
    seq = '/u/corpora/speech/wsj/audio' + list[0][4:len(list[0])-3] + 'sph', '\n', '/u/corpora/speech/wsj/audio' + list[2][4:len(list[0])-3] + 'sph', '\n'
    output.writelines(seq)
for line in f2:
    list = line.split()
    seq = '/u/corpora/speech/wsj/audio' + list[0][4:len(list[0])-3] + 'sph', '\n', '/u/corpora/speech/wsj/audio' + list[2][4:len(list[0])-3] + 'sph', '\n'
    output.writelines(seq)
for line in f3:
    list = line.split()
    seq = '/u/corpora/speech/wsj/audio' + list[0][4:len(list[0])-3] + 'sph', '\n', '/u/corpora/speech/wsj/audio' + list[2][4:len(list[0])-3] + 'sph', '\n'
    output.writelines(seq)

