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


class TaxRate(BaseModel):
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
        "name": "str",
        "tax_type": "str",
        "tax_components": "list[TaxComponent]",
        "status": "str",
        "report_tax_type": "str",
        "can_apply_to_assets": "bool",
        "can_apply_to_equity": "bool",
        "can_apply_to_expenses": "bool",
        "can_apply_to_liabilities": "bool",
        "can_apply_to_revenue": "bool",
        "display_tax_rate": "float",
        "effective_rate": "float",
    }

    attribute_map = {
        "name": "Name",
        "tax_type": "TaxType",
        "tax_components": "TaxComponents",
        "status": "Status",
        "report_tax_type": "ReportTaxType",
        "can_apply_to_assets": "CanApplyToAssets",
        "can_apply_to_equity": "CanApplyToEquity",
        "can_apply_to_expenses": "CanApplyToExpenses",
        "can_apply_to_liabilities": "CanApplyToLiabilities",
        "can_apply_to_revenue": "CanApplyToRevenue",
        "display_tax_rate": "DisplayTaxRate",
        "effective_rate": "EffectiveRate",
    }

    def __init__(
        self,
        name=None,
        tax_type=None,
        tax_components=None,
        status=None,
        report_tax_type=None,
        can_apply_to_assets=None,
        can_apply_to_equity=None,
        can_apply_to_expenses=None,
        can_apply_to_liabilities=None,
        can_apply_to_revenue=None,
        display_tax_rate=None,
        effective_rate=None,
    ):  # noqa: E501
        """TaxRate - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._tax_type = None
        self._tax_components = None
        self._status = None
        self._report_tax_type = None
        self._can_apply_to_assets = None
        self._can_apply_to_equity = None
        self._can_apply_to_expenses = None
        self._can_apply_to_liabilities = None
        self._can_apply_to_revenue = None
        self._display_tax_rate = None
        self._effective_rate = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_components is not None:
            self.tax_components = tax_components
        if status is not None:
            self.status = status
        if report_tax_type is not None:
            self.report_tax_type = report_tax_type
        if can_apply_to_assets is not None:
            self.can_apply_to_assets = can_apply_to_assets
        if can_apply_to_equity is not None:
            self.can_apply_to_equity = can_apply_to_equity
        if can_apply_to_expenses is not None:
            self.can_apply_to_expenses = can_apply_to_expenses
        if can_apply_to_liabilities is not None:
            self.can_apply_to_liabilities = can_apply_to_liabilities
        if can_apply_to_revenue is not None:
            self.can_apply_to_revenue = can_apply_to_revenue
        if display_tax_rate is not None:
            self.display_tax_rate = display_tax_rate
        if effective_rate is not None:
            self.effective_rate = effective_rate

    @property
    def name(self):
        """Gets the name of this TaxRate.  # noqa: E501

        Name of tax rate  # noqa: E501

        :return: The name of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxRate.

        Name of tax rate  # noqa: E501

        :param name: The name of this TaxRate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tax_type(self):
        """Gets the tax_type of this TaxRate.  # noqa: E501

        The tax type  # noqa: E501

        :return: The tax_type of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this TaxRate.

        The tax type  # noqa: E501

        :param tax_type: The tax_type of this TaxRate.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

    @property
    def tax_components(self):
        """Gets the tax_components of this TaxRate.  # noqa: E501

        See TaxComponents  # noqa: E501

        :return: The tax_components of this TaxRate.  # noqa: E501
        :rtype: list[TaxComponent]
        """
        return self._tax_components

    @tax_components.setter
    def tax_components(self, tax_components):
        """Sets the tax_components of this TaxRate.

        See TaxComponents  # noqa: E501

        :param tax_components: The tax_components of this TaxRate.  # noqa: E501
        :type: list[TaxComponent]
        """

        self._tax_components = tax_components

    @property
    def status(self):
        """Gets the status of this TaxRate.  # noqa: E501

        See Status Codes  # noqa: E501

        :return: The status of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaxRate.

        See Status Codes  # noqa: E501

        :param status: The status of this TaxRate.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "ARCHIVED", "PENDING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def report_tax_type(self):
        """Gets the report_tax_type of this TaxRate.  # noqa: E501

        See ReportTaxTypes  # noqa: E501

        :return: The report_tax_type of this TaxRate.  # noqa: E501
        :rtype: str
        """
        return self._report_tax_type

    @report_tax_type.setter
    def report_tax_type(self, report_tax_type):
        """Sets the report_tax_type of this TaxRate.

        See ReportTaxTypes  # noqa: E501

        :param report_tax_type: The report_tax_type of this TaxRate.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "AVALARA",
            "BASEXCLUDED",
            "CAPITALSALESOUTPUT",
            "CAPITALEXPENSESINPUT",
            "ECOUTPUT",
            "ECOUTPUTSERVICES",
            "ECINPUT",
            "ECACQUISITIONS",
            "EXEMPTEXPENSES",
            "EXEMPTINPUT",
            "EXEMPTOUTPUT",
            "GSTONIMPORTS",
            "INPUT",
            "INPUTTAXED",
            "MOSSSALES",
            "NONE",
            "NONEOUTPUT",
            "OUTPUT",
            "PURCHASESINPUT",
            "SALESOUTPUT",
            "EXEMPTCAPITAL",
            "EXEMPTEXPORT",
            "CAPITALEXINPUT",
            "GSTONCAPIMPORTS",
            "GSTONCAPITALIMPORTS",
            "REVERSECHARGES",
            "PAYMENTS",
            "INVOICE",
            "CASH",
            "ACCRUAL",
            "FLATRATECASH",
            "FLATRATEACCRUAL",
            "ACCRUALS",
            "TXCA",
            "SRCAS",
            "DSOUTPUT",
            "BLINPUT2",
            "EPINPUT",
            "IMINPUT2",
            "MEINPUT",
            "IGDSINPUT2",
            "ESN33OUTPUT",
            "OPINPUT",
            "OSOUTPUT",
            "TXN33INPUT",
            "TXESSINPUT",
            "TXREINPUT",
            "TXPETINPUT",
            "NRINPUT",
            "ES33OUTPUT",
            "ZERORATEDINPUT",
            "ZERORATEDOUTPUT",
            "DRCHARGESUPPLY",
            "DRCHARGE",
        ]  # noqa: E501
        if report_tax_type not in allowed_values:
            raise ValueError(
                "Invalid value for `report_tax_type` ({0}), must be one of {1}".format(  # noqa: E501
                    report_tax_type, allowed_values
                )
            )

        self._report_tax_type = report_tax_type

    @property
    def can_apply_to_assets(self):
        """Gets the can_apply_to_assets of this TaxRate.  # noqa: E501

        Boolean to describe if tax rate can be used for asset accounts i.e.  true,false  # noqa: E501

        :return: The can_apply_to_assets of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_to_assets

    @can_apply_to_assets.setter
    def can_apply_to_assets(self, can_apply_to_assets):
        """Sets the can_apply_to_assets of this TaxRate.

        Boolean to describe if tax rate can be used for asset accounts i.e.  true,false  # noqa: E501

        :param can_apply_to_assets: The can_apply_to_assets of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._can_apply_to_assets = can_apply_to_assets

    @property
    def can_apply_to_equity(self):
        """Gets the can_apply_to_equity of this TaxRate.  # noqa: E501

        Boolean to describe if tax rate can be used for equity accounts i.e true,false  # noqa: E501

        :return: The can_apply_to_equity of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_to_equity

    @can_apply_to_equity.setter
    def can_apply_to_equity(self, can_apply_to_equity):
        """Sets the can_apply_to_equity of this TaxRate.

        Boolean to describe if tax rate can be used for equity accounts i.e true,false  # noqa: E501

        :param can_apply_to_equity: The can_apply_to_equity of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._can_apply_to_equity = can_apply_to_equity

    @property
    def can_apply_to_expenses(self):
        """Gets the can_apply_to_expenses of this TaxRate.  # noqa: E501

        Boolean to describe if tax rate can be used for expense accounts  i.e. true,false  # noqa: E501

        :return: The can_apply_to_expenses of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_to_expenses

    @can_apply_to_expenses.setter
    def can_apply_to_expenses(self, can_apply_to_expenses):
        """Sets the can_apply_to_expenses of this TaxRate.

        Boolean to describe if tax rate can be used for expense accounts  i.e. true,false  # noqa: E501

        :param can_apply_to_expenses: The can_apply_to_expenses of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._can_apply_to_expenses = can_apply_to_expenses

    @property
    def can_apply_to_liabilities(self):
        """Gets the can_apply_to_liabilities of this TaxRate.  # noqa: E501

        Boolean to describe if tax rate can be used for liability accounts  i.e. true,false  # noqa: E501

        :return: The can_apply_to_liabilities of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_to_liabilities

    @can_apply_to_liabilities.setter
    def can_apply_to_liabilities(self, can_apply_to_liabilities):
        """Sets the can_apply_to_liabilities of this TaxRate.

        Boolean to describe if tax rate can be used for liability accounts  i.e. true,false  # noqa: E501

        :param can_apply_to_liabilities: The can_apply_to_liabilities of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._can_apply_to_liabilities = can_apply_to_liabilities

    @property
    def can_apply_to_revenue(self):
        """Gets the can_apply_to_revenue of this TaxRate.  # noqa: E501

        Boolean to describe if tax rate can be used for revenue accounts i.e. true,false  # noqa: E501

        :return: The can_apply_to_revenue of this TaxRate.  # noqa: E501
        :rtype: bool
        """
        return self._can_apply_to_revenue

    @can_apply_to_revenue.setter
    def can_apply_to_revenue(self, can_apply_to_revenue):
        """Sets the can_apply_to_revenue of this TaxRate.

        Boolean to describe if tax rate can be used for revenue accounts i.e. true,false  # noqa: E501

        :param can_apply_to_revenue: The can_apply_to_revenue of this TaxRate.  # noqa: E501
        :type: bool
        """

        self._can_apply_to_revenue = can_apply_to_revenue

    @property
    def display_tax_rate(self):
        """Gets the display_tax_rate of this TaxRate.  # noqa: E501

        Tax Rate (decimal to 4dp) e.g 12.5000  # noqa: E501

        :return: The display_tax_rate of this TaxRate.  # noqa: E501
        :rtype: float
        """
        return self._display_tax_rate

    @display_tax_rate.setter
    def display_tax_rate(self, display_tax_rate):
        """Sets the display_tax_rate of this TaxRate.

        Tax Rate (decimal to 4dp) e.g 12.5000  # noqa: E501

        :param display_tax_rate: The display_tax_rate of this TaxRate.  # noqa: E501
        :type: float
        """

        self._display_tax_rate = display_tax_rate

    @property
    def effective_rate(self):
        """Gets the effective_rate of this TaxRate.  # noqa: E501

        Effective Tax Rate (decimal to 4dp) e.g 12.5000  # noqa: E501

        :return: The effective_rate of this TaxRate.  # noqa: E501
        :rtype: float
        """
        return self._effective_rate

    @effective_rate.setter
    def effective_rate(self, effective_rate):
        """Sets the effective_rate of this TaxRate.

        Effective Tax Rate (decimal to 4dp) e.g 12.5000  # noqa: E501

        :param effective_rate: The effective_rate of this TaxRate.  # noqa: E501
        :type: float
        """

        self._effective_rate = effective_rate
