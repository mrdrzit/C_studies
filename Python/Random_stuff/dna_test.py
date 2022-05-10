# DNA  = A, G, T, C
# RNA  = A, G, U, C
# PROT = A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y

# ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN

# TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT

# ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN


s1 = 'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN'
s2 = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
s3 = 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN'



a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

dna  = ['A', 'G', 'T','C']
rna  = ['A', 'G', 'U','C']
prot = ['A', 'C', 'D','E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']


# is dna if sequence has only AGTC

def isdna_or_prot(sequence):
  return [True if x == 'b' else False for x in sequence]

def isrna(sequence):
  return [True if x == 'b' else False for x in sequence]

t = []
for nt in range (0, len(rna)):
  if dna[nt] == rna[nt]:
    t.append(True)
  else:
    t.append(False)


pdna = False
pprot = False
prna = False

for x in s1:
  if x == 'U':
    prna = True
  elif x == 'E':
    pprot == True
  else:
    pdna == True

