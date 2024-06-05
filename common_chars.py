def common_chars(words):
  letters = {ch: 0 for ch in words[0]}
  return letters


words = ['bella', 'label', 'roller']

print(common_chars(words))

"""
  Expected output:
    ['e', 'l', 'l']
"""
