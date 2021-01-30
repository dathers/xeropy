# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperannuationLine(BaseModel):
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
        "superannuation_type_id": "str",
        "display_name": "str",
        "amount": "float",
        "fixed_amount": "float",
        "percentage": "float",
        "manual_adjustment": "bool",
    }

    attribute_map = {
        "superannuation_type_id": "superannuationTypeID",
        "display_name": "displayName",
        "amount": "amount",
        "fixed_amount": "fixedAmount",
        "percentage": "percentage",
        "manual_adjustment": "manualAdjustment",
    }

    def __init__(
        self,
        superannuation_type_id=None,
        display_name=None,
        amount=None,
        fixed_amount=None,
        percentage=None,
        manual_adjustment=None,
    ):  # noqa: E501
        """SuperannuationLine - a model defined in OpenAPI"""  # noqa: E501

        self._superannuation_type_id = None
        self._display_name = None
        self._amount = None
        self._fixed_amount = None
        self._percentage = None
        self._manual_adjustment = None
        self.discriminator = None

        if superannuation_type_id is not None:
            self.superannuation_type_id = superannuation_type_id
        if display_name is not None:
            self.display_name = display_name
        if amount is not None:
            self.amount = amount
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if percentage is not None:
            self.percentage = percentage
        if manual_adjustment is not None:
            self.manual_adjustment = manual_adjustment

    @property
    def superannuation_type_id(self):
        """Gets the superannuation_type_id of this SuperannuationLine.  # noqa: E501

        Xero identifier for payroll superannucation type  # noqa: E501

        :return: The superannuation_type_id of this SuperannuationLine.  # noqa: E501
        :rtype: str
        """
        return self._superannuation_type_id

    @superannuation_type_id.setter
    def superannuation_type_id(self, superannuation_type_id):
        """Sets the superannuation_type_id of this SuperannuationLine.

        Xero identifier for payroll superannucation type  # noqa: E501

        :param superannuation_type_id: The superannuation_type_id of this SuperannuationLine.  # noqa: E501
        :type: str
        """

        self._superannuation_type_id = superannuation_type_id

    @property
    def display_name(self):
        """Gets the display_name of this SuperannuationLine.  # noqa: E501

        Benefit display name  # noqa: E501

        :return: The display_name of this SuperannuationLine.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SuperannuationLine.

        Benefit display name  # noqa: E501

        :param display_name: The display_name of this SuperannuationLine.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def amount(self):
        """Gets the amount of this SuperannuationLine.  # noqa: E501

        The amount of the superannuation line  # noqa: E501

        :return: The amount of this SuperannuationLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SuperannuationLine.

        The amount of the superannuation line  # noqa: E501

        :param amount: The amount of this SuperannuationLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this SuperannuationLine.  # noqa: E501

        Superannuation fixed amount  # noqa: E501

        :return: The fixed_amount of this SuperannuationLine.  # noqa: E501
        :rtype: float
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this SuperannuationLine.

        Superannuation fixed amount  # noqa: E501

        :param fixed_amount: The fixed_amount of this SuperannuationLine.  # noqa: E501
        :type: float
        """

        self._fixed_amount = fixed_amount

    @property
    def percentage(self):
        """Gets the percentage of this SuperannuationLine.  # noqa: E501

        Superannuation rate percentage  # noqa: E501

        :return: The percentage of this SuperannuationLine.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this SuperannuationLine.

        Superannuation rate percentage  # noqa: E501

        :param percentage: The percentage of this SuperannuationLine.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def manual_adjustment(self):
        """Gets the manual_adjustment of this SuperannuationLine.  # noqa: E501

        manual adjustment made  # noqa: E501

        :return: The manual_adjustment of this SuperannuationLine.  # noqa: E501
        :rtype: bool
        """
        return self._manual_adjustment

    @manual_adjustment.setter
    def manual_adjustment(self, manual_adjustment):
        """Sets the manual_adjustment of this SuperannuationLine.

        manual adjustment made  # noqa: E501

        :param manual_adjustment: The manual_adjustment of this SuperannuationLine.  # noqa: E501
        :type: bool
        """

        self._manual_adjustment = manual_adjustment