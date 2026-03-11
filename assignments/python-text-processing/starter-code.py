"""
Python Text Processing Utility - Starter Code

This is a starter template for building a text processing utility.
Follow the requirements in the README.md to complete the assignment.
"""

import os
import string
from collections import Counter

# TODO: Implement the following functions:
# 1. read_file(filename) - Read text from a file
# 2. clean_text(text) - Remove punctuation and normalize whitespace
# 3. count_words(text) - Count word frequencies
# 4. split_into_sentences(text) - Split text into sentences
# 5. generate_statistics(text) - Calculate text statistics
# 6. write_to_file(filename, content) - Write processed text to file
# 7. main() - Orchestrate the text processing workflow

def read_file(filename):
    """
    Read and return the contents of a text file.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        str: Contents of the file
        
    Raises:
        FileNotFoundError: If the file does not exist
    """
    # TODO: Implement file reading
    pass

def clean_text(text):
    """
    Clean and normalize text by removing punctuation and extra whitespace.
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned text
    """
    # TODO: Implement text cleaning
    pass

def count_words(text):
    """
    Count the frequency of each word in the text.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        dict: Dictionary of word frequencies
    """
    # TODO: Implement word counting
    pass

def split_into_sentences(text):
    """
    Split text into sentences.
    
    Args:
        text (str): Text to split
        
    Returns:
        list: List of sentences
    """
    # TODO: Implement sentence splitting
    pass

def generate_statistics(text):
    """
    Generate statistics about the text.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        dict: Dictionary containing word count, character count, unique words, etc.
    """
    # TODO: Implement statistics generation
    pass

def write_to_file(filename, content):
    """
    Write content to a file.
    
    Args:
        filename (str): Path to the output file
        content (str): Content to write
    """
    # TODO: Implement file writing
    pass

def main():
    """
    Main function to orchestrate text processing workflow.
    """
    # TODO: Implement main workflow:
    # 1. Prompt user for input file
    # 2. Read the file
    # 3. Clean and process the text
    # 4. Generate statistics
    # 5. Write results to output file
    # 6. Display summary to user
    pass

if __name__ == "__main__":
    main()
