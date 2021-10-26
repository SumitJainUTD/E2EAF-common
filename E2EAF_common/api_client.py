import requests


class ApiClient(object):

    def call_api(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return requests.get(url,
                                params=params,
                                timeout=timeout,
                                headers=headers)

        elif method == "HEAD":
            return requests.head(url,
                                 params=params,
                                 timeout=timeout,
                                 headers=headers)

        elif method == "OPTIONS":
            return requests.options(url,
                                    params=params,
                                    headers=headers,
                                    timeout=timeout,
                                    data=data)
        elif method == "POST":
            return requests.post(url,
                                 params=params,
                                 headers=headers,
                                 timeout=timeout,
                                 data=data)
        elif method == "PUT":
            return requests.put(url,
                                params=params,
                                headers=headers,
                                timeout=timeout,
                                data=data)
        elif method == "PATCH":
            return requests.patch(url,
                                  params=params,
                                  headers=headers,


                                  timeout=timeout,
                                  data=data)
        elif method == "DELETE":
            return requests.delete(url,
                                   params=params,
                                   headers=headers,
                                   timeout=timeout,
                                   data=data)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )