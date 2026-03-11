"""
Python Data Visualization - Starter Code

This is a starter template for creating professional data visualizations.
Follow the requirements in the README.md to complete the assignment.

Work with matplotlib for static visualizations and plotly for interactive charts.
"""

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# TODO: Implement the following functions:

def create_line_chart(x_data, y_data, title="", xlabel="", ylabel="", filename=None):
    """
    Create a line chart showing trends over time.
    
    Args:
        x_data (list): X-axis data
        y_data (list): Y-axis data
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        filename (str): Optional filename to save the chart
    """
    # TODO: Implement line chart using matplotlib
    pass

def create_bar_chart(categories, values, title="", xlabel="", ylabel="", filename=None):
    """
    Create a bar chart for categorical data comparison.
    
    Args:
        categories (list): Category names
        values (list): Values for each category
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        filename (str): Optional filename to save the chart
    """
    # TODO: Implement bar chart using matplotlib
    pass

def create_scatter_plot(x_data, y_data, title="", xlabel="", ylabel="", filename=None):
    """
    Create a scatter plot to show relationships between variables.
    
    Args:
        x_data (list): X-axis data
        y_data (list): Y-axis data
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        filename (str): Optional filename to save the chart
    """
    # TODO: Implement scatter plot using matplotlib
    pass

def create_histogram(data, bins=10, title="", xlabel="", ylabel="", filename=None):
    """
    Create a histogram to visualize data distribution.
    
    Args:
        data (list): Data to plot
        bins (int): Number of bins
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        filename (str): Optional filename to save the chart
    """
    # TODO: Implement histogram using matplotlib
    pass

def create_pie_chart(labels, values, title="", filename=None):
    """
    Create a pie chart for showing proportions and percentages.
    
    Args:
        labels (list): Category labels
        values (list): Values for each category
        title (str): Chart title
        filename (str): Optional filename to save the chart
    """
    # TODO: Implement pie chart using matplotlib
    pass

def create_interactive_line_chart(x_data, y_data, title="", xlabel="", ylabel=""):
    """
    Create an interactive line chart using plotly.
    
    Args:
        x_data (list): X-axis data
        y_data (list): Y-axis data
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
    """
    # TODO: Implement interactive line chart using plotly
    pass

def create_interactive_scatter_plot(df, x_col, y_col, title="", hover_data=None):
    """
    Create an interactive scatter plot using plotly with hover information.
    
    Args:
        df (DataFrame): DataFrame containing the data
        x_col (str): Column name for x-axis
        y_col (str): Column name for y-axis
        title (str): Chart title
        hover_data (list): Additional columns to show on hover
    """
    # TODO: Implement interactive scatter plot using plotly
    pass

def create_multi_series_chart(data_dict, title="", xlabel="", ylabel="", filename=None):
    """
    Create a chart with multiple data series.
    
    Args:
        data_dict (dict): Dictionary with series names as keys and data lists as values
        title (str): Chart title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        filename (str): Optional filename to save the chart
    """
    # TODO: Implement multi-series chart
    pass

def create_subplots(datasets, subplot_titles, filename=None):
    """
    Create multiple subplots in one figure.
    
    Args:
        datasets (list): List of (x_data, y_data) tuples
        subplot_titles (list): Titles for each subplot
        filename (str): Optional filename to save the figure
    """
    # TODO: Implement subplots
    pass

def main():
    """
    Main function to demonstrate data visualization capabilities.
    """
    # TODO: Create sample datasets and test each visualization function
    # Example:
    # - Generate sample time series data
    # - Create sample categorical data
    # - Generate random data for scatter plots and histograms
    # - Call each visualization function with appropriate data
    pass

if __name__ == "__main__":
    main()
