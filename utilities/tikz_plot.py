import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib


def plot(func, range=[-10, 10], special_points=None, filename='plot', axis=False, ticks=True, **kwargs):
    '''
    Plots a function and saves it as a tikz file.
    
    Parameters
    ----------
    func : function
        The function to plot.
    range : list
        The range of the x-axis.
    special_points : list
        A list of tuples containing the x and y coordinates of special points.
    filename : str
        The name of the file to save the plot to.
    axis : bool
        Whether to draw the x and y axis.
    ticks : bool
        Whether to draw the x and y ticks.
    **kwargs : dict
        Additional keyword arguments to pass to matplotlib and tikzplotlib.

    Returns
    -------
    code : str
        The tikz code of the plot.
    '''

    # Generate function values
    x = np.linspace(range[0], range[1], 1000, dtype=float)
    y = func(x)

    # Plot axes
    if axis == True:
        plt.axhline(y=0, color='gray')
        plt.axvline(x=0, color='gray')
        plt.text(0, 0, r'0', fontsize=10, color='grey', ha='right', va='top')
        
    # Plot function
    plt.plot(x, y)
    plt.xlabel(kwargs.get('xlabel', ''))
    plt.ylabel(kwargs.get('ylabel', ''))
    plt.title(kwargs.get('title', ''))
    plt.ylim(kwargs.get('ylims', None))

    # Remove ticks
    if ticks == False:
        plt.xticks([])
        plt.yticks([])

    # Plot special points
    if special_points != None:
        # Check if a number is not zero
        def not_zero(x):
            return True if abs(x) > 1e-10 else False

        for point in special_points:
            x_ = float(point[0])
            y_ = float(point[1])
            plt.plot(x_, y_, 'r.')
            
            # Add coordinate lines
            if not_zero(x_) and not_zero(y_):
                plt.plot([x_, 0], [y_, y_], color='grey', linestyle='--')
                plt.plot([x_, x_], [y_, 0], color='grey', linestyle='--')

            # Add labels to coordinate lines
            if not_zero(x_):
                plt.text(x_, -0.01, r'{:.2f}'.format(x_), fontsize=10, color='grey', ha='center', va='top')
            if not_zero(y_):
                plt.text(-0.01, y_, r'{:.2f}'.format(y_), fontsize=10, color='grey', ha='left', va='center')

    # Save and view plot
    tikzplotlib.save(filename, strict=kwargs.get('strict', False))
    plt.show()
    code = tikzplotlib.get_tikz_code()

    return code


# Test
if __name__ == '__main__':
    def func(x):
        return np.piecewise(x, [x <= 1.0, x > 1.0, x >= 2.0], [0, lambda x: (np.square(x) - 1.0)/(2.0*x), lambda x: (np.square(2.0)- 1.0)/(2.0*2.0)])


    plot(func, range=[0.0, 2.5], ylims=[-0.05, 1], xlabel=r'$r$', ylabel=r'$H$', axis=True, ticks=False, filename='homework/plots/test.tex', strict=True, special_points=[(1.0, func(1.0)), (2.0, func(2.0))])