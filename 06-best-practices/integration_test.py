import pandas as pd
from datetime import datetime
import batch
import read_files

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

options = {
    'client_kwargs': {
        'endpoint_url': 'http://localhost.localstack.cloud:4566'
    }
}

data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]
columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df_input = pd.DataFrame(data, columns=columns)
input_file = read_files.get_input_path(2023,1)
df_input.to_parquet(
    path=input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)

def save_data(input_file):
    output_file = read_files.get_output_path(2023,1)
    df_output = batch.main(2023, 1, input_file, output_file)
    df_output.to_parquet(
        path=output_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )
save_data(input_file)

