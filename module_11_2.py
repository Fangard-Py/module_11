def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    module_name = obj.__mod__
    additional_info = {}
    if hasattr(obj, '__doc__'):
        additional_info['doc'] = obj.__doc__
    if hasattr(obj, '__name__'):
        additional_info['name'] = obj.__name__
    info = {'type': obj_type, 'attributes': attributes,
            'methods': methods, 'module': module_name,
            'additional_info': additional_info}
    return info


number_info = introspection_info(42)
print(number_info)
