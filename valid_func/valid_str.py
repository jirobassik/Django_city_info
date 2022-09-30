def check_for_numeric(self, str_name, value_name):
    if value_name.isnumeric():
        self._errors[str_name] = self.error_class([
            'Значение должно быть строкой'])