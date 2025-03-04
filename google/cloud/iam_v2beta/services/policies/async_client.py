# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.iam_v2beta.services.policies import pagers
from google.cloud.iam_v2beta.types import policy
from google.cloud.iam_v2beta.types import policy as gi_policy

from .client import PoliciesClient
from .transports.base import DEFAULT_CLIENT_INFO, PoliciesTransport
from .transports.grpc_asyncio import PoliciesGrpcAsyncIOTransport


class PoliciesAsyncClient:
    """An interface for managing Identity and Access Management
    (IAM) policies.
    """

    _client: PoliciesClient

    DEFAULT_ENDPOINT = PoliciesClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PoliciesClient.DEFAULT_MTLS_ENDPOINT

    policy_path = staticmethod(PoliciesClient.policy_path)
    parse_policy_path = staticmethod(PoliciesClient.parse_policy_path)
    common_billing_account_path = staticmethod(
        PoliciesClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PoliciesClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(PoliciesClient.common_folder_path)
    parse_common_folder_path = staticmethod(PoliciesClient.parse_common_folder_path)
    common_organization_path = staticmethod(PoliciesClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        PoliciesClient.parse_common_organization_path
    )
    common_project_path = staticmethod(PoliciesClient.common_project_path)
    parse_common_project_path = staticmethod(PoliciesClient.parse_common_project_path)
    common_location_path = staticmethod(PoliciesClient.common_location_path)
    parse_common_location_path = staticmethod(PoliciesClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PoliciesAsyncClient: The constructed client.
        """
        return PoliciesClient.from_service_account_info.__func__(PoliciesAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PoliciesAsyncClient: The constructed client.
        """
        return PoliciesClient.from_service_account_file.__func__(PoliciesAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return PoliciesClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PoliciesTransport:
        """Returns the transport used by the client instance.

        Returns:
            PoliciesTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PoliciesClient).get_transport_class, type(PoliciesClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, PoliciesTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the policies client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PoliciesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = PoliciesClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_policies(
        self,
        request: Union[policy.ListPoliciesRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPoliciesAsyncPager:
        r"""Retrieves the policies of the specified kind that are
        attached to a resource.

        The response lists only policy metadata. In particular,
        policy rules are omitted.

        .. code-block:: python

            from google.cloud import iam_v2beta

            async def sample_list_policies():
                # Create a client
                client = iam_v2beta.PoliciesAsyncClient()

                # Initialize request argument(s)
                request = iam_v2beta.ListPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.iam_v2beta.types.ListPoliciesRequest, dict]):
                The request object. Request message for `ListPolicies`.
            parent (:class:`str`):
                Required. The resource that the policy is attached to,
                along with the kind of policy to list. Format:
                ``policies/{attachment_point}/denypolicies``

                The attachment point is identified by its URL-encoded
                full resource name, which means that the forward-slash
                character, ``/``, must be written as ``%2F``. For
                example,
                ``policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies``.

                For organizations and folders, use the numeric ID in the
                full resource name. For projects, you can use the
                alphanumeric or the numeric ID.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager:
                Response message for ListPolicies.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy.ListPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_policies,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_policy(
        self,
        request: Union[policy.GetPolicyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy.Policy:
        r"""Gets a policy.

        .. code-block:: python

            from google.cloud import iam_v2beta

            async def sample_get_policy():
                # Create a client
                client = iam_v2beta.PoliciesAsyncClient()

                # Initialize request argument(s)
                request = iam_v2beta.GetPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iam_v2beta.types.GetPolicyRequest, dict]):
                The request object. Request message for `GetPolicy`.
            name (:class:`str`):
                Required. The resource name of the policy to retrieve.
                Format:
                ``policies/{attachment_point}/denypolicies/{policy_id}``

                Use the URL-encoded full resource name, which means that
                the forward-slash character, ``/``, must be written as
                ``%2F``. For example,
                ``policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy``.

                For organizations and folders, use the numeric ID in the
                full resource name. For projects, you can use the
                alphanumeric or the numeric ID.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iam_v2beta.types.Policy:
                Data for an IAM policy.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy.GetPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_policy,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_policy(
        self,
        request: Union[gi_policy.CreatePolicyRequest, dict] = None,
        *,
        parent: str = None,
        policy: gi_policy.Policy = None,
        policy_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a policy.

        .. code-block:: python

            from google.cloud import iam_v2beta

            async def sample_create_policy():
                # Create a client
                client = iam_v2beta.PoliciesAsyncClient()

                # Initialize request argument(s)
                request = iam_v2beta.CreatePolicyRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_policy(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iam_v2beta.types.CreatePolicyRequest, dict]):
                The request object. Request message for `CreatePolicy`.
            parent (:class:`str`):
                Required. The resource that the policy is attached to,
                along with the kind of policy to create. Format:
                ``policies/{attachment_point}/denypolicies``

                The attachment point is identified by its URL-encoded
                full resource name, which means that the forward-slash
                character, ``/``, must be written as ``%2F``. For
                example,
                ``policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies``.

                For organizations and folders, use the numeric ID in the
                full resource name. For projects, you can use the
                alphanumeric or the numeric ID.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy (:class:`google.cloud.iam_v2beta.types.Policy`):
                Required. The policy to create.
                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy_id (:class:`str`):
                The ID to use for this policy, which will become the
                final component of the policy's resource name. The ID
                must contain 3 to 63 characters. It can contain
                lowercase letters and numbers, as well as dashes (``-``)
                and periods (``.``). The first character must be a
                lowercase letter.

                This corresponds to the ``policy_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.iam_v2beta.types.Policy` Data for
                an IAM policy.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, policy, policy_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gi_policy.CreatePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if policy is not None:
            request.policy = policy
        if policy_id is not None:
            request.policy_id = policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_policy,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            gi_policy.Policy,
            metadata_type=gi_policy.PolicyOperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_policy(
        self,
        request: Union[policy.UpdatePolicyRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the specified policy.

        You can update only the rules and the display name for the
        policy.

        To update a policy, you should use a read-modify-write loop:

        1. Use [GetPolicy][google.iam.v2beta.Policies.GetPolicy] to read
           the current version of the policy.
        2. Modify the policy as needed.
        3. Use ``UpdatePolicy`` to write the updated policy.

        This pattern helps prevent conflicts between concurrent updates.

        .. code-block:: python

            from google.cloud import iam_v2beta

            async def sample_update_policy():
                # Create a client
                client = iam_v2beta.PoliciesAsyncClient()

                # Initialize request argument(s)
                request = iam_v2beta.UpdatePolicyRequest(
                )

                # Make the request
                operation = client.update_policy(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iam_v2beta.types.UpdatePolicyRequest, dict]):
                The request object. Request message for `UpdatePolicy`.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.iam_v2beta.types.Policy` Data for
                an IAM policy.

        """
        # Create or coerce a protobuf request object.
        request = policy.UpdatePolicyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_policy,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("policy.name", request.policy.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            policy.Policy,
            metadata_type=policy.PolicyOperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_policy(
        self,
        request: Union[policy.DeletePolicyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a policy. This action is permanent.

        .. code-block:: python

            from google.cloud import iam_v2beta

            async def sample_delete_policy():
                # Create a client
                client = iam_v2beta.PoliciesAsyncClient()

                # Initialize request argument(s)
                request = iam_v2beta.DeletePolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_policy(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iam_v2beta.types.DeletePolicyRequest, dict]):
                The request object. Request message for `DeletePolicy`.
            name (:class:`str`):
                Required. The resource name of the policy to delete.
                Format:
                ``policies/{attachment_point}/denypolicies/{policy_id}``

                Use the URL-encoded full resource name, which means that
                the forward-slash character, ``/``, must be written as
                ``%2F``. For example,
                ``policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy``.

                For organizations and folders, use the numeric ID in the
                full resource name. For projects, you can use the
                alphanumeric or the numeric ID.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.iam_v2beta.types.Policy` Data for
                an IAM policy.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = policy.DeletePolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_policy,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            policy.Policy,
            metadata_type=policy.PolicyOperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-iam",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("PoliciesAsyncClient",)
