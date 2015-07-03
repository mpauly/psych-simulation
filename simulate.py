import numpy as np

NR_PER_CONDITION = 1000

neuro_sigma = 4
neuro_mean = 0

satis_sigma = 4
satis_mean = 0



print "Start drawing"

bins = {
    5: np.array([-6, -3, 0, 3, 6]),
    7: np.array([-6, -4, -2, 0, 2, 4, 6])
}


borders = {
    5: np.array([-4.5,-1.5,1.5,4.5]),
    7: np.array([-5.,-3.,-1.,1,3,5])
}
'output.dat'
conditions = [
    {'cond': 1, 'first': 5, 'second': 5},
    {'cond': 2, 'first': 7, 'second': 7},
    {'cond': 3, 'first': 5, 'second': 7},
    {'cond': 4, 'first': 7, 'second': 5}
]

neuro_vals = np.empty([12,NR_PER_CONDITION])
satis_vals = np.empty([12,NR_PER_CONDITION])

outfile = file('output.dat', 'w')
outfile.write('cond')
for i in range(12):
	outfile.write('\tneuro'+str(i+1))
for i in range(12):
	outfile.write('\tsatis'+str(i+1))
outfile.write('\n')

for cond in conditions:
    print "Writing condition ", cond['cond']
    for i in range(12):
        neuro = neuro_sigma * np.random.randn(NR_PER_CONDITION) + neuro_mean
        neuro_index = np.digitize(neuro, borders[cond['first']])
        neuro_vals[i] = bins[cond['first']][neuro_index]

        satis = satis_sigma * np.random.randn(NR_PER_CONDITION) + satis_mean
        satis_index = np.digitize(satis, borders[cond['second']])
        satis_vals[i] = bins[cond['second']][satis_index]

    cond_arr = np.full([1,NR_PER_CONDITION], cond['cond'])
    output = np.concatenate((cond_arr, neuro_vals, satis_vals) )

    np.savetxt(outfile, output.transpose(), fmt="%2i")

outfile.close()
print "Finished"
