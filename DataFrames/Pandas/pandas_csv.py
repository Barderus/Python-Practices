import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv(
    r'C:\Users\gabe_\OneDrive\Documents\GitHub\Python-Practices\DataFrames\Pandas\pokemon_data.csv')

# Information about the dataset
print(pokemon_df.info())

# Only display gen 1 - 4
gen = pokemon_df[pokemon_df["generation"] < 5]

# Main attribute of each Pokemon
pokes = pokemon_df[["dexnum", "name", "generation", "type1", "type2", "hp",
                    "attack", "defense", "sp_atk", "sp_def", "speed"]]

# Catch rate of each Pokemon in descending order
catch_rate = gen[["dexnum", "name", "generation", "catch_rate"]]
print(catch_rate.sort_values(by=["generation", "catch_rate"], ascending=False).to_string())

# Visualization 1: Distribution of Pokémon Generations
plt.figure(figsize=(10, 6))
sns.countplot(x='generation', data=pokemon_df, palette='viridis')
plt.title('Distribution of Pokémon Generations')
plt.xlabel('Generation')
plt.ylabel('Count')
plt.show()

# Visualization 2: Distribution of Pokémon Types
plt.figure(figsize=(14, 8))
type_counts = pd.concat([pokemon_df['type1'], pokemon_df['type2']]).value_counts()
sns.barplot(x=type_counts.index, y=type_counts.values, palette='viridis')
plt.title('Distribution of Pokémon Types')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Visualization 3: Pokemon Catch Rates per generation
# plt.figure(figsize=(12, 6))
# sns.boxplot(x='generation', y='catch_rate', data=pokemon_df, palette='viridis')
# plt.title('Distribution of Catch Rate by Pokémon Generation')
# plt.xlabel('Generation')
# plt.ylabel('Catch Rate')
# plt.show()
#
# plt.figure(figsize=(12, 6))
# sns.violinplot(x='generation', y='catch_rate', data=pokemon_df, palette='viridis')
# plt.title('Distribution of Catch Rate by Pokémon Generation')
# plt.xlabel('Generation')
# plt.ylabel('Catch Rate')
# plt.show()

# Aggregate the data: mean catch rate of Pokémon per generation and catch rate
agg_data = pokemon_df.groupby(['generation', 'catch_rate']).mean().unstack(fill_value=0)

# Plotting
agg_data.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis', legend=False)
plt.title('Mean Catch Rate of Pokémon by Generation and Catch Rate')
plt.xlabel('Generation')
plt.ylabel('Mean Catch Rate')
plt.show()

# # Calculate the average catch rate for each generation
# avg_catch_rate = pokemon_df.groupby('generation')['catch_rate'].mean().reset_index()
#
# # Visualization: Average Catch Rate by Pokémon Generation
# plt.figure(figsize=(12, 6))
# sns.barplot(x='generation', y='catch_rate', data=avg_catch_rate, palette='viridis')
# plt.title('Average Catch Rate by Pokémon Generation')
# plt.xlabel('Generation')
# plt.ylabel('Average Catch Rate')
# plt.show()