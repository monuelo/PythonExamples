# coding: utf-8
# Tweets por página
# (c) Héricles Emanuel, UFCG, Programação 1

tweets = int(raw_input())			# Número de Tweets a inserir
									# Considerando 400 tweets/página...
qpag = tweets / 400
tweets_restantes = (tweets % 400.0)
porc_restantes = (tweets_restantes / tweets) * 100.0

print "Serão necessárias %i página(s) para visualizar os tweets." % qpag
print "%.1f%% dos tweets serão perdidos." % porc_restantes
