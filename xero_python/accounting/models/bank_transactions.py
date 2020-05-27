# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.1.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BankTransactions(BaseModel):
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
    openapi_types = {"bank_transactions": "list[BankTransaction]"}

    attribute_map = {"bank_transactions": "BankTransactions"}

    def __init__(self, bank_transactions=None):  # noqa: E501
        """BankTransactions - a model defined in OpenAPI"""  # noqa: E501

        self._bank_transactions = None
        self.discriminator = None

        if bank_transactions is not None:
            self.bank_transactions = bank_transactions

    @property
    def bank_transactions(self):
        """Gets the bank_transactions of this BankTransactions.  # noqa: E501


        :return: The bank_transactions of this BankTransactions.  # noqa: E501
        :rtype: list[BankTransaction]
        """
        return self._bank_transactions

    @bank_transactions.setter
    def bank_transactions(self, bank_transactions):
        """Sets the bank_transactions of this BankTransactions.


        :param bank_transactions: The bank_transactions of this BankTransactions.  # noqa: E501
        :type: list[BankTransaction]
        """

        self._bank_transactions = bank_transactions
