# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
_PBRESULTCODE = descriptor.EnumDescriptor(
  name='PBResultCode',
  full_name='PBResultCode',
  filename='PBResultCode',
  values=[
    descriptor.EnumValueDescriptor(
      name='UNKNOW_ERROR', index=0, number=-1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SYSTEM_ERROR', index=2, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PARSE_PB_ERROR', index=3, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PARAMETER_ERROR', index=4, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='AUTH_ERROR', index=5, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NETWORK_ERROR', index=6, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TIMEOUT_ERROR', index=7, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UNLOGIN_ERROR', index=8, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='USER_NOT_EXISTS_ERROR', index=9, number=10001,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PASSWORD_INCORRECT_ERROR', index=10, number=10002,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='USER_STATUS_EXCEPTION_ERROR', index=11, number=10003,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UNAME_EXISTS_ERROR', index=12, number=10004,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACTION_NOT_EXISTS_ERROR', index=13, number=20001,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACTION_STATUS_EXCEPTION_ERROR', index=14, number=20002,
      options=None,
      type=None),
  ],
  options=None,
)


UNKNOW_ERROR = -1
SUCCESS = 0
SYSTEM_ERROR = 1
PARSE_PB_ERROR = 2
PARAMETER_ERROR = 3
AUTH_ERROR = 4
NETWORK_ERROR = 5
TIMEOUT_ERROR = 6
UNLOGIN_ERROR = 7
USER_NOT_EXISTS_ERROR = 10001
PASSWORD_INCORRECT_ERROR = 10002
USER_STATUS_EXCEPTION_ERROR = 10003
UNAME_EXISTS_ERROR = 10004
ACTION_NOT_EXISTS_ERROR = 20001
ACTION_STATUS_EXCEPTION_ERROR = 20002



_PBRESPONSE = descriptor.Descriptor(
  name='PBResponse',
  full_name='PBResponse',
  filename='response.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='PBResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error_message', full_name='PBResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='has_more', full_name='PBResponse.has_more', index=2,
      number=3, type=8, cpp_type=7, label=1,
      default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='actions', full_name='PBResponse.actions', index=3,
      number=10, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='messages', full_name='PBResponse.messages', index=4,
      number=11, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='users', full_name='PBResponse.users', index=5,
      number=12, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='activitys', full_name='PBResponse.activitys', index=6,
      number=13, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comments', full_name='PBResponse.comments', index=7,
      number=14, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='briefUsers', full_name='PBResponse.briefUsers', index=8,
      number=15, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='PBResponse.user', index=9,
      number=50, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='action', full_name='PBResponse.action', index=10,
      number=51, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='merchant', full_name='PBResponse.merchant', index=11,
      number=52, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)

import basic_pb2
import user_pb2
import action_pb2
import message_pb2

_PBRESPONSE.fields_by_name['code'].enum_type = _PBRESULTCODE
_PBRESPONSE.fields_by_name['actions'].message_type = action_pb2._PBACTION
_PBRESPONSE.fields_by_name['messages'].message_type = message_pb2._PBMESSAGE
_PBRESPONSE.fields_by_name['users'].message_type = user_pb2._PBUSER
_PBRESPONSE.fields_by_name['activitys'].message_type = action_pb2._PBACTIVITY
_PBRESPONSE.fields_by_name['comments'].message_type = action_pb2._PBCOMMENT
_PBRESPONSE.fields_by_name['briefUsers'].message_type = user_pb2._PBBRIEFUSER
_PBRESPONSE.fields_by_name['user'].message_type = user_pb2._PBUSER
_PBRESPONSE.fields_by_name['action'].message_type = action_pb2._PBACTION
_PBRESPONSE.fields_by_name['merchant'].message_type = action_pb2._PBMERCHANT

class PBResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRESPONSE

