# Returns True for every row that is a duplicate, otherwise False:

print(df.duplicated())

# Remove all duplicates:

df.drop_duplicates(inplace = True)

