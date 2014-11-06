max_iterations = 50;


def update_density(density_matrix):
    from random import randint, choice

    length = len(density_matrix);
    if length == 0:
        raise TypeError("The density matrix must have a positive length!");

    #Choose the index to upgrade in a random fashion.
    index = randint(0, length - 1);

    if index == 0:
        direction = 1
    elif index == (length - 1):
        direction = -1
    else:
        direction = choice([-1, 1])

    updated_matrix = list(density_matrix)

    if updated_matrix[index] > 0:
        updated_matrix[index] -= 1;
        updated_matrix[index + direction] += 1

    return updated_matrix;


def main(energy, density, temperature=100):
    from math import exp;
    from random import random;
    from plot import plot_results;

    if type(density) != list:
        raise TypeError("The density matrix is not in the proper form!");

    #Store the initial density.
    initial_density = list(density)

    #Calculate the current energy.
    current_energy = energy(density)

    current_ite = 0;
    while current_ite < max_iterations:

        #Calculate the new density matrix.
        updated_density = update_density(density);

        print(updated_density)

        #Calculate the new energy.
        updated_energy = energy(updated_density);

        #Decide if the new energy must be accepted or not.
        if updated_energy < current_energy:
            density = updated_density;
            current_energy = updated_energy;
        else:
            P0 = exp(-(updated_energy - current_energy) / temperature) > random();
            if P0:
                density = updated_density;
                current_energy = updated_energy;

        current_ite += 1;

    print("The simulation has finished!")

    plot_results('output', initial_density, density)

    return;
