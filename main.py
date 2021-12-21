import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

def planifica(horario, ubicacion, duracion, asistencia):
    if horario:
        # En horas de oficiona
        return (ubicacion and asistencia)
    else:
        # Fuera de horario 
        return (not ubicacion and duracion)

csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
csp.add_constraint(planifica, ['horario', 'ubicacion', 'duracion','asistencia'])

bqm = dwavebinarycsp.stitch(csp)
print(bqm.linear)
print(bqm.quadratic)

response = sampler.sample(bpm, num_reads= 5000)
min_energy = next(response.data(['energy']))[0]

print(response)

total = 0
for sample, energy, ocurrences in response.data(['sample', 'energy', 'num_ocurrences']):
    total = total + 