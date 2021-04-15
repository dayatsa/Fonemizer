from fonem import *

converter = IndoARPA(separator=' ', res_ipa=True)


texts = ["ternak", "gembala", "ambil", "bakpao", "saung", "kait", "lebah", "cuka", "diam", "ridho", "énak", "faédah","gerbang","hampar","singgah","adiraja","kenangan","lingkaran","minum","naik","yang","bongkar","pulsa","ranjau","sayang","masyarakat","tikung","kuku","viral","wejangan","yakin","zaman","jangkrik","tsani"]

for text in texts:
  # print(text)
  res = converter.indo2ARPA(text)
  print("{} =  {}".format(text, res))