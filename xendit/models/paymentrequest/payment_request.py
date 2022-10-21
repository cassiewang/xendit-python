from typing import List
from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params
from xendit.models._base_model import BaseModel
from xendit.models.paymentmethod.billing_information import BillingInformation
from xendit.models.paymentmethod.card.card import Card

from xendit.models.paymentmethod.direct_debit.direct_debit import DirectDebit
from xendit.models.paymentmethod.ewallet.ewallet import EWallet
from xendit.models.paymentmethod.over_the_counter.over_the_counter import (
    OverTheCounter,
)
from xendit.models.paymentmethod.payment_method import PaymentMethod
from xendit.models.paymentmethod.qr_code.qr_code import QRCode
from xendit.models.paymentmethod.virtual_account.virtual_account import (
    VirtualAccount,
)
from xendit.xendit_error import XenditError


class PaymentRequest(BaseModel):
    """PaymentMethod class (API Reference: Pay )

    Related Classes:
      - paymentmethod.PaymentMethod

    Static Methods:
      - PaymentRequest.create (API Reference: /Create Payment Method)
    """

    id: str 
    created: str
    type: str
    updated: str
    reference_id: str
    business_id: str
    customer_id:str
    amount: float
    country: str
    currency: str
    payment_method: PaymentMethod
    description: str
    failure_code: str
    capture_method: str
    initiator: str
    card_verification_results: dict
    status: str
    actions: List[dict]
    metadata: dict
    shipping_information: dict

    def create(
        *,
        currency: str,
        amount: float = None,
        reference_id: str = None,
        customer_id: str=None,
        country: str = None,
        description: str = None,
        payment_method: PaymentMethod.Query = None,
        payment_method_id: str=None,
        channel_properties: ChannelProperties.Query=None,
        metadata: dict=None,
        shipping_information: dict=None,
        capture_method: str=None,
        initiator: str=None,
        items: List[dict] = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Payment Requ
        (API Reference: Payment Methods/Create Payment Request)

        Args:
          - type (str)
          - reusability (str)
          - **reference_id (str)
          - **description (str)
          - **country (str)
          - **customer_id (str)
          - **payment_method (paymentmethod.PaymentMethod)
          - **payment_method_id (str)
          - **channel_properties (ChannelProperties)
          - **metadata (dict)
          - **shipping_information (dict)
          - **capture_method (str)
          - **initiator (str)
          - **items (List[dict])
          - **for_user_id (str)
          - **x_api_version  (str)

        Returns:
          PaymetnRequest

        Raises:
          XenditError
        """

        url = "/payment_requests"
        headers, body = _extract_params(
            locals(),
            func_object=PaymentMethod.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentRequest(**resp.body)
        else:
            raise XenditError(resp)
    
    @staticmethod
    def get(
        *,
        payment_request_id,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """Get Payment Request by Payment Request ID (API Reference: Payment Requests/Get Payment Request by ID)

        Args:
          - payment_request_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentRequest

        Raises:
          XenditError

        """
        url = f"/payment_requests/{payment_request_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentMethod.get,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_request_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def confirm(
        *,
        payment_request_id: str,
        auth_code: str,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """This endpoint only applies to BRI Direct Debit. This is only applicable for select payment DIRECT_DEBIT channels (BRI Direct Debit, BPI, RCBC, UBP, CHINABANK)
        This is used when an additional authorization (ex. OTP Validation, PIN validation) is required in order to successfully activate a payment method. This is equivalent to the POST - AUTH action provided when a Payment Method has the status REQUIRES_ACTION.
        (API Reference: Payment Requests/Confirm Payment Request)

        Args:
          - payment_request_id (str)
          - auth_code (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentRequest

        Raises:
          XenditError

        """
        url = f"/payment_requests/{payment_request_id}/auth"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentMethod.confirm,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_request_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)

    @staticmethod
    def list(
        *,
        after_id: str = None,
        before_id: str = None,
        channel_code: str = None,
        customer_id: str = None,
        payment_request_id: str = None,
        reusability: str = None,
        status: str = None,
        type: str = None,
        limit: int = None,
        for_user_id=None,
        x_api_version=None,
        **kwargs,
    ):
        """List retrieves an array of Payment Method objects that match the provided filter.
        An empty array [] will be returned if no records match the provided parameters.
        (API Reference: Payment Methods/Fetch Payment Methods)

        Args:
          - **after_id (str)
          - **before_id (str)
          - **channel_code (str)
          - **customer_id (str)
          - **id (str)
          - **reusability (str)
          - **status (str)
          - **type (str)
          - **limit (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          PaymentMethod[]

        Raises:
          XenditError

        """
        url = "/v2/payment_methods"
        headers, params = _extract_params(
            locals(),
            func_object=PaymentMethod.list,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=[],
        )
        kwargs["headers"] = headers
        kwargs["params"] = params

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            has_more = resp.body["has_more"]
            data = [PaymentMethod(**pm) for pm in resp.body["data"]]
            return PaymentRequestList(has_more=has_more, data=data)
        else:
            raise XenditError(resp)


class PaymentRequestList(BaseModel):
    has_more: bool
    data: List[PaymentRequestList]
