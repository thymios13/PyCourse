def plot_results(filename, initial_density, final_density):
    from matplotlib import pyplot

    #Store the results into a .png image.
    filename += '.png'

    #Create the range of values in the x-axis, based on the length of the input matrices.
    length = len(initial_density);
    x_interval = range(length);

    # http://matplotlib.org/api/pyplot_api.html?highlight=subplots#matplotlib.pyplot.subplots
    # Both sup-plots will share the y-axis.
    f, (subplot1, subplot2) = pyplot.subplots(1, 2, sharey=True);

    #https://scipy-lectures.github.io/intro/matplotlib/matplotlib.html#bar-plots
    #Create the sub-plot based on the initial density.
    subplot1.bar(x_interval, initial_density, facecolor='green')
    subplot1.set_title('Initial density values.')
    subplot1.set_xlabel('Initial position.')
    subplot1.set_ylabel('Total particles.')

    #Create the sub-plot based on the final density.
    subplot2.bar(x_interval, final_density, facecolor='blue')
    subplot2.set_title('Final density values.')
    subplot2.set_xlabel('Final position.')

    #Store the plot and project it on the screen.
    pyplot.savefig(filename)
    pyplot.show()
