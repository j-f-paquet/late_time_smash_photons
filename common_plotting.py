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


def load_plotting_style_paper():
    import matplotlib as mpl
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['axes.labelsize'] = 16
    mpl.rcParams['xtick.labelsize'] = 12
    mpl.rcParams['ytick.labelsize'] = 12
    mpl.rcParams['legend.fontsize'] = 9.5
    mpl.rcParams['figure.figsize'] = 10*0.8, 6*0.8

    # colors
    import seaborn as sns
    sns.set_palette("rocket",3)


def load_plotting_style_paper_v2_panel():
    import matplotlib as mpl
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['axes.labelsize'] = 16
    mpl.rcParams['xtick.labelsize'] = 12
    mpl.rcParams['ytick.labelsize'] = 12
    mpl.rcParams['legend.fontsize'] = 9.5
    mpl.rcParams['figure.figsize'] = 10*0.9, 6*0.9

    # colors
    import seaborn as sns
    sns.set_palette("rocket",3)


def load_plotting_style_v2_sum():
    import matplotlib as mpl
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['axes.labelsize'] = 16
    mpl.rcParams['xtick.labelsize'] = 12
    mpl.rcParams['ytick.labelsize'] = 12
    mpl.rcParams['legend.fontsize'] = 9.5
    mpl.rcParams['figure.figsize'] = 10*0.8, 4*0.8

    # colors
    import seaborn as sns
    sns.set_palette("rocket",3)
