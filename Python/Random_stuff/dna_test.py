def what_is(sequence):
  lastindex = 0 # Marcando o indice pra poder usar como referencia de final

# ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN

  # Aqui eu pego a lista inteira e faço uma checagem direta pra ver se tem alguma
  # letra inválida e, se tiver, já para o loop principal e fala que não é uma sequência válida
  if [item for item in sequence if item not in prot and item not in rna]:
    # Basicamente: "grave o item da sequência dada se o item não estiver na lista das proteinas e não 
    # estiver na lista do RNA"
    print("It's nothing")
    return

  # Agora como já fizemos um check geral pra ver se não tem letras inválidas podemos fazer
  # checagens mais simples:

  for nt in sequence:
    lastindex +=1
    # Só o RNA tem a uracila, então a gente checa pra ver se o nucleotídeo atual é um U
    # Se sim então podemos parar e avisar que é uma sequência de RNA
    if nt == 'U': 
      print("It's an RNA")
      break

    # Aqui eu eu checo o nucleotídeo atual com a lista protein_negation
    # Se tiver incluída nessa lista então só pode ser uma proteína
    elif nt in protein_negation:
      print("It's a protein")
      break

    # Se chegou no último índice da lista e não nenhum dos acima
    # então só pode ser uma sequência de DNA
    elif lastindex == len(sequence):
      print("It's a DNA")
      pass

# Sequencias dadas pela professora
s1 = 'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN'
s2 = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
s3 = 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN'

# Sequencias de dna que eu gerei aleatóriamente na internet pra testar: 
# https://www.bioinformatics.org/sms2/random_dna.html
# https://molbiotools.com/randomsequencegenerator.php
s4 = 'ACTGGCGCCGAACTTTGGAAACGTGAGGGTTCGGAGAAGA'
s5 = 'TTGAAACCGGAGTCATAACAGGAACGTCGCTTACTGATTA'

# Sequencias de proteinas que eu gerei aleatóriamente na internet pra testar:
# https://www.bioinformatics.org/sms2/random_dna.html
# https://molbiotools.com/randomsequencegenerator.ph
s6 = 'LNEKGILQYPQRYTEGFPWNPKNTYDFCMCPGITPRAYCT'
s7 = 'MRVPFLMKLWCRPGWQAQPVNDYSQCRMRKSRYCFPIHGA'

# Sequencias de rna que eu gerei aleatóriamente na internet pra testar:
# https://www.bioinformatics.org/sms2/random_dna.html
# https://molbiotools.com/randomsequencegenerator.ph
s8 = 'CAUGGCAGAUUCGUCUUAACAAAAGGUAGCUCUAUGCGAG'
s9 = 'CACGAGACUGACUCUGAUCACACAUUGCUACUCCAAAACU'

# sequencias que eu peguei ali em cima e adicionei um "B" ou "O" no final
s10 = 'CAUGGCAGAUUCGUCUUAACAAAAGGUAGCUCUAUGCGAGB'
s11 = 'CACGAGACUGACUCUGAUCACACAUUGCUACUCCAAAACUO'

# Fiz essa lista pra poder checar todas as listas de uma vez só
seqs = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]

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

