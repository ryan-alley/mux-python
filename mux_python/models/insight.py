# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Insight(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total_watch_time': 'int',
        'total_views': 'int',
        'total_row_count': 'int',
        'negative_impact_score': 'int',
        'metric': 'int',
        'filter_value': 'str',
        'filter_column': 'str'
    }

    attribute_map = {
        'total_watch_time': 'total_watch_time',
        'total_views': 'total_views',
        'total_row_count': 'total_row_count',
        'negative_impact_score': 'negative_impact_score',
        'metric': 'metric',
        'filter_value': 'filter_value',
        'filter_column': 'filter_column'
    }

    def __init__(self, total_watch_time=None, total_views=None, total_row_count=None, negative_impact_score=None, metric=None, filter_value=None, filter_column=None):  # noqa: E501
        """Insight - a model defined in OpenAPI"""  # noqa: E501

        self._total_watch_time = None
        self._total_views = None
        self._total_row_count = None
        self._negative_impact_score = None
        self._metric = None
        self._filter_value = None
        self._filter_column = None
        self.discriminator = None

        if total_watch_time is not None:
            self.total_watch_time = total_watch_time
        if total_views is not None:
            self.total_views = total_views
        if total_row_count is not None:
            self.total_row_count = total_row_count
        if negative_impact_score is not None:
            self.negative_impact_score = negative_impact_score
        if metric is not None:
            self.metric = metric
        if filter_value is not None:
            self.filter_value = filter_value
        if filter_column is not None:
            self.filter_column = filter_column

    @property
    def total_watch_time(self):
        """Gets the total_watch_time of this Insight.  # noqa: E501


        :return: The total_watch_time of this Insight.  # noqa: E501
        :rtype: int
        """
        return self._total_watch_time

    @total_watch_time.setter
    def total_watch_time(self, total_watch_time):
        """Sets the total_watch_time of this Insight.


        :param total_watch_time: The total_watch_time of this Insight.  # noqa: E501
        :type: int
        """

        self._total_watch_time = total_watch_time

    @property
    def total_views(self):
        """Gets the total_views of this Insight.  # noqa: E501


        :return: The total_views of this Insight.  # noqa: E501
        :rtype: int
        """
        return self._total_views

    @total_views.setter
    def total_views(self, total_views):
        """Sets the total_views of this Insight.


        :param total_views: The total_views of this Insight.  # noqa: E501
        :type: int
        """

        self._total_views = total_views

    @property
    def total_row_count(self):
        """Gets the total_row_count of this Insight.  # noqa: E501


        :return: The total_row_count of this Insight.  # noqa: E501
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this Insight.


        :param total_row_count: The total_row_count of this Insight.  # noqa: E501
        :type: int
        """

        self._total_row_count = total_row_count

    @property
    def negative_impact_score(self):
        """Gets the negative_impact_score of this Insight.  # noqa: E501


        :return: The negative_impact_score of this Insight.  # noqa: E501
        :rtype: int
        """
        return self._negative_impact_score

    @negative_impact_score.setter
    def negative_impact_score(self, negative_impact_score):
        """Sets the negative_impact_score of this Insight.


        :param negative_impact_score: The negative_impact_score of this Insight.  # noqa: E501
        :type: int
        """

        self._negative_impact_score = negative_impact_score

    @property
    def metric(self):
        """Gets the metric of this Insight.  # noqa: E501


        :return: The metric of this Insight.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Insight.


        :param metric: The metric of this Insight.  # noqa: E501
        :type: int
        """

        self._metric = metric

    @property
    def filter_value(self):
        """Gets the filter_value of this Insight.  # noqa: E501


        :return: The filter_value of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._filter_value

    @filter_value.setter
    def filter_value(self, filter_value):
        """Sets the filter_value of this Insight.


        :param filter_value: The filter_value of this Insight.  # noqa: E501
        :type: str
        """

        self._filter_value = filter_value

    @property
    def filter_column(self):
        """Gets the filter_column of this Insight.  # noqa: E501


        :return: The filter_column of this Insight.  # noqa: E501
        :rtype: str
        """
        return self._filter_column

    @filter_column.setter
    def filter_column(self, filter_column):
        """Sets the filter_column of this Insight.


        :param filter_column: The filter_column of this Insight.  # noqa: E501
        :type: str
        """

        self._filter_column = filter_column

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Insight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
