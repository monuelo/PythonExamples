# coding: utf-8
# Espaço em Disco Simplificado
# (c) Héricles Emanuel, UFCG, Programação 1

usuario1 = (raw_input())
space1 = float(raw_input())
usuario2 = (raw_input())
space2 = float(raw_input())
usuario3 = (raw_input())
space3 = float(raw_input())
print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado\n"

smb1 = (space1 / 1024) / 1024.0
smb2 = (space2 / 1024) / 1024.0
smb3 = (space3 / 1024) / 1024.0

print "1, %s, %.2f MB" % (usuario1 , smb1)
print "2, %s, %.2f MB" % (usuario2 , smb2)
print "3, %s, %.2f MB" % (usuario3 , smb3)

total = smb1 + smb2 + smb3
medio = (smb1 + smb2 + smb3) / 3

print "\nEspaço total ocupado: %.2f MB" % total
print "Espaço médio ocupado: %.2f MB" % medio