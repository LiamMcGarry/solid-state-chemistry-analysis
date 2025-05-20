import sys
import os
import pandas as pd

# Add src folder to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from xrd_analysis import load_xrd_data, normalize_intensity

def test_load_xrd_data():
    # Build path to sample_xrd.csv relative to this test file
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_xrd.csv'))

    # Load sample data
    df = load_xrd_data(data_path)
    assert isinstance(df, pd.DataFrame)
    assert '2Theta' in df.columns
    assert 'Intensity' in df.columns

def test_normalize_intensity():
    df = pd.DataFrame({'Intensity': [10, 20, 30]})
    df = normalize_intensity(df)
    assert 'NormalizedIntensity' in df.columns
    assert df['NormalizedIntensity'].max() == 1.0
