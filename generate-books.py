import pandas as pd
import os
from pathlib import Path

# Import books dataset
abs_path = Path(".").absolute()
books = pd.read_csv(str(abs_path) + os.sep + "Books.csv")
book_titles = books["Titles"]

# TODO: generate synthetic book titles based on scraped data
