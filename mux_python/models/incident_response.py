# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class IncidentResponse(object):
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
        'data': 'Incident',
        'timeframe': 'list[int]'
    }

    attribute_map = {
        'data': 'data',
        'timeframe': 'timeframe'
    }

    def __init__(self, data=None, timeframe=None, local_vars_configuration=None):  # noqa: E501
        """IncidentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._timeframe = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if timeframe is not None:
            self.timeframe = timeframe

    @property
    def data(self):
        """Gets the data of this IncidentResponse.  # noqa: E501


        :return: The data of this IncidentResponse.  # noqa: E501
        :rtype: Incident
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this IncidentResponse.


        :param data: The data of this IncidentResponse.  # noqa: E501
        :type data: Incident
        """

        self._data = data

    @property
    def timeframe(self):
        """Gets the timeframe of this IncidentResponse.  # noqa: E501


        :return: The timeframe of this IncidentResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe):
        """Sets the timeframe of this IncidentResponse.


        :param timeframe: The timeframe of this IncidentResponse.  # noqa: E501
        :type timeframe: list[int]
        """

        self._timeframe = timeframe

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IncidentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncidentResponse):
            return True

        return self.to_dict() != other.to_dict()
