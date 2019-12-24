# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Riskv1authenticationsConsumerAuthenticationInformationIvr(object):
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
        'enabled_message': 'bool',
        'encryption_key': 'str',
        'encryption_mandatory': 'bool',
        'encryption_type': 'str',
        'label': 'str',
        'prompt': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'enabled_message': 'enabledMessage',
        'encryption_key': 'encryptionKey',
        'encryption_mandatory': 'encryptionMandatory',
        'encryption_type': 'encryptionType',
        'label': 'label',
        'prompt': 'prompt',
        'status_message': 'statusMessage'
    }

    def __init__(self, enabled_message=None, encryption_key=None, encryption_mandatory=None, encryption_type=None, label=None, prompt=None, status_message=None):
        """
        Riskv1authenticationsConsumerAuthenticationInformationIvr - a model defined in Swagger
        """

        self._enabled_message = None
        self._encryption_key = None
        self._encryption_mandatory = None
        self._encryption_type = None
        self._label = None
        self._prompt = None
        self._status_message = None

        if enabled_message is not None:
          self.enabled_message = enabled_message
        if encryption_key is not None:
          self.encryption_key = encryption_key
        if encryption_mandatory is not None:
          self.encryption_mandatory = encryption_mandatory
        if encryption_type is not None:
          self.encryption_type = encryption_type
        if label is not None:
          self.label = label
        if prompt is not None:
          self.prompt = prompt
        if status_message is not None:
          self.status_message = status_message

    @property
    def enabled_message(self):
        """
        Gets the enabled_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        Flag to indicate if a valid IVR transaction was detected. 

        :return: The enabled_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: bool
        """
        return self._enabled_message

    @enabled_message.setter
    def enabled_message(self, enabled_message):
        """
        Sets the enabled_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        Flag to indicate if a valid IVR transaction was detected. 

        :param enabled_message: The enabled_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: bool
        """

        self._enabled_message = enabled_message

    @property
    def encryption_key(self):
        """
        Gets the encryption_key of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        Encryption key to be used in the event the ACS requires encryption of the credential field. 

        :return: The encryption_key of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: str
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """
        Sets the encryption_key of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        Encryption key to be used in the event the ACS requires encryption of the credential field. 

        :param encryption_key: The encryption_key of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: str
        """
        if encryption_key is not None and len(encryption_key) > 16:
            raise ValueError("Invalid value for `encryption_key`, length must be less than or equal to `16`")

        self._encryption_key = encryption_key

    @property
    def encryption_mandatory(self):
        """
        Gets the encryption_mandatory of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        Flag to indicate if the ACS requires the credential to be encrypted. 

        :return: The encryption_mandatory of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: bool
        """
        return self._encryption_mandatory

    @encryption_mandatory.setter
    def encryption_mandatory(self, encryption_mandatory):
        """
        Sets the encryption_mandatory of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        Flag to indicate if the ACS requires the credential to be encrypted. 

        :param encryption_mandatory: The encryption_mandatory of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: bool
        """

        self._encryption_mandatory = encryption_mandatory

    @property
    def encryption_type(self):
        """
        Gets the encryption_type of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An indicator from the ACS to inform the type of encryption that should be used in the event the ACS requires encryption of the credential field. 

        :return: The encryption_type of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: str
        """
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, encryption_type):
        """
        Sets the encryption_type of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An indicator from the ACS to inform the type of encryption that should be used in the event the ACS requires encryption of the credential field. 

        :param encryption_type: The encryption_type of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: str
        """
        if encryption_type is not None and len(encryption_type) > 20:
            raise ValueError("Invalid value for `encryption_type`, length must be less than or equal to `20`")

        self._encryption_type = encryption_type

    @property
    def label(self):
        """
        Gets the label of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An ACS Provided label that can be presented to the Consumer. Recommended use with an application. 

        :return: The label of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An ACS Provided label that can be presented to the Consumer. Recommended use with an application. 

        :param label: The label of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: str
        """
        if label is not None and len(label) > 20:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `20`")

        self._label = label

    @property
    def prompt(self):
        """
        Gets the prompt of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An ACS provided string that can be presented to the Consumer. Recommended use with an application. 

        :return: The prompt of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        """
        Sets the prompt of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An ACS provided string that can be presented to the Consumer. Recommended use with an application. 

        :param prompt: The prompt of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: str
        """
        if prompt is not None and len(prompt) > 80:
            raise ValueError("Invalid value for `prompt`, length must be less than or equal to `80`")

        self._prompt = prompt

    @property
    def status_message(self):
        """
        Gets the status_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An ACS provided message that can provide additional information or details. 

        :return: The status_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        An ACS provided message that can provide additional information or details. 

        :param status_message: The status_message of this Riskv1authenticationsConsumerAuthenticationInformationIvr.
        :type: str
        """
        if status_message is not None and len(status_message) > 80:
            raise ValueError("Invalid value for `status_message`, length must be less than or equal to `80`")

        self._status_message = status_message

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
        if not isinstance(other, Riskv1authenticationsConsumerAuthenticationInformationIvr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other