# Transform
# Language: Python
# Input: CSV (abundances)
# Output: CSV (shifted abundances)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin that can take a CSV file of abundances and execute
the algorithm of (Egozcue and Pawlowski-Glahn, 2016) to shift their values.
This method was used by PhiLR (Silverman et al, 2017) for a pre-proceessing step in place of
typical normalization.

The input CSV file is assumed to contain rows representing samples and 
columns representing entities, with entry (i, j) the abundance of entry j in sample i.
The output CSV file has the same format, but contains the shifted composition.
Division is done by the Euclidean and geometric means, plus the sum of each row.
