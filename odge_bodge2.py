import random

vowels = ('i', 'ee', 'a', 'ar', 'o', 'or', 'u', 'oo', 'ir', 'e', 'ay', 'oa', 'ie', 'ow', 'oi' 'eer')
consonants = ('m', 'p', 'b', 'f', 'v', 'th', 'n', 't', 'd', 's', 'z', 'l', 'ch', 'j', 'sh', 's', 'r', 'y', 'k', 'g', 'w', 'h')
onset_con_clu = ('pr', 'pl', 'br', 'bl', 'fr', 'fl', 'tr', 'dr', 'sl', 'kr', 'kl', 'gr', 'gl', 'gw')
coda_con_clu = ('ms', 'med', 'ps', 'ped', 'bs', 'bed', 'fs', 'fed', 'vs', 'vd', 'ths', 'ns', 'nt', 'nd', 'ts', 'ds', 'ls', 'rs', 'ys', 'ks', 'kd', 'gs', 'gd')

def word_length():
	wlength = 1
	likely = random.randint(1,15)
	if likely < 5:
		wlength = 1
	elif likely in range(5, 8):
		wlength = 2
	elif likely in range (9, 11):
		wlength = 3
	elif likely in range (12, 13):
		wlength = 4
	elif likely in range (14, 15):
		wlength = 5
	elif likely == 16:
		wlength = 6
	return wlength
	
def syllable_form():
	onset_likely = random.randint(0, 2)
	if onset_likely == 0:
		onset = ""
	elif onset_likely == 1:
		onsetnum = random.randint(0, 21)
		onset = consonants[onsetnum]
	elif onset_likely == 2:
		onsetnum = random.randint(0, 13)
		onset = onset_con_clu[onsetnum]

	nucleusnum = random.randint(0, 14)
	nucleus = vowels[nucleusnum]
	
	coda_likely = random.randint (0, 2)
	if coda_likely == 0:
		coda = ""
	elif coda_likely == 1:
		codanum = random.randint(0, 21)
		coda = consonants[codanum]
	elif coda_likely == 2:
		codanum = random.randint(0, 22)
		coda = coda_con_clu[codanum]
	
	syllable = (onset + nucleus + coda)
	return syllable


def generate_word():
	word = ""
	wlength = word_length()
	if wlength == 1:
		word = syllable_form()
	elif wlength == 2:
		syllable1 = syllable_form()
		syllable2 = syllable_form()
		word = (syllable1 + syllable2)
	elif wlength == 3:
		syllable1 = syllable_form()
		syllable2 = syllable_form()
		syllable3 = syllable_form()
		word = (syllable1 + syllable2 + syllable3)
	elif wlength == 4:
		syllable1 = syllable_form()
		syllable2 = syllable_form()
		syllable3 = syllable_form()
		syllable4 = syllable_form()
		word = (syllable1 + syllable2 + syllable3 + syllable4)
	elif wlength == 5:
		syllable1 = syllable_form()
		syllable2 = syllable_form()
		syllable3 = syllable_form()
		syllable4 = syllable_form()
		syllable5 = syllable_form()
		word = (syllable1 + syllable2 + syllable3 + syllable4 + syllable5)
	elif wlength == 6:
		syllable1 = syllable_form()
		syllable2 = syllable_form()
		syllable3 = syllable_form()
		syllable4 = syllable_form()
		syllable5 = syllable_form()
		syllable6 = syllable_form()
		word = (syllable1 + syllable2 + syllable3 + syllable4 + syllable5 + syllable6)
	print (word)

generate_word()