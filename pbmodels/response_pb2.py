# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import basic_pb2
import user_pb2
import action_pb2
import message_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='response.proto',
  package='',
  serialized_pb='\n\x0eresponse.proto\x1a\x0b\x62\x61sic.proto\x1a\nuser.proto\x1a\x0c\x61\x63tion.proto\x1a\rmessage.proto\"\xa6\x02\n\nPBResponse\x12\x1b\n\x04\x63ode\x18\x01 \x02(\x0e\x32\r.PBResultCode\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x1a\n\x07\x61\x63tions\x18\n \x03(\x0b\x32\t.PBAction\x12\x1c\n\x08messages\x18\x0b \x03(\x0b\x32\n.PBMessage\x12\x1b\n\x05users\x18\x0c \x03(\x0b\x32\x0c.PBUserBasic\x12\x1e\n\tactivitys\x18\r \x03(\x0b\x32\x0b.PBActivity\x12\x1c\n\x08\x63omments\x18\x0e \x03(\x0b\x32\n.PBComment\x12\x15\n\x04user\x18\x32 \x01(\x0b\x32\x07.PBUser\x12\x19\n\x06\x61\x63tion\x18\x33 \x01(\x0b\x32\t.PBAction\x12\x1d\n\x08merchant\x18\x34 \x01(\x0b\x32\x0b.PBMerchant*\xc8\x02\n\x0cPBResultCode\x12\x19\n\x0cUNKNOW_ERROR\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0b\n\x07SUCCESS\x10\x00\x12\x10\n\x0cSYSTEM_ERROR\x10\x01\x12\x12\n\x0ePARSE_PB_ERROR\x10\x02\x12\x13\n\x0fPARAMETER_ERROR\x10\x03\x12\x0e\n\nAUTH_ERROR\x10\x04\x12\x11\n\rNETWORK_ERROR\x10\x05\x12\x11\n\rTIMEOUT_ERROR\x10\x06\x12\x1a\n\x15USER_NOT_EXISTS_ERROR\x10\x91N\x12\x1d\n\x18PASSWORD_INCORRECT_ERROR\x10\x92N\x12 \n\x1bUSER_STATUS_EXCEPTION_ERROR\x10\x93N\x12\x1d\n\x17\x41\x43TION_NOT_EXISTS_ERROR\x10\xa1\x9c\x01\x12#\n\x1d\x41\x43TION_STATUS_EXCEPTION_ERROR\x10\xa2\x9c\x01')

_PBRESULTCODE = descriptor.EnumDescriptor(
  name='PBResultCode',
  full_name='PBResultCode',
  filename=None,
  file=DESCRIPTOR,
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
      name='USER_NOT_EXISTS_ERROR', index=8, number=10001,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PASSWORD_INCORRECT_ERROR', index=9, number=10002,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='USER_STATUS_EXCEPTION_ERROR', index=10, number=10003,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACTION_NOT_EXISTS_ERROR', index=11, number=20001,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACTION_STATUS_EXCEPTION_ERROR', index=12, number=20002,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=370,
  serialized_end=698,
)


UNKNOW_ERROR = -1
SUCCESS = 0
SYSTEM_ERROR = 1
PARSE_PB_ERROR = 2
PARAMETER_ERROR = 3
AUTH_ERROR = 4
NETWORK_ERROR = 5
TIMEOUT_ERROR = 6
USER_NOT_EXISTS_ERROR = 10001
PASSWORD_INCORRECT_ERROR = 10002
USER_STATUS_EXCEPTION_ERROR = 10003
ACTION_NOT_EXISTS_ERROR = 20001
ACTION_STATUS_EXCEPTION_ERROR = 20002



_PBRESPONSE = descriptor.Descriptor(
  name='PBResponse',
  full_name='PBResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='PBResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error_message', full_name='PBResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='actions', full_name='PBResponse.actions', index=2,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='messages', full_name='PBResponse.messages', index=3,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='users', full_name='PBResponse.users', index=4,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='activitys', full_name='PBResponse.activitys', index=5,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comments', full_name='PBResponse.comments', index=6,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='PBResponse.user', index=7,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='action', full_name='PBResponse.action', index=8,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='merchant', full_name='PBResponse.merchant', index=9,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=73,
  serialized_end=367,
)

_PBRESPONSE.fields_by_name['code'].enum_type = _PBRESULTCODE
_PBRESPONSE.fields_by_name['actions'].message_type = action_pb2._PBACTION
_PBRESPONSE.fields_by_name['messages'].message_type = message_pb2._PBMESSAGE
_PBRESPONSE.fields_by_name['users'].message_type = user_pb2._PBUSERBASIC
_PBRESPONSE.fields_by_name['activitys'].message_type = action_pb2._PBACTIVITY
_PBRESPONSE.fields_by_name['comments'].message_type = action_pb2._PBCOMMENT
_PBRESPONSE.fields_by_name['user'].message_type = user_pb2._PBUSER
_PBRESPONSE.fields_by_name['action'].message_type = action_pb2._PBACTION
_PBRESPONSE.fields_by_name['merchant'].message_type = action_pb2._PBMERCHANT
DESCRIPTOR.message_types_by_name['PBResponse'] = _PBRESPONSE

class PBResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBResponse)

# @@protoc_insertion_point(module_scope)
