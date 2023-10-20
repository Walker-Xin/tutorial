import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib


def plot(functions, x_range=(-10, 10), special_points=None, text=None, filename='plot', axis=True, origin=False, ticks=False, **kwargs):
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
    origin : bool
        Whether to denote the origin.
    ticks : bool
        Whether to draw the x and y ticks.
    **kwargs : dict
        Additional keyword arguments to pass to matplotlib and tikzplotlib.

    Returns
    -------
    code : str
        The tikz code of the plot.
    '''

    for func in functions:
        x = np.linspace(x_range[0], x_range[1], 300)
        y = np.linspace(x_range[0], x_range[1], 300)
        y = np.array([func(i) for i in x])

        # Pop nan values points
        for i in range(len(y)):
            if y[i] == None:
                np.delete(x, i)
                np.delete(y, i)

        plt.plot(x, y)

    # Plot axes
    if axis == True:
        plt.axhline(y=0, color='gray')
        plt.axvline(x=0, color='gray')

    if origin == True:
        plt.text(0, 0, r'0', fontsize=10, color='grey', ha='right', va='top')

    plt.xlabel(kwargs.get('xlabel', ''))
    plt.ylabel(kwargs.get('ylabel', ''))
    plt.title(kwargs.get('title', ''))
    plt.ylim(kwargs.get('ylims', None))
    plt.xlim(kwargs.get('xlims', None))

    # Remove ticks
    if ticks == False:
        plt.xticks([])
        plt.yticks([])

    # Plot special points
    if special_points != None:
        # Check if a number is not zero
        def not_zero(x):
            return True if abs(x) > 1e-10 else False
        
        for key in special_points:
            x_ = key[0]
            y_ = key[1]
            note = special_points[key]
            plt.plot(x_, y_, 'r.')

            # Add coordinate lines if there is no custom note
            if note == None:
                if not_zero(x_) and not_zero(y_):
                    plt.plot([x_, 0], [y_, y_], color='grey', linestyle='--')
                    plt.plot([x_, x_], [y_, 0], color='grey', linestyle='--')
                if not_zero(x_):
                    plt.text(x_, -0.01, r'{:.2f}'.format(x_),
                            fontsize=kwargs.get('fontsize', 10), color='black', ha='center', va='top')
                if not_zero(y_):
                    plt.text(-0.01, y_, r'{:.2f}'.format(y_),
                            fontsize=kwargs.get('fontsize', 10), 
                            color='black', ha='left', va='center')
            else:
                plt.text(x_, y_, note, fontsize=kwargs.get('fontsize', 10), color='black', ha='center', va='bottom')
                
                
    # Plot text
    if text != None:
        for key in text:
                plt.text(key[0], key[1], text[key], fontsize=kwargs.get('fontsize', 10), color='black', ha='center', va='bottom')

    # Save and view plot
    tikzplotlib.save(filename, strict=kwargs.get('strict', False))
    plt.show()
    code = tikzplotlib.get_tikz_code()

    return code


# Test
if __name__ == '__main__':
    # def func(x):
    #     return np.piecewise(x, [x <= 1.0, x > 1.0, x >= 2.0], [0, lambda x: (np.square(x) - 1.0)/(2.0*x), lambda x: (np.square(2.0)- 1.0)/(2.0*2.0)])

    def func_1(x):
        return -0.1*x + 5.0 if x <= 50 else 0

    def func_2(x):
        return -0.1*x + 2.0 if x <= 20 else 0

    def func_3(x):
        return -0.1*x + 1.0 if x <= 10 else 0

    # def func_1(x):
    #     return 1/(0.5 + x)

    # def func_2(x):
    #     return x*x

    funcs = [func_1, func_2, func_3]

    # texts = {
    #         (1.1, func_2(1.1)): r'$T_{2}$',
    #         (0.6, func_1(0.6)): r'$T_{1}$'
    #         }
    
    # points = {
    #         (0.7, func_2(0.7)): r'System 2',
    #         (0.7, func_1(0.7)): r'System 1'
    # }

    plot(funcs, x_range=(0, 8), filename='second_year/plots/test.tex', axis=True, origin=False, ticks=False, xlabel=r'$P$', ylabel=r'$V$', fontsize=12, strict=True)
