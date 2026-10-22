def word_frequency(text):
  freq = {}
  x = text.split()
  for i in x:
   freq[i] = freq.get(i,0)+1
  return freq

