import numpy as np

def calculate_percentiles(data, percentiles):
  """
  Calculates percentiles for a sequence or NumPy array.

  Args:
    data: A sequence or NumPy array of numerical values.
    percentiles: A list of percentiles to calculate (e.g., [50, 40, 90]).

  Returns:
    A dictionary containing the calculated percentiles.
  """

  # Convert data to a NumPy array if necessary
  data = np.array(data)

  # Ensure data is sorted
  data = np.sort(data)

  # Calculate percentiles using np.percentile
  percentiles_dict = {}
  for percentile in percentiles:
    percentiles_dict[percentile] = np.percentile(data, percentile)

  return percentiles_dict

# Sample data
data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

# Percentiles to calculate
percentiles = [50, 40, 90]

# Calculate and print percentiles
percentiles_dict = calculate_percentiles(data, percentiles)

for percentile, value in percentiles_dict.items():
  print(f"{percentile}th percentile (median): {value}")
