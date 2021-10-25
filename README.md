# Amazon price tracker

Tracking the price of a product on Amazon and Emailing to the user
when the price is lower than the defined target price

## Installation

Install all the required packages from the requirements.txt

```bash
pip install -r requirements.txt
```

Rename the .env.example file to .env and change the values

```bash
 cp .env.example .env
```

## Usage

Fill/change all the required values in the .env file

```python
# Your Email password
PASSWORD=""
# Your Email address
MY_EMAIL="example@gmail.com"
# Target Email address to where the information about the product proce will be sent
TARGET_EMAIL="example@gmail.com"
# The link to the product on Amazon
PRODUCT_URL="https://www.amazon.com/Chloe-Nomade-Parfum-Spray-Women/dp/B07F8FJ7ND/ref=sr_1_11?dchild=1&keywords=chloe+perfume&qid=1632157335&sr=8-11"
# Your desired price for the product
TARGET_PRICE=80

```

