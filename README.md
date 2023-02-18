
![GitHub contributors](https://img.shields.io/github/contributors/BroaderImpact/ml-model-selection) ![GitHub forks](https://img.shields.io/github/forks/BroaderImpact/ml-model-selection?style=social)

# ml-model-selection

Easy python script for determining which machine learning model to use.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `select_model`.

```bash
pip install select_model
```

## Usage

```python
import select_model

# returns 'Linear Regression is recommended.'
select_model.linear('yes')

# returns 'Random Forest Classifier is recommended.'
select_model.classification('yes')

# returns 'Logistic Regression is recommended.'
select_model.binary('yes')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
