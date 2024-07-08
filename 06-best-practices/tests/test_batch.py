import pandas as pd
from datetime import datetime
from batch import prepare_data

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]
    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)
    
    expected_data = [
        ('-1', '-1', dt(1, 1), dt(1, 10), 9.0),
        ('1', '1', dt(1, 2), dt(1, 10), 8.0), 
    ]
    expected_columns = columns + ['duration']
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)
    
    result_df = prepare_data(df)

    result_df['duration'] = result_df['duration'].round(6)
    expected_df['duration'] = expected_df['duration'].round(6)

    result_dict = result_df.to_dict(orient='list')
    expected_dict = expected_df.to_dict(orient='list')
    
    assert result_dict == expected_dict