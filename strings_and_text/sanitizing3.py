import unicodedata
import sys

# s = 'pýtĥöñ\fis\tawesome\r\n'

# remap = {
#     ord('\t'): ' ',
#     ord('\f'): ' ',
#     ord('\r'): None      # Deleted
# }
# a = s.translate(remap)

# cmb_chrs = dict.fromkeys(c for c in range(
#     sys.maxunicode) if unicodedata.combining(chr(c)))
# b = unicodedata.normalize('NFD', a)
# x = b.translate(cmb_chrs)

# print(x)

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'}

print(digitmap)
