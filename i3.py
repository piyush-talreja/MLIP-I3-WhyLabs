import pandas as pd
import numpy as np

# Input date from the user (format: YYYY-MM-DD)
input_date = '2024-03-26'

# Calculate entries for a total of ~2000 entries
total_entries = 100

# Dictionary of movies and their genres
movies_with_genres = {'movie1': 'Drama', 'movie2': 'Crime', 'movie3': 'Crime', 'movie4': 'Action',
                      'movie5': 'Drama', 'movie6': 'History', 'movie7': 'Fantasy', 'movie8': 'Crime',
                      'movie9': 'Western', 'movie10': 'Fantasy', 'movie11': 'Drama', 'movie12': 'Drama',
                      'movie13': 'Science Fiction', 'movie14': 'Fantasy', 'movie15': 'Science Fiction',
                      'movie16': 'Science Fiction', 'movie17': 'Crime', 'movie18': 'Drama',
                      'movie19': 'Action', 'movie20': 'Thriller'}

# Generate user IDs, ratings, and occupations for each entry
user_ids = np.random.randint(1001, 1101, size=total_entries)
ratings = np.random.randint(4, 5, size=total_entries)
occupations = np.random.choice(['Student', 'Engineer', 'Doctor', 'Lawyer', 'Farmer'], size=total_entries)

# Randomly select a movie for each entry
movie_names = list(movies_with_genres.keys())
selected_movies = np.random.choice(movie_names, size=total_entries)

# Map selected movie names to their genres
selected_genres = [movies_with_genres[movie] for movie in selected_movies]

# Create the DataFrame without the 'date' column
df = pd.DataFrame({
    'user_id': user_ids,
    'rating': ratings,
    'occupation': occupations,
    'movie_name': selected_movies,
    'genre': selected_genres
})

# Format the filename with the user-provided date
filename = f'data_{input_date}.csv'

# Save the DataFrame to a CSV file
df.to_csv(filename, index=False)
print(f"DataFrame saved to {filename} successfully.")
