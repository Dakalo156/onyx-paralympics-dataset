from collections import Counter


def hosting_times(df, col_name):
    filtered_df = df[["games_year", col_name]].copy()
    filtered_df["key"] = filtered_df["games_year"].astype(str) + filtered_df[col_name]

    my_list = []
    for country in filtered_df["key"].unique():
        country = country[4:]
        my_list.append(country)

    return Counter(my_list)
