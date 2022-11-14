from numpy import asarray, exp
from numpy.random import randn, rand, seed
from matplotlib import pyplot

# Define objective function
def objective(step):
    return step[0] ** 2.0

# Define simulated annealing algorithm
def sa(objective, area, iterations, step_size, temperature):
    # create initial point
    start_point = area[:, 0] + rand( len( area ) ) * ( area[:, 1] - area[:, 0] )
    # evaluate initial point
    start_point_eval = objective(start_point)
    # Assign previous and new solution to previous and new_point_eval variable 
    actual_start_point, actual_start_eval = start_point, start_point_eval
    outputs = []
    for i in range(iterations):
        # First step by mia
        step = actual_start_point + randn( len( area ) ) * step_size  
        step_eval = objective(step)
        if step_eval < start_point_eval:
            start_point, start_point_eval = step, step_eval
      #Append the new values into the output list
            outputs.append(start_point_eval)
            print('Criterio de aceptacion = %.5f' % mac," ",'iteracion = ',i," ", 'mejor anterior = ',start_point," " ,'nuevo mejor = %.5f' % start_point_eval)
        difference = step_eval - actual_start_eval
        t = temperature / float(i + 1)
        # calculate Metropolis Acceptance Criterion / Acceptance Probability
        mac = exp(-difference / t)
        # check whether the new point is acceptable 
        if difference < 0 or rand() < mac:
            actual_start_point, actual_start_eval = step, step_eval
    return [start_point, start_point_eval, outputs]

if __name__ == '__main__':
    seed(1)
    # define the area of the search space
    area = asarray([[-5.0, 5.0]])
    # initial temperature
    temperature = 12
    # define the total no. of iterations
    iterations = 1200
    # define maximum step_size
    step_size = 0.1
    # perform the simulated annealing search
    start_point, output, outputs = sa(objective, area, iterations, step_size, temperature)
    #plotting the values
    pyplot.plot(outputs, 'ro-')
    pyplot.xlabel('Valor de mejora')
    pyplot.ylabel('Evaluacion de la funcion objetivo')
    pyplot.show()