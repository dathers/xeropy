# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PaidLeaveEarningsLine(BaseModel):
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
        "leave_type_id": "str",
        "amount": "float",
        "sgc_applied_leave_loading_amount": "float",
        "sgc_exempted_leave_loading_amount": "float",
        "reset_stp_categorisation": "bool",
    }

    attribute_map = {
        "leave_type_id": "LeaveTypeID",
        "amount": "Amount",
        "sgc_applied_leave_loading_amount": "SGCAppliedLeaveLoadingAmount",
        "sgc_exempted_leave_loading_amount": "SGCExemptedLeaveLoadingAmount",
        "reset_stp_categorisation": "ResetSTPCategorisation",
    }

    def __init__(
        self,
        leave_type_id=None,
        amount=None,
        sgc_applied_leave_loading_amount=None,
        sgc_exempted_leave_loading_amount=None,
        reset_stp_categorisation=None,
    ):  # noqa: E501
        """PaidLeaveEarningsLine - a model defined in OpenAPI"""  # noqa: E501

        self._leave_type_id = None
        self._amount = None
        self._sgc_applied_leave_loading_amount = None
        self._sgc_exempted_leave_loading_amount = None
        self._reset_stp_categorisation = None
        self.discriminator = None

        self.leave_type_id = leave_type_id
        self.amount = amount
        if sgc_applied_leave_loading_amount is not None:
            self.sgc_applied_leave_loading_amount = sgc_applied_leave_loading_amount
        if sgc_exempted_leave_loading_amount is not None:
            self.sgc_exempted_leave_loading_amount = sgc_exempted_leave_loading_amount
        if reset_stp_categorisation is not None:
            self.reset_stp_categorisation = reset_stp_categorisation

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this PaidLeaveEarningsLine.  # noqa: E501

        Xero leave type identifier  # noqa: E501

        :return: The leave_type_id of this PaidLeaveEarningsLine.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this PaidLeaveEarningsLine.

        Xero leave type identifier  # noqa: E501

        :param leave_type_id: The leave_type_id of this PaidLeaveEarningsLine.  # noqa: E501
        :type: str
        """
        if leave_type_id is None:
            raise ValueError(
                "Invalid value for `leave_type_id`, must not be `None`"
            )  # noqa: E501

        self._leave_type_id = leave_type_id

    @property
    def amount(self):
        """Gets the amount of this PaidLeaveEarningsLine.  # noqa: E501

        Paid leave amount  # noqa: E501

        :return: The amount of this PaidLeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaidLeaveEarningsLine.

        Paid leave amount  # noqa: E501

        :param amount: The amount of this PaidLeaveEarningsLine.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def sgc_applied_leave_loading_amount(self):
        """Gets the sgc_applied_leave_loading_amount of this PaidLeaveEarningsLine.  # noqa: E501

        The amount of leave loading applied for the leave type that is subject to Superannuation Guarantee Contributions. *Only applicable for Leave Types with Annual Leave Categories  # noqa: E501

        :return: The sgc_applied_leave_loading_amount of this PaidLeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._sgc_applied_leave_loading_amount

    @sgc_applied_leave_loading_amount.setter
    def sgc_applied_leave_loading_amount(self, sgc_applied_leave_loading_amount):
        """Sets the sgc_applied_leave_loading_amount of this PaidLeaveEarningsLine.

        The amount of leave loading applied for the leave type that is subject to Superannuation Guarantee Contributions. *Only applicable for Leave Types with Annual Leave Categories  # noqa: E501

        :param sgc_applied_leave_loading_amount: The sgc_applied_leave_loading_amount of this PaidLeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._sgc_applied_leave_loading_amount = sgc_applied_leave_loading_amount

    @property
    def sgc_exempted_leave_loading_amount(self):
        """Gets the sgc_exempted_leave_loading_amount of this PaidLeaveEarningsLine.  # noqa: E501

        The amount of leave loading applied for the leave type that is exempt from Superannuation Guarantee Contributions. *Only applicable for Leave Types with Annual Leave Categories  # noqa: E501

        :return: The sgc_exempted_leave_loading_amount of this PaidLeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._sgc_exempted_leave_loading_amount

    @sgc_exempted_leave_loading_amount.setter
    def sgc_exempted_leave_loading_amount(self, sgc_exempted_leave_loading_amount):
        """Sets the sgc_exempted_leave_loading_amount of this PaidLeaveEarningsLine.

        The amount of leave loading applied for the leave type that is exempt from Superannuation Guarantee Contributions. *Only applicable for Leave Types with Annual Leave Categories  # noqa: E501

        :param sgc_exempted_leave_loading_amount: The sgc_exempted_leave_loading_amount of this PaidLeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._sgc_exempted_leave_loading_amount = sgc_exempted_leave_loading_amount

    @property
    def reset_stp_categorisation(self):
        """Gets the reset_stp_categorisation of this PaidLeaveEarningsLine.  # noqa: E501

        Reset the STP categorisations for the leave type. *Only applicable for Leave Types with Annual Leave Categories  # noqa: E501

        :return: The reset_stp_categorisation of this PaidLeaveEarningsLine.  # noqa: E501
        :rtype: bool
        """
        return self._reset_stp_categorisation

    @reset_stp_categorisation.setter
    def reset_stp_categorisation(self, reset_stp_categorisation):
        """Sets the reset_stp_categorisation of this PaidLeaveEarningsLine.

        Reset the STP categorisations for the leave type. *Only applicable for Leave Types with Annual Leave Categories  # noqa: E501

        :param reset_stp_categorisation: The reset_stp_categorisation of this PaidLeaveEarningsLine.  # noqa: E501
        :type: bool
        """

        self._reset_stp_categorisation = reset_stp_categorisation