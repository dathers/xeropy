# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BankAccount(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "statement_text": "str",
        "account_name": "str",
        "bsb": "str",
        "account_number": "str",
        "remainder": "bool",
        "amount": "float",
    }

    attribute_map = {
        "statement_text": "StatementText",
        "account_name": "AccountName",
        "bsb": "BSB",
        "account_number": "AccountNumber",
        "remainder": "Remainder",
        "amount": "Amount",
    }

    def __init__(
        self,
        statement_text=None,
        account_name=None,
        bsb=None,
        account_number=None,
        remainder=None,
        amount=None,
    ):  # noqa: E501
        """BankAccount - a model defined in OpenAPI"""  # noqa: E501

        self._statement_text = None
        self._account_name = None
        self._bsb = None
        self._account_number = None
        self._remainder = None
        self._amount = None
        self.discriminator = None

        if statement_text is not None:
            self.statement_text = statement_text
        if account_name is not None:
            self.account_name = account_name
        if bsb is not None:
            self.bsb = bsb
        if account_number is not None:
            self.account_number = account_number
        if remainder is not None:
            self.remainder = remainder
        if amount is not None:
            self.amount = amount

    @property
    def statement_text(self):
        """Gets the statement_text of this BankAccount.  # noqa: E501

        The text that will appear on your employee's bank statement when they receive payment  # noqa: E501

        :return: The statement_text of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._statement_text

    @statement_text.setter
    def statement_text(self, statement_text):
        """Sets the statement_text of this BankAccount.

        The text that will appear on your employee's bank statement when they receive payment  # noqa: E501

        :param statement_text: The statement_text of this BankAccount.  # noqa: E501
        :type: str
        """

        self._statement_text = statement_text

    @property
    def account_name(self):
        """Gets the account_name of this BankAccount.  # noqa: E501

        The name of the account  # noqa: E501

        :return: The account_name of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this BankAccount.

        The name of the account  # noqa: E501

        :param account_name: The account_name of this BankAccount.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def bsb(self):
        """Gets the bsb of this BankAccount.  # noqa: E501

        The BSB number of the account  # noqa: E501

        :return: The bsb of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._bsb

    @bsb.setter
    def bsb(self, bsb):
        """Sets the bsb of this BankAccount.

        The BSB number of the account  # noqa: E501

        :param bsb: The bsb of this BankAccount.  # noqa: E501
        :type: str
        """

        self._bsb = bsb

    @property
    def account_number(self):
        """Gets the account_number of this BankAccount.  # noqa: E501

        The account number  # noqa: E501

        :return: The account_number of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BankAccount.

        The account number  # noqa: E501

        :param account_number: The account_number of this BankAccount.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def remainder(self):
        """Gets the remainder of this BankAccount.  # noqa: E501

        If this account is the Remaining bank account  # noqa: E501

        :return: The remainder of this BankAccount.  # noqa: E501
        :rtype: bool
        """
        return self._remainder

    @remainder.setter
    def remainder(self, remainder):
        """Sets the remainder of this BankAccount.

        If this account is the Remaining bank account  # noqa: E501

        :param remainder: The remainder of this BankAccount.  # noqa: E501
        :type: bool
        """

        self._remainder = remainder

    @property
    def amount(self):
        """Gets the amount of this BankAccount.  # noqa: E501

        Fixed amounts (for example, if an employee wants to have $100 of their salary transferred to one account, and the remaining amount to another)  # noqa: E501

        :return: The amount of this BankAccount.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BankAccount.

        Fixed amounts (for example, if an employee wants to have $100 of their salary transferred to one account, and the remaining amount to another)  # noqa: E501

        :param amount: The amount of this BankAccount.  # noqa: E501
        :type: float
        """

        self._amount = amount
