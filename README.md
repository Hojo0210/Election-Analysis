# Election-Analysis
## Overview
An audit was performed on a Colorado congressional election to determine the winner of the election. While completing this election audit, additional data was needed to determine the largest voter turnout by county. This data needed to be written to a text file in order to generate the completed report.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.5, Visual Studio Code 1.56

## Election Audit Results
The results of this election audit determined that:
- 369,711 votes were cast in the election
- The county votes were:
  - Jefferson: 38,855 (10.5%)
  - Denver: 306,055 (82.8%)
  - Arapahoe: 24,801 (6.7%)
- Denver county had the most votes cast
- The votes for each candidate were:
  - Charles Casper Stockham: 85,213 (23.0%)
  - Diana DeGette: 272,892 (73.8%)
  - Raymond Anthone Doane: 11,606 (3.1%)
- The winner of the election was Diana DeGette, with 272,892 votes and 73.8% of the total votes.

## Election Audit Summary
This script could be used in any election with minor changes. By changing the read and write files, we can complete this audit for any election that fits this model. If we were trying to use this script for say a federal election, we would just have to alter the output language from county to state and add any varialbes that may be required for the results. 
