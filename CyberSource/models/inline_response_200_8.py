# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2008(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'InlineResponse2008Links',
        'object': 'str',
        'offset': 'str',
        'limit': 'str',
        'count': 'str',
        'total': 'str',
        'embedded': 'object'
    }

    attribute_map = {
        'links': '_links',
        'object': 'object',
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count',
        'total': 'total',
        'embedded': '_embedded'
    }

    def __init__(self, links=None, object=None, offset=None, limit=None, count=None, total=None, embedded=None):
        """
        InlineResponse2008 - a model defined in Swagger
        """

        self._links = None
        self._object = None
        self._offset = None
        self._limit = None
        self._count = None
        self._total = None
        self._embedded = None

        if links is not None:
          self.links = links
        if object is not None:
          self.object = object
        if offset is not None:
          self.offset = offset
        if limit is not None:
          self.limit = limit
        if count is not None:
          self.count = count
        if total is not None:
          self.total = total
        if embedded is not None:
          self.embedded = embedded

    @property
    def links(self):
        """
        Gets the links of this InlineResponse2008.

        :return: The links of this InlineResponse2008.
        :rtype: InlineResponse2008Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse2008.

        :param links: The links of this InlineResponse2008.
        :type: InlineResponse2008Links
        """

        self._links = links

    @property
    def object(self):
        """
        Gets the object of this InlineResponse2008.
        Shows the response is a collection of objects.

        :return: The object of this InlineResponse2008.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this InlineResponse2008.
        Shows the response is a collection of objects.

        :param object: The object of this InlineResponse2008.
        :type: str
        """
        allowed_values = ["collection"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def offset(self):
        """
        Gets the offset of this InlineResponse2008.
        The offset parameter supplied in the request.

        :return: The offset of this InlineResponse2008.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this InlineResponse2008.
        The offset parameter supplied in the request.

        :param offset: The offset of this InlineResponse2008.
        :type: str
        """

        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this InlineResponse2008.
        The limit parameter supplied in the request.

        :return: The limit of this InlineResponse2008.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this InlineResponse2008.
        The limit parameter supplied in the request.

        :param limit: The limit of this InlineResponse2008.
        :type: str
        """

        self._limit = limit

    @property
    def count(self):
        """
        Gets the count of this InlineResponse2008.
        The number of Payment Instruments returned in the array.

        :return: The count of this InlineResponse2008.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this InlineResponse2008.
        The number of Payment Instruments returned in the array.

        :param count: The count of this InlineResponse2008.
        :type: str
        """

        self._count = count

    @property
    def total(self):
        """
        Gets the total of this InlineResponse2008.
        The total number of Payment Instruments associated with the Instrument Identifier in the zero-based dataset.

        :return: The total of this InlineResponse2008.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this InlineResponse2008.
        The total number of Payment Instruments associated with the Instrument Identifier in the zero-based dataset.

        :param total: The total of this InlineResponse2008.
        :type: str
        """

        self._total = total

    @property
    def embedded(self):
        """
        Gets the embedded of this InlineResponse2008.
        Array of Payment Instruments returned for the supplied Instrument Identifier.

        :return: The embedded of this InlineResponse2008.
        :rtype: object
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """
        Sets the embedded of this InlineResponse2008.
        Array of Payment Instruments returned for the supplied Instrument Identifier.

        :param embedded: The embedded of this InlineResponse2008.
        :type: object
        """

        self._embedded = embedded

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other