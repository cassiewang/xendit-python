# Xendit Python Library

This library is the abstraction of Xendit API for access from applications written with Python.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Xendit Python Library](#xendit-python-library)
  - [Table of Contents](#table-of-contents)
  - [API Documentation](#api-documentation)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [API Key](#api-key)
      - [Global Variable](#global-variable)
      - [Use Xendit Instance](#use-xendit-instance)
    - [Headers](#headers)
    - [Balance Service](#balance-service)
      - [Get Balance](#get-balance)
    - [eWallets](#ewallets)
      - [Create OVO Payment](#create-ovo-payment)
      - [Create DANA Payment](#create-dana-payment)
      - [Create LinkAja Payment](#create-linkaja-payment)
      - [Get Payment Status](#get-payment-status)
    - [Virtual Account Service](#virtual-account-service)
      - [Create Virtual Account](#create-virtual-account)
      - [Get Virtual Account Banks](#get-virtual-account-banks)
      - [Get Virtual Account](#get-virtual-account)
      - [Update Virtual Account](#update-virtual-account)
      - [Get Virtual Account Payment](#get-virtual-account-payment)
    - [Retail Outlet Service](#retail-outlet-service)
      - [Create Fixed Payment Code](#create-fixed-payment-code)
      - [Update Fixed Payment Code](#update-fixed-payment-code)
      - [Get Fixed Payment Code](#get-fixed-payment-code)
    - [Disbursement Service](#disbursement-service)
      - [Create Disbursement](#create-disbursement)
      - [Get Disbursement by ID](#get-disbursement-by-id)
      - [Get Disbursement by External ID](#get-disbursement-by-external-id)
      - [Get Available Banks](#get-available-banks)
  - [Contributing](#contributing)
    - [Tests](#tests)
      - [Running the Test](#running-the-test)
      - [Creating Custom HTTP Client](#creating-custom-http-client)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## API Documentation
Please check [Xendit API Reference](https://xendit.github.io/apireference/).

## Requirements

Python 3.7 or later

## Installation

To use the package, run ```pip install xendit-python```

## Usage

### API Key

To add API Key, you have 2 option: Use global variable or use Xendit instance

#### Global Variable

```python
import xendit
xendit.api_key = "test-key123"

# Then just run each class as static
from xendit import Balance
Balance.get()
```

#### Use Xendit Instance
```python
import xendit
x = xendit.Xendit(api_key="test-key123")

# Then access each class from x attribute
Balance = x.Balance
Balance.get()
```

### Headers

You can add headers by using the following keyword parameters
- X-IDEMPOTENCY-KEY: `x_idempotency_key`

```
VirtualAccount.create(x_idempotency_key="your-idemp-key")
```

- for-user-id: `for_user_id`

```
Balance.get(for_user_id='subaccount-user-id')
```

- X-API-VERSION: `x_api_version`

```
Balance.get(x_api_version='2020-01-01')
```

### Balance Service

#### Get Balance

The `account_type` parameter is optional.

```python
from xendit import Balance
Balance.get()

Balance.get(Balance.AccountType)
```

Usage example:

```python
from xendit import Balance
Balance balance = Balance.get(Balance.AccountType.CASH)

# To get the JSON view
print(balance)

# To get only the value
print(balance.balance)
``` 

Will return

```
{'balance': 1000000000}
1000000000
```

### eWallets

#### Create OVO Payment

```python
from xendit import EWallet

ovo_payment = EWallet.create_ovo_payment("ovo-ewallet-testing-id-1593583779", "80001", "08123123123")
print(ovo_payment)
```

Will return

```
{
    "amount": 80001,
    "business_id": "5ed75086a883856178afc12e",
    "external_id": "ovo-ewallet-testing-id-1593583779",
    "ewallet_type": "OVO",
    "phone": "08123123123",
    "created": "2020-07-01T06:09:47.610Z",
    "status": "PENDING"
}
```

#### Create DANA Payment

```python
from xendit import EWallet

dana_payment = EWallet.create_dana_payment("dana-ewallet-test-1593583817", "1001", "https://my-shop.com/callbacks", "https://my-shop.com/home")
print(dana_payment)
```

Will return

```
{
    "external_id": "dana-ewallet-test-1593583817",
    "amount": 1001,
    "checkout_url": "https://sandbox.m.dana.id/m/portal/cashier/checkout?bizNo=20200701111212800110166367100513589&timestamp=1593583818552&mid=216620000000261692328&sign=a0WQ2g2PktDQ1oZdO4dzLUIIcD%2FhakqLIVo6Z8D87WNPwfV5JKEeZT%2F7XmR50XUrvKSDwJQMpfdAPi2UYbuV2Cqwxy494FDp%2BVyz69gvQ5R7SyQSxyeqfpy6%2ByE7OFPtJTHu%2BzDtD95DVNssSfz0GmUvBO4ykF3Rwu8qbLP2nchvh7URslKH9cmtisE%2BXfBcP45UyeQndDDG4DdF16d%2FeR2C8uPhS5thMt1mDZKRsw41QZS4gZ%2BSjhvpCWfkfLoUVOymtzE3Q7KuC%2FzLxsI5Kd7BnxE3GhkKbOw7dNpacqfctXpGGO08jNwrdqsptUKYnF87bzX8kUAEvJif6Hu9Gw%3D%3D",
    "ewallet_type": "DANA"
}
```

#### Create LinkAja Payment

```python
from xendit import EWallet, LinkAjaItem

items = []
items.append(LinkAjaItem(id="123123", name="Phone Case", price=100000, quantity=1))
linkaja_payment = EWallet.create_linkaja_payment("linkaja-ewallet-test-1593583880", "089911111111", 300000, items, "https://my-shop.com/callbacks", "https://xendit.co/")
print(linkaja_payment)
```

Will return

```
{
    "checkout_url": "https://ewallet-linkaja-dev.xendit.co/checkouts/c631e9a1-b460-4f22-98a2-b481e6feda10",
    "transaction_date": "2020-07-01T06:11:22.335Z",
    "amount": 300000,
    "external_id": "linkaja-ewallet-test-1593583880",
    "ewallet_type": "LINKAJA"
}
```

#### Get Payment Status

```python
from xendit import EWallet

ovo_payment_status = EWallet.get_payment_status('ovo-ewallet-testing-id-1234', EWalletType.OVO)
print(ovo_payment_status)
```

Will return

```
{
    "amount": "8888",
    "business_id": "5ed75086a883856178afc12e",
    "ewallet_type": "OVO",
    "external_id": "ovo-ewallet-testing-id-1234",
    "status": "COMPLETED",
    "transaction_date": "2020-06-30T01:32:28.267Z"
}
```

### Virtual Account Service

#### Create Virtual Account

```python
from xendit import VirtualAccount

virtual_account = VirtualAccount.create("demo_1475459775872", "BNI", "Rika Sutanto")
print(virtual_account)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "bank_code": "BNI",
    "merchant_code": "8808",
    "name": "Rika Sutanto",
    "account_number": "8808999956275653",
    "is_single_use": false,
    "status": "PENDING",
    "expiration_date": "2051-06-22T17:00:00.000Z",
    "is_closed": false,
    "id": "5ef174c48dd9ea2fc97d6a1e"
}
```

#### Get Virtual Account Banks
```python
from xendit import VirtualAccount

virtual_account_banks = VirtualAccount.get_banks()
print(virtual_account_banks)
```

Will return

```
[{
    "name": "Bank Mandiri",
    "code": "MANDIRI"
}, {
    "name": "Bank Negara Indonesia",
    "code": "BNI"
}, {
    "name": "Bank Rakyat Indonesia",
    "code": "BRI"
}, {
    "name": "Bank Permata",
    "code": "PERMATA"
}, {
    "name": "Bank Central Asia",
    "code": "BCA"
}]
```
#### Get Virtual Account

```python
from xendit import VirtualAccount

virtual_account = VirtualAccount.get("5eec3a3e8dd9ea2fc97d6728")
print(virtual_account)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "bank_code": "BNI",
    "merchant_code": "8808",
    "name": "Rika Sutanto",
    "account_number": "8808999917965673",
    "is_single_use": true,
    "status": "ACTIVE",
    "expiration_date": "2051-06-18T17:00:00.000Z",
    "is_closed": false,
    "id": "5eec3a3e8dd9ea2fc97d6728"
}
```

#### Update Virtual Account

```python
from xendit import VirtualAccount

virtual_account = VirtualAccount.update("5eec3a3e8dd9ea2fc97d6728", is_single_use=True)
print(virtual_account)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "bank_code": "BNI",
    "merchant_code": "8808",
    "name": "Rika Sutanto",
    "account_number": "8808999917965673",
    "is_single_use": true,
    "status": "PENDING",
    "expiration_date": "2051-06-18T17:00:00.000Z",
    "is_closed": false,
    "id": "5eec3a3e8dd9ea2fc97d6728"
}
```

#### Get Virtual Account Payment

```python
from xendit import VirtualAccount

virtual_account_payment = VirtualAccount.get_payment("5ef18efca7d10d1b4d61fb52")
print(virtual_account)
```

Will return

```
{
    "id": "5ef18efcf9ce3b5f8e188ee4",
    "payment_id": "5ef18efca7d10d1b4d61fb52",
    "callback_virtual_account_id": "5ef18ece8dd9ea2fc97d6a84",
    "external_id": "VA_fixed-1592889038",
    "merchant_code": "88608",
    "account_number": "9999317837",
    "bank_code": "MANDIRI",
    "amount": 50000,
    "transaction_timestamp": "2020-06-23T05:11:24.000Z"
}
```

### Retail Outlet Service

#### Create Fixed Payment Code

```python
from xendit import RetailOutlet

retail_outlet = RetailOutlet.create_fixed_payment_code(
    "demo_fixed_payment_code_123", "ALFAMART", "Rika Sutanto", 10000
)
print(retail_outlet)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_fixed_payment_code_123",
    "retail_outlet_name": "ALFAMART",
    "prefix": "TEST",
    "name": "Rika Sutanto",
    "payment_code": "TEST56147",
    "expected_amount": 10000,
    "is_single_use": False,
    "expiration_date": "2051-06-23T17:00:00.000Z",
    "id": "5ef2f0f8e7f5c14077275493",
}
```

#### Update Fixed Payment Code

```python
from xendit import RetailOutlet

retail_outlet = RetailOutlet.update_fixed_payment_code(
    "5ef2f0f8e7f5c14077275493", name="Joe Contini"
)
print(retail_outlet)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_fixed_payment_code_123",
    "retail_outlet_name": "ALFAMART",
    "prefix": "TEST",
    "name": "Joe Contini",
    "payment_code": "TEST56147",
    "expected_amount": 10000,
    "is_single_use": False,
    "expiration_date": "2051-06-23T17:00:00.000Z",
    "id": "5ef2f0f8e7f5c14077275493",
}
```

#### Get Fixed Payment Code

```python
from xendit import RetailOutlet

retail_outlet = RetailOutlet.get_fixed_payment_code("5ef2f0f8e7f5c14077275493")
print(retail_outlet)
```

Will return

```
{
    "owner_id": "5ed75086a883856178afc12e",
    "external_id": "demo_fixed_payment_code_123",
    "retail_outlet_name": "ALFAMART",
    "prefix": "TEST",
    "name": "Rika Sutanto",
    "payment_code": "TEST56147",
    "expected_amount": 10000,
    "is_single_use": False,
    "expiration_date": "2051-06-23T17:00:00.000Z",
    "id": "5ef2f0f8e7f5c14077275493",
}
```

### Disbursement Service

#### Create Disbursement

```python
from xendit import Disbursement

disbursement = Disbursement.create(
    external_id="demo_1475459775872",
    bank_code="BCA",
    account_holder_name="Bob Jones",
    account_number="1231242311",
    description="Reimbursement for shoes",
    amount=17000,
)
print(disbursement)
```

Will return

```
{
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "amount": 17000,
    "bank_code": "BCA",
    "account_holder_name": "Bob Jones",
    "disbursement_description": "Reimbursement for shoes",
    "status": "PENDING",
    "id": "5ef1c4f40c2e150017ce3b96",
}
```

#### Get Disbursement by ID

```python
from xendit import Disbursement

disbursement = Disbursement.get("5ef1befeecb16100179e1d05")
print(disbursement)
```

Will return

```
{
    "user_id": "5ed75086a883856178afc12e",
    "external_id": "demo_1475459775872",
    "amount": 17000,
    "bank_code": "BCA",
    "account_holder_name": "Bob Jones",
    "disbursement_description": "Disbursement from Postman",
    "status": "PENDING",
    "id": "5ef1befeecb16100179e1d05"
}
```

#### Get Disbursement by External ID

```python
from xendit import Disbursement

disbursement_list = Disbursement.get_by_ext_id("demo_1475459775872")
print(disbursement_list)

```

Will return

```
[
    {
        "user_id": "5ed75086a883856178afc12e",
        "external_id": "demo_1475459775872",
        "amount": 17000,
        "bank_code": "BCA",
        "account_holder_name": "Bob Jones",
        "disbursement_description": "Reimbursement for shoes",
        "status": "PENDING",
        "id": "5ef1c4f40c2e150017ce3b96",
    },
    {
        "user_id": "5ed75086a883856178afc12e",
        "external_id": "demo_1475459775872",
        "amount": 17000,
        "bank_code": "BCA",
        "account_holder_name": "Bob Jones",
        "disbursement_description": "Disbursement from Postman",
        "status": "PENDING",
        "id": "5ef1befeecb16100179e1d05",
    },
    ...
]
```
#### Get Available Banks

```python
from xendit import Disbursement

disbursement_banks = Disbursement.get_available_banks()
print(disbursement_banks)
```

Will return

```
[
    ...
    {
        "name": "Mandiri Taspen Pos (formerly Bank Sinar Harapan Bali)",
        "code": "MANDIRI_TASPEN",
        "can_disburse": True,
        "can_name_validate": True,
    },
    {
        "name": "Bank QNB Indonesia (formerly Bank QNB Kesawan)",
        "code": "QNB_INDONESIA",
        "can_disburse": True,
        "can_name_validate": True,
    }
]
```
## Contributing

For any requests, bugs, or comments, please open an [issue](https://github.com/xendit/xendit-python/issues) or [submit a pull request](https://github.com/xendit/xendit-python/pulls).

To start developing on this repository, you need to have Poetry installed for package dependency. After that, you can run ```poetry install``` to install the dependency. To enter the environment, run ```poetry shell```

### Tests

#### Running the Test

Make sure the the code passes all tests.

Run the test:

```
python -m pytest tests/
```

Run with coverage:

```
python -m pytest tests/ --cov=xendit/
```

#### Creating Custom HTTP Client

To create your own HTTP Client, you can do it by implementing interface at `xendit/network/http_client_interface.py`. Our default HTTP Client are wrapper of [requests](https://github.com/psf/requests), which can be found at `xendit/network/_xendit_http_client.py`. To attach it to your instance, add it to your xendit parameter.

```python
import xendit

xendit_instance =  xendit.Xendit(api_key='', http_client=YourHTTPClientClass)
```
