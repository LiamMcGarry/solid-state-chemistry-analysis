import pandas as pd
import matplotlib.pyplot as plt

def load_xrd_data(filepath):
    """
    Load XRD data from a CSV file.

    Parameters:
        filepath (str): Path to the CSV file containing '2Theta' and 'Intensity' columns.

    Returns:
        pd.DataFrame: DataFrame with the XRD data.
    """
    return pd.read_csv(filepath)

def normalize_intensity(df):
    """
    Normalize the intensity values so the maximum is 1.

    Parameters:
        df (pd.DataFrame): DataFrame with 'Intensity' column.

    Returns:
        pd.DataFrame: Updated DataFrame with new 'NormalizedIntensity' column.
    """
    df['NormalizedIntensity'] = df['Intensity'] / df['Intensity'].max()
    return df

def plot_xrd(df):
    """
    Plot the normalized XRD pattern.

    Parameters:
        df (pd.DataFrame): DataFrame with '2Theta' and 'NormalizedIntensity' columns.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(df['2Theta'], df['NormalizedIntensity'], color='blue', lw=2)
    plt.xlabel("2θ (degrees)")
    plt.ylabel("Normalized Intensity")
    plt.title("X-ray Diffraction Pattern")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Run this only when file is executed directly
    filepath = "../data/sample_xrd.csv"  # path to your CSV file
    data = load_xrd_data(filepath)
    data = normalize_intensity(data)
    plot_xrd(data)
