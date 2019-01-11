# coding: utf-8
# Aluno: Héricles Emanuel Gomes da Silva
# Matrícula: 117110647
# Atividade: Diferença entre Dois Horários no Dia
def quanto_tempo(horario1, horario2):
    horario1 = horario1.split(":")
    horario2 = horario2.split(":")
    horas = int(horario2[0]) - int(horario1[0])
    minutos = int(horario2[1]) - int(horario1[1])
    if minutos < 0:
        horas -= 1
        minutos = 60 + minutos
    return "%i hora(s) e %i minuto(s)" % (horas, minutos)