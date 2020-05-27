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


class ManualJournals(BaseModel):
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
    openapi_types = {"manual_journals": "list[ManualJournal]"}

    attribute_map = {"manual_journals": "ManualJournals"}

    def __init__(self, manual_journals=None):  # noqa: E501
        """ManualJournals - a model defined in OpenAPI"""  # noqa: E501

        self._manual_journals = None
        self.discriminator = None

        if manual_journals is not None:
            self.manual_journals = manual_journals

    @property
    def manual_journals(self):
        """Gets the manual_journals of this ManualJournals.  # noqa: E501


        :return: The manual_journals of this ManualJournals.  # noqa: E501
        :rtype: list[ManualJournal]
        """
        return self._manual_journals

    @manual_journals.setter
    def manual_journals(self, manual_journals):
        """Sets the manual_journals of this ManualJournals.


        :param manual_journals: The manual_journals of this ManualJournals.  # noqa: E501
        :type: list[ManualJournal]
        """

        self._manual_journals = manual_journals
