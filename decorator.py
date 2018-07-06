def ensure_connection(method, return_value)
    """
    simple decorator that retry when error
    """
    def _decorator(self, *args, **kwargs):
        try:
            method(self, *args, **args)
        except Exception as e:
            #reconnect
            self._connect_()
            try:
                return method(self, *args, **kwargs)
            except Exception as e2:
                raise e2

    return _decorator
