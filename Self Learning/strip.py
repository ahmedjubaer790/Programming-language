fvr_lang='python '
fvr_lang=fvr_lang.rstrip()  #permanent remove space
print(fvr_lang)

#left side
lside=' Java'
prv=lside.lstrip()
print(f"orginal {lside} and after remove using lstrip {prv} ")

#both side remove use .strip()
bth=' Java '
btst=bth.strip()
print(f"Orginal {bth} and after remove using strip {btst}")
