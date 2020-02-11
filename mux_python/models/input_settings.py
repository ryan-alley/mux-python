# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class InputSettings(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'overlay_settings': 'InputSettingsOverlaySettings',
        'type': 'str',
        'text_type': 'str',
        'language_code': 'str',
        'name': 'str',
        'closed_captions': 'bool',
        'passthrough': 'str'
    }

    attribute_map = {
        'url': 'url',
        'overlay_settings': 'overlay_settings',
        'type': 'type',
        'text_type': 'text_type',
        'language_code': 'language_code',
        'name': 'name',
        'closed_captions': 'closed_captions',
        'passthrough': 'passthrough'
    }

    def __init__(self, url=None, overlay_settings=None, type=None, text_type=None, language_code=None, name=None, closed_captions=None, passthrough=None):  # noqa: E501
        """InputSettings - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._overlay_settings = None
        self._type = None
        self._text_type = None
        self._language_code = None
        self._name = None
        self._closed_captions = None
        self._passthrough = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if overlay_settings is not None:
            self.overlay_settings = overlay_settings
        if type is not None:
            self.type = type
        if text_type is not None:
            self.text_type = text_type
        if language_code is not None:
            self.language_code = language_code
        if name is not None:
            self.name = name
        if closed_captions is not None:
            self.closed_captions = closed_captions
        if passthrough is not None:
            self.passthrough = passthrough

    @property
    def url(self):
        """Gets the url of this InputSettings.  # noqa: E501


        :return: The url of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InputSettings.


        :param url: The url of this InputSettings.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def overlay_settings(self):
        """Gets the overlay_settings of this InputSettings.  # noqa: E501


        :return: The overlay_settings of this InputSettings.  # noqa: E501
        :rtype: InputSettingsOverlaySettings
        """
        return self._overlay_settings

    @overlay_settings.setter
    def overlay_settings(self, overlay_settings):
        """Sets the overlay_settings of this InputSettings.


        :param overlay_settings: The overlay_settings of this InputSettings.  # noqa: E501
        :type: InputSettingsOverlaySettings
        """

        self._overlay_settings = overlay_settings

    @property
    def type(self):
        """Gets the type of this InputSettings.  # noqa: E501


        :return: The type of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputSettings.


        :param type: The type of this InputSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["video", "audio", "text"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def text_type(self):
        """Gets the text_type of this InputSettings.  # noqa: E501


        :return: The text_type of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._text_type

    @text_type.setter
    def text_type(self, text_type):
        """Sets the text_type of this InputSettings.


        :param text_type: The text_type of this InputSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["subtitles"]  # noqa: E501
        if text_type not in allowed_values:
            raise ValueError(
                "Invalid value for `text_type` ({0}), must be one of {1}"  # noqa: E501
                .format(text_type, allowed_values)
            )

        self._text_type = text_type

    @property
    def language_code(self):
        """Gets the language_code of this InputSettings.  # noqa: E501


        :return: The language_code of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this InputSettings.


        :param language_code: The language_code of this InputSettings.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def name(self):
        """Gets the name of this InputSettings.  # noqa: E501


        :return: The name of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputSettings.


        :param name: The name of this InputSettings.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def closed_captions(self):
        """Gets the closed_captions of this InputSettings.  # noqa: E501


        :return: The closed_captions of this InputSettings.  # noqa: E501
        :rtype: bool
        """
        return self._closed_captions

    @closed_captions.setter
    def closed_captions(self, closed_captions):
        """Sets the closed_captions of this InputSettings.


        :param closed_captions: The closed_captions of this InputSettings.  # noqa: E501
        :type: bool
        """

        self._closed_captions = closed_captions

    @property
    def passthrough(self):
        """Gets the passthrough of this InputSettings.  # noqa: E501


        :return: The passthrough of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this InputSettings.


        :param passthrough: The passthrough of this InputSettings.  # noqa: E501
        :type: str
        """

        self._passthrough = passthrough

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
        if not isinstance(other, InputSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
