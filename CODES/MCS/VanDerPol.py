import numpy as np

def van_der_pol(t, y, mu):
  """
  The Van der Pol oscillator differential equation.
  """
  dy_dt = [y[1], mu * (1 - y[0]**2) * y[1] - y[0]]
  return dy_dt

def solve_van_der_pol(mu, y0, t_span, tol=1e-6):
  """
  Solve the Van der Pol oscillator using the shooting method and the Runge-Kutta method.
  """
  # Set the time step
  dt = 0.01

  # Initialize the solution array
  y = np.empty((2, len(t_span)))
  y[:, 0] = y0

  # Iterate until the error is within the tolerance
  error = tol + 1
  while error > tol:
    # Initialize the solution at the current time step
    y_i = y0

    # Iterate over the time steps
    for i in range(1, len(t_span)):
      # Compute the next time step
      t = t_span[i-1]
      k1 = dt * np.array(van_der_pol(t, y_i, mu))
      k2 = dt * np.array(van_der_pol(t + dt/2, y_i + k1/2, mu))
      k3 = dt * np.array(van_der_pol(t + dt/2, y_i + k2/2, mu))
      k4 = dt * np.array(van_der_pol(t + dt, y_i + k3, mu))
      y_i += (k1 + 2*k2 + 2*k3 + k4) / 6

      # Update the solution array
      y[:, i] = y_i

    # Compute the error
    error = np.abs(y[0, -1] - y[0, -2])

    # Adjust the initial condition for the next iteration
    y0[0] += (y[0, -1] - y[0, -2]) / 2

  return y

# Set the parameters
mu = 2
y0 = [0, 1]
t_span = [0, 20]

# Solve the Van der Pol oscillator
y = solve_van_der_pol(mu, y0, t_span)

# Print the solution
print(y)
