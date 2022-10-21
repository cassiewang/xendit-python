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
<<<<<<< HEAD
      - PaymentRequest.create (API Reference: /Create Payment Method)
=======
      - PaymentRequest.create (API Reference: /Create a payment method)
>>>>>>> 7fee56d (wip)
    """

    id: str 
    created: str
    type: str
    updated: str
    reference_id: str
    business_id: str
<<<<<<< HEAD
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
=======
          type: string
    customer_id:
          type: string
        amount:
          format: double
          type: number
        country:
          $ref: '#/components/schemas/PaymentRequestCountry'
        currency:
          $ref: '#/components/schemas/PaymentRequestCurrency'
        payment_method:
          $ref: '#/components/schemas/PublicPaymentMethod'
        description:
          type: string
        failure_code:
          nullable: true
          type: string
        capture_method:
          $ref: '#/components/schemas/PaymentRequestCaptureMethod'
        initiator:
          $ref: '#/components/schemas/PaymentRequestInitiator'
        card_verification_results:
          $ref: '#/components/schemas/PaymentRequestCardVerificationResults'
        status:
          $ref: '#/components/schemas/PaymentRequestStatus'
        actions:
          type: array
          items:
            $ref: '#/components/schemas/PaymentRequestAction'
        metadata:
          $ref: '#/components/schemas/Object'
        shipping_information:
          $ref: '#/components/schemas/PaymentRequestShippingInformation'

    def create(
>>>>>>> 7fee56d (wip)
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
<<<<<<< HEAD
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
        """Get Payment Request by Payment Request ID (API Reference: Payment Methods/Get Payment Method by ID)

        Args:
          - payment_method_id (str)
          - **for_user_id (str)
          - **x_api_version (str)

        Returns:
          Payment Method

        Raises:
          XenditError

        """
        url = f"/v2/payment_methods/{payment_method_id}"
        headers, _ = _extract_params(
            locals(),
            func_object=PaymentMethod.get,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
            ignore_params=["payment_method_id"],
        )
        kwargs["headers"] = headers

        resp = _APIRequestor.get(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return PaymentMethod(**resp.body)
        else:
            raise XenditError(resp)
=======
        shipping_information: ShippingInformation=None,
        capture_method: str=None,
        initiator: str=None,
        items: List[dict],
    ):
        pass
>>>>>>> 7fee56d (wip)
