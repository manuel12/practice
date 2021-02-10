import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
lines = ['* ' + lines[i]  for i in  range(len(lines))]
text = '\n'.join(lines)
pyperclip.copy(text)
