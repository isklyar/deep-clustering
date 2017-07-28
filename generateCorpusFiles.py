input = open('/u/sklyar/master-thesis/deep-clustering/createMix/create-speaker-mixtures/mix_2_spk_tt.txt','r')

output = open('test\_list.txt','w')
for line in input:
    list = line.split()

    seq = '/work/asr2/sklyar/corpora/' + list[0] + ' ' +  list[0][5:8], '\n', '/work/asr2/sklyar/corpora/' + list[2] + ' ' + list[2][5:8], '\n'
    output.writelines(seq)
    #print list[0][5:8]
