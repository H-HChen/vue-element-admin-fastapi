# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _rmt_py_wrapper
else:
    import _rmt_py_wrapper

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class device_info(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    deviceID = property(_rmt_py_wrapper.device_info_deviceID_get, _rmt_py_wrapper.device_info_deviceID_set)
    model = property(_rmt_py_wrapper.device_info_model_get, _rmt_py_wrapper.device_info_model_set)
    host = property(_rmt_py_wrapper.device_info_host_get, _rmt_py_wrapper.device_info_host_set)
    ip = property(_rmt_py_wrapper.device_info_ip_get, _rmt_py_wrapper.device_info_ip_set)
    mac = property(_rmt_py_wrapper.device_info_mac_get, _rmt_py_wrapper.device_info_mac_set)
    rmt_version = property(_rmt_py_wrapper.device_info_rmt_version_get, _rmt_py_wrapper.device_info_rmt_version_set)

    def __init__(self):
        _rmt_py_wrapper.device_info_swiginit(self, _rmt_py_wrapper.new_device_info())
    __swig_destroy__ = _rmt_py_wrapper.delete_device_info

# Register device_info in _rmt_py_wrapper:
_rmt_py_wrapper.device_info_swigregister(device_info)

CONFIG_KEY_STR_LEN = _rmt_py_wrapper.CONFIG_KEY_STR_LEN
class data_info(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    deviceID = property(_rmt_py_wrapper.data_info_deviceID_get, _rmt_py_wrapper.data_info_deviceID_set)
    value_list = property(_rmt_py_wrapper.data_info_value_list_get, _rmt_py_wrapper.data_info_value_list_set)

    def __init__(self):
        _rmt_py_wrapper.data_info_swiginit(self, _rmt_py_wrapper.new_data_info())
    __swig_destroy__ = _rmt_py_wrapper.delete_data_info

# Register data_info in _rmt_py_wrapper:
_rmt_py_wrapper.data_info_swigregister(data_info)


def rmt_server_config(interface):
    return _rmt_py_wrapper.rmt_server_config(interface)

def rmt_server_init():
    return _rmt_py_wrapper.rmt_server_init()

def rmt_server_create_device_list(num):
    return _rmt_py_wrapper.rmt_server_create_device_list(num)

def rmt_server_free_device_list(dev):
    return _rmt_py_wrapper.rmt_server_free_device_list(dev)

def rmt_server_get_info(id_list, id_num, key_list, info_num):
    return _rmt_py_wrapper.rmt_server_get_info(id_list, id_num, key_list, info_num)

def rmt_server_free_info(info_list):
    return _rmt_py_wrapper.rmt_server_free_info(info_list)

def rmt_server_set_info(dev_list, dev_num, info_num):
    return _rmt_py_wrapper.rmt_server_set_info(dev_list, dev_num, info_num)

def rmt_server_set_info_with_same_value(id_list, id_num, value_list, info_num):
    return _rmt_py_wrapper.rmt_server_set_info_with_same_value(id_list, id_num, value_list, info_num)

def rmt_server_send_file(filename, pFile, file_len):
    return _rmt_py_wrapper.rmt_server_send_file(filename, pFile, file_len)

def rmt_server_recv_file(filename, pFile, file_len):
    return _rmt_py_wrapper.rmt_server_recv_file(filename, pFile, file_len)

def rmt_server_deinit():
    return _rmt_py_wrapper.rmt_server_deinit()

def rmt_server_version():
    return _rmt_py_wrapper.rmt_server_version()

def new_intptr():
    return _rmt_py_wrapper.new_intptr()

def copy_intptr(value):
    return _rmt_py_wrapper.copy_intptr(value)

def delete_intptr(obj):
    return _rmt_py_wrapper.delete_intptr(obj)

def intptr_assign(obj, value):
    return _rmt_py_wrapper.intptr_assign(obj, value)

def intptr_value(obj):
    return _rmt_py_wrapper.intptr_value(obj)

def new_data_info_array(nelements):
    return _rmt_py_wrapper.new_data_info_array(nelements)

def delete_data_info_array(ary):
    return _rmt_py_wrapper.delete_data_info_array(ary)

def data_info_array_getitem(ary, index):
    return _rmt_py_wrapper.data_info_array_getitem(ary, index)

def data_info_array_setitem(ary, index, value):
    return _rmt_py_wrapper.data_info_array_setitem(ary, index, value)
class device_info_list(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _rmt_py_wrapper.device_info_list_swiginit(self, _rmt_py_wrapper.new_device_info_list(nelements))
    __swig_destroy__ = _rmt_py_wrapper.delete_device_info_list

    def __getitem__(self, index):
        return _rmt_py_wrapper.device_info_list___getitem__(self, index)

    def __setitem__(self, index, value):
        return _rmt_py_wrapper.device_info_list___setitem__(self, index, value)

    def cast(self):
        return _rmt_py_wrapper.device_info_list_cast(self)

    @staticmethod
    def frompointer(t):
        return _rmt_py_wrapper.device_info_list_frompointer(t)

# Register device_info_list in _rmt_py_wrapper:
_rmt_py_wrapper.device_info_list_swigregister(device_info_list)

def device_info_list_frompointer(t):
    return _rmt_py_wrapper.device_info_list_frompointer(t)

class data_info_list(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _rmt_py_wrapper.data_info_list_swiginit(self, _rmt_py_wrapper.new_data_info_list(nelements))
    __swig_destroy__ = _rmt_py_wrapper.delete_data_info_list

    def __getitem__(self, index):
        return _rmt_py_wrapper.data_info_list___getitem__(self, index)

    def __setitem__(self, index, value):
        return _rmt_py_wrapper.data_info_list___setitem__(self, index, value)

    def cast(self):
        return _rmt_py_wrapper.data_info_list_cast(self)

    @staticmethod
    def frompointer(t):
        return _rmt_py_wrapper.data_info_list_frompointer(t)

# Register data_info_list in _rmt_py_wrapper:
_rmt_py_wrapper.data_info_list_swigregister(data_info_list)

def data_info_list_frompointer(t):
    return _rmt_py_wrapper.data_info_list_frompointer(t)

class ulong_array(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _rmt_py_wrapper.ulong_array_swiginit(self, _rmt_py_wrapper.new_ulong_array(nelements))
    __swig_destroy__ = _rmt_py_wrapper.delete_ulong_array

    def __getitem__(self, index):
        return _rmt_py_wrapper.ulong_array___getitem__(self, index)

    def __setitem__(self, index, value):
        return _rmt_py_wrapper.ulong_array___setitem__(self, index, value)

    def cast(self):
        return _rmt_py_wrapper.ulong_array_cast(self)

    @staticmethod
    def frompointer(t):
        return _rmt_py_wrapper.ulong_array_frompointer(t)

# Register ulong_array in _rmt_py_wrapper:
_rmt_py_wrapper.ulong_array_swigregister(ulong_array)

def ulong_array_frompointer(t):
    return _rmt_py_wrapper.ulong_array_frompointer(t)



