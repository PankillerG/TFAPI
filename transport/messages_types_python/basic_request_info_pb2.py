# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basic_request_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basic_request_info.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x62\x61sic_request_info.proto\"d\n\x10\x42\x61sicRequestInfo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0buse_sandbox\x18\x02 \x01(\x08\x12\x15\n\rrequest_topic\x18\x03 \x01(\t\x12\x16\n\x0eresponse_topic\x18\x04 \x01(\tb\x06proto3'
)




_BASICREQUESTINFO = _descriptor.Descriptor(
  name='BasicRequestInfo',
  full_name='BasicRequestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='BasicRequestInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_sandbox', full_name='BasicRequestInfo.use_sandbox', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_topic', full_name='BasicRequestInfo.request_topic', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_topic', full_name='BasicRequestInfo.response_topic', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['BasicRequestInfo'] = _BASICREQUESTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BasicRequestInfo = _reflection.GeneratedProtocolMessageType('BasicRequestInfo', (_message.Message,), {
  'DESCRIPTOR' : _BASICREQUESTINFO,
  '__module__' : 'basic_request_info_pb2'
  # @@protoc_insertion_point(class_scope:BasicRequestInfo)
  })
_sym_db.RegisterMessage(BasicRequestInfo)


# @@protoc_insertion_point(module_scope)
