import seaborn as sns
import matplotlib.pyplot as plt
import os

def violin_plot_generator(df, numeric_cols):
    n_cols_graph = 2
    n_rows_graph = (len(numeric_cols) + n_cols_graph - 1) // n_cols_graph

    fig, axes = plt.subplots(n_rows_graph, n_cols_graph, figsize=(6 * n_cols_graph, 5 * n_rows_graph))
    axes = axes.flatten()

    for i, feature in enumerate(numeric_cols):
        sns.violinplot(y=df[feature], ax=axes[i], inner=None, color="skyblue", linewidth=1)
        sns.boxplot(y=df[feature], ax=axes[i], width=0.15, boxprops={'facecolor':'white'})
        axes[i].set_title(f'Distribution of {feature}')
    
    # Remove unused axes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.savefig(os.getenv("ANALYZES_DIR_PATH") + "/ViolinAndBoxplots.png")

def bar_plots_generator(df, categ_cols):
    n_cols_graph = 2
    n_rows_graph = (len(categ_cols) + n_cols_graph - 1) // n_cols_graph

    fig, axes = plt.subplots(n_rows_graph, n_cols_graph, figsize=(6 * n_cols_graph, 4 * n_rows_graph))

    if isinstance(axes, plt.Axes):
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, col in enumerate(categ_cols):
        value_counts = df[col].value_counts().head(20)  # show top 20 categories
        sns.barplot(x=value_counts.values, y=value_counts.index, ax=axes[i], palette="viridis")
        axes[i].set_title(f'{col} (Top 20)')
        axes[i].set_xlabel("Count")
        axes[i].set_ylabel("")

    # Remove unused axes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
    plt.savefig(os.getenv("ANALYZES_DIR_PATH") + "/BarPlots.png")
