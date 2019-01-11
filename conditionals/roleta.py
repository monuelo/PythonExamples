# coding: utf-8
# Roleta
# (c) Héricles Emanuel, UFCG, Programação 1

num = int(raw_input())
cor = raw_input()
num_sort = int(raw_input())
cor_sort = raw_input()

if num == num_sort and cor == cor_sort:
	print "150"
elif num == num_sort and cor != cor_sort:
	print "100"
elif cor == cor_sort and num_sort > num:
	print "80"
elif cor == cor_sort and num_sort < num:
	print "100"
elif cor != cor_sort and num != num_sort:
	print "0"