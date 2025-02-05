import matplotlib.pyplot as plt
import pandas as pd

# Plot extra-vehicular activity (eva) of nasa over time

def read_json_to_df(input_file):
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)  # float needed for calculations
    eva_df.dropna(axis=0, inplace=True)  # drop missing values
    eva_df.sort_values('date', inplace=True)  # sort data by date to calculate cumulative eva
    return eva_df

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

eva_df = read_json_to_df(input_file) # read in eva JSON to pandas df

eva_df.to_csv(output_file, index=False)  # save data without headers

eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60) # convert duration in hours as float
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum() 
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-') # plot 
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()