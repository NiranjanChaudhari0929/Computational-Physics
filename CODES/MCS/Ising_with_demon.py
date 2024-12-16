import numpy as np

# Set the size of the lattice and the temperature
L = 32
T = 2.0

# Initialize the lattice with random spin values
spins = 2*np.random.randint(2, size=(L,L))-1

# Set the coupling constant and the external field
J = 1.0
H = 0.0

# Set the number of Monte Carlo steps to perform
nsteps = 1000

# Set the number of demon moves to perform per Monte Carlo step
ndemons = 10

# Set the demon acceptance probability
p = 0.5

# Initialize the magnetization and energy
M = np.sum(spins)
E = -J*np.sum(spins[:,:-1]*spins[:,1:]) - J*np.sum(spins[:-1,:]*spins[1:,:]) - H*np.sum(spins)

# Initialize lists to store the values of the magnetization and energy
Mlist = []
Elist = []

# Perform the Monte Carlo simulation
for step in range(nsteps):
    # Perform the demon moves
    for demon in range(ndemons):
        # Choose a random spin
        i = np.random.randint(L)
        j = np.random.randint(L)
        spin = spins[i,j]
        
        # Compute the change in energy if the spin is flipped
        deltaE = 2*spin*(J*(spins[(i+1)%L,j] + spins[(i-1)%L,j] + spins[i,(j+1)%L] + spins[i,(j-1)%L]) + H)
        
        # Accept or reject the spin flip with probability p
        if deltaE <= 0 or np.random.rand() < np.exp(-deltaE/T):
            spins[i,j] = -spin
            M += 2*spin
            E += deltaE
    
    # Update the lists storing the magnetization and energy
    Mlist.append(M)
    Elist.append(E)

# Compute the average magnetization
avgM = np.mean(Mlist)

# Compute the specific heat
C = (np.var(Elist)/T**2)/(L**2)

# Compute the magnetic susceptibility
X = (np.var(Mlist)/T)/(L**2)

# Print the results
print("Average magnetization: ", avgM)
print("Specific heat: ", C)
print("Magnetic susceptibility: ", X)
