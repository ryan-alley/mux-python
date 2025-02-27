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


class LiveStreamEmbeddedSubtitleSettings(object):
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
        'name': 'str',
        'passthrough': 'str',
        'language_code': 'str',
        'language_channel': 'str'
    }

    attribute_map = {
        'name': 'name',
        'passthrough': 'passthrough',
        'language_code': 'language_code',
        'language_channel': 'language_channel'
    }

    def __init__(self, name=None, passthrough=None, language_code='en', language_channel='cc1', local_vars_configuration=None):  # noqa: E501
        """LiveStreamEmbeddedSubtitleSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._passthrough = None
        self._language_code = None
        self._language_channel = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if passthrough is not None:
            self.passthrough = passthrough
        if language_code is not None:
            self.language_code = language_code
        if language_channel is not None:
            self.language_channel = language_channel

    @property
    def name(self):
        """Gets the name of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501

        A name for this live stream closed caption track.  # noqa: E501

        :return: The name of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LiveStreamEmbeddedSubtitleSettings.

        A name for this live stream closed caption track.  # noqa: E501

        :param name: The name of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def passthrough(self):
        """Gets the passthrough of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501

        Arbitrary user-supplied metadata set for the live stream closed caption track. Max 255 characters.  # noqa: E501

        :return: The passthrough of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this LiveStreamEmbeddedSubtitleSettings.

        Arbitrary user-supplied metadata set for the live stream closed caption track. Max 255 characters.  # noqa: E501

        :param passthrough: The passthrough of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def language_code(self):
        """Gets the language_code of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501

        The language of the closed caption stream. Value must be BCP 47 compliant.  # noqa: E501

        :return: The language_code of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this LiveStreamEmbeddedSubtitleSettings.

        The language of the closed caption stream. Value must be BCP 47 compliant.  # noqa: E501

        :param language_code: The language_code of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :type language_code: str
        """

        self._language_code = language_code

    @property
    def language_channel(self):
        """Gets the language_channel of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501

        CEA-608 caption channel to read data from.  # noqa: E501

        :return: The language_channel of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :rtype: str
        """
        return self._language_channel

    @language_channel.setter
    def language_channel(self, language_channel):
        """Sets the language_channel of this LiveStreamEmbeddedSubtitleSettings.

        CEA-608 caption channel to read data from.  # noqa: E501

        :param language_channel: The language_channel of this LiveStreamEmbeddedSubtitleSettings.  # noqa: E501
        :type language_channel: str
        """
        allowed_values = ["cc1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language_channel not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language_channel` ({0}), must be one of {1}"  # noqa: E501
                .format(language_channel, allowed_values)
            )

        self._language_channel = language_channel

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
        if not isinstance(other, LiveStreamEmbeddedSubtitleSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LiveStreamEmbeddedSubtitleSettings):
            return True

        return self.to_dict() != other.to_dict()
