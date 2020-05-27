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


class PaymentServices(BaseModel):
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
    openapi_types = {"payment_services": "list[PaymentService]"}

    attribute_map = {"payment_services": "PaymentServices"}

    def __init__(self, payment_services=None):  # noqa: E501
        """PaymentServices - a model defined in OpenAPI"""  # noqa: E501

        self._payment_services = None
        self.discriminator = None

        if payment_services is not None:
            self.payment_services = payment_services

    @property
    def payment_services(self):
        """Gets the payment_services of this PaymentServices.  # noqa: E501


        :return: The payment_services of this PaymentServices.  # noqa: E501
        :rtype: list[PaymentService]
        """
        return self._payment_services

    @payment_services.setter
    def payment_services(self, payment_services):
        """Sets the payment_services of this PaymentServices.


        :param payment_services: The payment_services of this PaymentServices.  # noqa: E501
        :type: list[PaymentService]
        """

        self._payment_services = payment_services
