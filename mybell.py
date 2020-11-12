# Import the Cirq library
import cirq

#INSERTAR X,Y DESEADOS
x = '1'
y = '1'


bell_circ = cirq.Circuit()

q0, q1 = cirq.LineQubit.range(2)
bell_circ.append(cirq.H(q0))



if x=='0' and y=='0':
    bell_circ.append(cirq.CNOT(q0,q1))
elif x=='0' and y=='1' :
    bell_circ.append(cirq.CNOT(q0,q1))
    bell_circ.append(cirq.X(q1))
elif x=='1' and y=='0':
    bell_circ.append(cirq.CNOT(q0,q1))
    bell_circ.append(cirq.Z(q1))
elif x=='1' and y=='1':
    bell_circ.append(cirq.CNOT(q0,q1))
    bell_circ.append(cirq.Y(q1))

#initialize sim

s = cirq.Simulator()

print('Circuit')
print(bell_circ)
print('Simulate the circuit:')
results = s.simulate(bell_circ)
print(results)
print()

bell_circ.append(cirq.measure(q0, q1, key = 'z'))

print('Sample the circuit:')
samples = s.run(bell_circ, repetitions = 100)
print(samples.histogram(key = 'z'))


