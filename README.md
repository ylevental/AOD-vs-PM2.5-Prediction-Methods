# Comparing Ensemble and Linear Methods for Predicting PM2.5 Levels from AOD Data
A major challenge involving pollution detection is to measure the average PM2.5 concentration over major metropolitan areas. One useful method for predicting PM2.5 over a relatively wide range are AOD measurements.  Ensemble algorithms are more effective than linear algorithms for prediction.  Pandas and scikit-learn were used for data analysis.

## Data Repository

The PM2.5 data for this project was sourced from the **[OpenAQ Project](https://openaq.org/)** (covering 2016-2019).  The raw data was originally stored in a `Reference.zip` file which was too large for the repository.  More specifically, the stations used were Addis Ababa: US Diplomatic Post (Central & School), and Los Angeles: Anaheim, Santa Clarita, Glendora, North-Main, Reseda, South Long Beach.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install scikit-learn before running.

```bash
pip3 install -U scikit-learn
```

## Usage

On line 13 of aodvspm25.py, add the folder names with the requested geographic locations for AOD and PM2.5 data.

```python
python3 aodvspm25.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
