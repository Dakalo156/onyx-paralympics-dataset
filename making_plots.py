import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_season_pie(df, col_name, title_name):
    summer = df[df["games_season"] == "Summer"][col_name].sum()
    winter = df[df["games_season"] == "Winter"][col_name].sum()
    print(f"Summer: {summer} \nWinter: {winter}")

    seasons = ["Summer", "Winter"]
    totals = [summer, winter]

    # Plotting the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(totals, labels=seasons, autopct="%1.1f%%", startangle=140)
    plt.title(f"{title_name}")
    plt.show()


def plot_season_trend(df, col_name, group_name):
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(
        data=df,
        x="games_year",
        y=col_name,
        hue="games_season",
        style="games_season",
        markers=["o", "o"],
        markersize=8,
    )

    ax.xaxis.grid()
    plt.xticks(
        np.arange(
            df["games_year"].min(),
            df["games_year"].max() + 1,
            2.0,
        )
    )
    plt.xticks(rotation=80)
    ax.set(
        xlabel="Games Year",
        ylabel=f"Number of {group_name}",
        title=f"Number of {group_name} Over the Years - Summer and Winter Events",
    )
    plt.legend()
    plt.show()


def hosting_times_bar(counter_list, name: str):
    keys = list(dict(counter_list).keys())
    values = list(dict(counter_list).values())

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.bar(keys, values, color="teal")

    ax.set(
        title=f"Number of time a {name} hosted Paralympic Events", xlabel="", yticks=[]
    )
    plt.xticks(rotation=80)
    ax.yaxis.set_visible(False)

    for p in ax.patches:
        height = p.get_height()
        # Add text label above each bar
        ax.text(
            p.get_x() + p.get_width() / 2.0,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
            # fontweight="bold",
        )
    plt.tight_layout()
    plt.show()
