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


class BankTransfers(BaseModel):
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
    openapi_types = {"bank_transfers": "list[BankTransfer]"}

    attribute_map = {"bank_transfers": "BankTransfers"}

    def __init__(self, bank_transfers=None):  # noqa: E501
        """BankTransfers - a model defined in OpenAPI"""  # noqa: E501

        self._bank_transfers = None
        self.discriminator = None

        if bank_transfers is not None:
            self.bank_transfers = bank_transfers

    @property
    def bank_transfers(self):
        """Gets the bank_transfers of this BankTransfers.  # noqa: E501


        :return: The bank_transfers of this BankTransfers.  # noqa: E501
        :rtype: list[BankTransfer]
        """
        return self._bank_transfers

    @bank_transfers.setter
    def bank_transfers(self, bank_transfers):
        """Sets the bank_transfers of this BankTransfers.


        :param bank_transfers: The bank_transfers of this BankTransfers.  # noqa: E501
        :type: list[BankTransfer]
        """

        self._bank_transfers = bank_transfers
