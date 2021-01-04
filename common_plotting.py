def load_plotting_style():
    import matplotlib as mpl
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['axes.labelsize'] = 15
    mpl.rcParams['xtick.labelsize'] = 10
    mpl.rcParams['ytick.labelsize'] = 10
    mpl.rcParams['legend.fontsize'] = 8.3
    mpl.rcParams['figure.figsize'] = 5, 3.8

    # colors
    import seaborn as sns
    sns.set_palette("rocket",3)
