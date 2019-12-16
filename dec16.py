import numpy as np

inputs = "59782619540402316074783022180346847593683757122943307667976220344797950034514416918778776585040527955353805734321825495534399127207245390950629733658814914072657145711801385002282630494752854444244301169223921275844497892361271504096167480707096198155369207586705067956112600088460634830206233130995298022405587358756907593027694240400890003211841796487770173357003673931768403098808243977129249867076581200289745279553289300165042557391962340424462139799923966162395369050372874851854914571896058891964384077773019120993386024960845623120768409036628948085303152029722788889436708810209513982988162590896085150414396795104755977641352501522955134675"
# inputs = "80871224585914546619083218645595"

def getPattern(size):
    pattern = np.zeros((size, size), dtype=int)
    base = np.array([0, 1, 0, -1], dtype=int)
    for i in range(size):
        tempBase = np.repeat(base, i+1)
        if tempBase.size <= size:
            tempBase = np.tile(tempBase, (size//tempBase.size)+1)
        pattern[i] = tempBase[1:size+1]
    return pattern

def getSequence(numPhase, pattern, sequence):
    for i in range(numPhase):
        sequence = pattern @ sequence
        sequence = np.absolute(sequence) % 10
    return sequence.T[0]

# part 1
pattern = getPattern(len(inputs))
sequence = np.array([int(i) for i in inputs])
sequence = sequence[np.newaxis].T
numPhase = 100

final = getSequence(numPhase, pattern, sequence)
print(final[:8])

# part 2
sequence = np.array([int(i) for i in inputs*10000])
offset = int(inputs[:7])
data = sequence[offset:]
for i in range(numPhase):
    data = np.cumsum(data[::-1]) % 10
    data = data[::-1]

print(data[:8])