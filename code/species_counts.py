# Count the number of samples by species_id
# HINT: use record_id as a column to count
species_counts = surveys_df.groupby('')[''].count()
print(species_counts)

# we can also count just a single one, try DO
surveys_df.groupby('species_id')['record_id'].count()