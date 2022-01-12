class Helper:
    def count_plot(x):
        import matplotlib.pyplot as plt
        import seaborn as sns

        print(x)
        print('-----')

        sns.distplot(x, hist=True, kde=True)

        plt.show()