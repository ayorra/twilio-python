# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CurrentCallList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CurrentCallList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallList
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallList
        """
        super(CurrentCallList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a CurrentCallContext

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        """
        return CurrentCallContext(self._version, )

    def __call__(self):
        """
        Constructs a CurrentCallContext

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        """
        return CurrentCallContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.CurrentCallList>'


class CurrentCallPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CurrentCallPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallPage
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallPage
        """
        super(CurrentCallPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CurrentCallInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallInstance
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallInstance
        """
        return CurrentCallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.CurrentCallPage>'


class CurrentCallContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CurrentCallContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        """
        super(CurrentCallContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/CurrentCall'.format(**self._solution)

    def fetch(self, from_=values.unset, to=values.unset):
        """
        Fetch a CurrentCallInstance

        :param unicode from_: The originating Phone Number
        :param unicode to: The terminating Phone Number

        :returns: Fetched CurrentCallInstance
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallInstance
        """
        params = values.of({'From': from_, 'To': to, })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CurrentCallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.CurrentCallContext {}>'.format(context)


class CurrentCallInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the CurrentCallInstance

        :returns: twilio.rest.preview.trusted_comms.current_call.CurrentCallInstance
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallInstance
        """
        super(CurrentCallInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'from_': payload['from'],
            'to': payload['to'],
            'reason': payload['reason'],
            'created_at': deserialize.iso8601_datetime(payload['created_at']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CurrentCallContext for this CurrentCallInstance
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallContext
        """
        if self._context is None:
            self._context = CurrentCallContext(self._version, )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Current Call.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def from_(self):
        """
        :returns: The originating Phone Number
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: The terminating Phone Number
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def reason(self):
        """
        :returns: The business reason for this phone call
        :rtype: unicode
        """
        return self._properties['reason']

    @property
    def created_at(self):
        """
        :returns: The date this Current Call was created
        :rtype: datetime
        """
        return self._properties['created_at']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, from_=values.unset, to=values.unset):
        """
        Fetch a CurrentCallInstance

        :param unicode from_: The originating Phone Number
        :param unicode to: The terminating Phone Number

        :returns: Fetched CurrentCallInstance
        :rtype: twilio.rest.preview.trusted_comms.current_call.CurrentCallInstance
        """
        return self._proxy.fetch(from_=from_, to=to, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.CurrentCallInstance {}>'.format(context)
