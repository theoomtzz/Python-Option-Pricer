import matplotlib.pyplot as plt

def drawn(X, Y, average, elapsed_time):
    fig, ax = plt.subplots()
    ax.text(0.05, 0.92, f'Execution time {elapsed_time} secondes', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})
    moyenne = float(np.sum(Y[-1, :]) / Y.shape[1])
    ax.text(0.05, 0.80, f'Average Price: {moyenne} dollars', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'green', 'alpha': 0.5, 'pad': 10})
    ax.set_title("Monte-Carlo simulation for WTI oil")
    ax.set(xlabel = "time (year)", ylabel = "price (dollar)")
    ax.plot(X, Y, '-', linewidth = 0.5)
    plt.show()