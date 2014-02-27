# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='atm_message',
  serialized_pb='\n\x0emessages.proto\x12\x0b\x61tm_message\"\\\n\rClientRequest\x12\x0f\n\x07version\x18\x01 \x02(\t\x12\x10\n\x08\x63hecksum\x18\x02 \x02(\t\x12\x0e\n\x06opcode\x18\x03 \x02(\t\x12\x0b\n\x03\x61\x63t\x18\x04 \x02(\x05\x12\x0b\n\x03\x62\x61l\x18\x05 \x01(\x05\"t\n\x0eServerResponse\x12\x0f\n\x07version\x18\x01 \x02(\t\x12\x10\n\x08\x63hecksum\x18\x02 \x02(\t\x12\x0e\n\x06opcode\x18\x03 \x02(\t\x12\x0b\n\x03\x61\x63t\x18\x04 \x01(\x05\x12\x0b\n\x03\x62\x61l\x18\x05 \x01(\x05\x12\x15\n\rerror_message\x18\x06 \x01(\t')




_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='atm_message.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='atm_message.ClientRequest.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='atm_message.ClientRequest.checksum', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opcode', full_name='atm_message.ClientRequest.opcode', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='atm_message.ClientRequest.act', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bal', full_name='atm_message.ClientRequest.bal', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=31,
  serialized_end=123,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='atm_message.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='atm_message.ServerResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='atm_message.ServerResponse.checksum', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opcode', full_name='atm_message.ServerResponse.opcode', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='atm_message.ServerResponse.act', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bal', full_name='atm_message.ServerResponse.bal', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='atm_message.ServerResponse.error_message', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=125,
  serialized_end=241,
)

DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE

class ClientRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLIENTREQUEST

  # @@protoc_insertion_point(class_scope:atm_message.ClientRequest)

class ServerResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERRESPONSE

  # @@protoc_insertion_point(class_scope:atm_message.ServerResponse)


# @@protoc_insertion_point(module_scope)
