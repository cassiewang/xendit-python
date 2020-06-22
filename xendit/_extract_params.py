import inspect


def _extract_params(function_locals, func_object, headers_params=[]):
    """Extract data from function_locals to headers and body of the request

    Args:
        - function_locals (dict): locals() of the function
        - func_object (function): Function that will be analyzed the parameter list
        - **headers_params (list): List of headers parameter. Defaults to [].

    Returns:
        dict, dict: headers and body of the request
    """
    body = dict()
    headers = dict()
    map_headers_key = {
        "for_user_id": "for-user-id",
        "x_idempotency_key": "X-IDEMPOTENCY-KEY",
    }
    for param in inspect.getfullargspec(func_object)[0]:
        value = function_locals.get(param, None)
        if value is not None:
            if param in headers_params:
                mapped_param = map_headers_key[param]
                headers[mapped_param] = function_locals[param]
            else:
                body[param] = function_locals[param]
    return headers, body
