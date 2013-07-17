# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import basic_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='user.proto',
  package='',
  serialized_pb='\n\nuser.proto\x1a\x0b\x62\x61sic.proto\"\xb2\x01\n\x05PBSNS\x12\x12\n\ntel_number\x18\x01 \x01(\t\x12\x11\n\tqq_number\x18\x02 \x01(\t\x12\x13\n\x0bqq_weibo_id\x18\x03 \x01(\t\x12\x15\n\rqq_weibo_nick\x18\x04 \x01(\t\x12\x15\n\rsina_weibo_id\x18\x05 \x01(\t\x12\x17\n\x0fsina_weibo_nick\x18\x06 \x01(\t\x12\x11\n\trenren_id\x18\x07 \x01(\t\x12\x13\n\x0brenren_nick\x18\x08 \x01(\t\"j\n\x05PBLog\x12\x15\n\rlast_log_date\x18\x01 \x01(\x05\x12\x13\n\x0blast_log_ip\x18\x02 \x01(\x05\x12\x19\n\x11last_log_latitude\x18\x03 \x01(\x02\x12\x1a\n\x12last_log_longitude\x18\x04 \x01(\x02\"V\n\x0ePBRegistration\x12\x10\n\x08reg_date\x18\x01 \x02(\x05\x12\"\n\x08reg_type\x18\x02 \x01(\x0e\x32\n.PBRegType:\x04NICK\x12\x0e\n\x06reg_ip\x18\x03 \x01(\t\"[\n\x08PBDevice\x12\x11\n\tdevice_id\x18\x01 \x02(\t\x12\x11\n\tdevice_os\x18\x02 \x02(\t\x12\x14\n\x0c\x64\x65vice_token\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x04 \x01(\t\"\xc9\x01\n\x0bPBStatistic\x12\x11\n\tfan_count\x18\x01 \x01(\x05\x12\x14\n\x0c\x66ollow_count\x18\x02 \x01(\x05\x12\x13\n\x0bmy_activity\x18\x03 \x01(\x05\x12\x15\n\rnew_fan_count\x18\x14 \x01(\x05\x12\x18\n\x10new_follow_count\x18\x16 \x01(\x05\x12\x19\n\x11new_message_count\x18\x17 \x01(\x05\x12\x16\n\x0enew_feed_count\x18\x18 \x01(\x05\x12\x18\n\x10new_notice_count\x18\x19 \x01(\x05\"\x8f\x02\n\x0bPBUserBasic\x12\r\n\x05uname\x18\x02 \x02(\t\x12\x0c\n\x04nick\x18\x03 \x01(\t\x12\x1f\n\x04role\x18\x04 \x01(\x0e\x32\x0b.PBUserRole:\x04USER\x12\x0e\n\x06gender\x18\x05 \x01(\x08\x12\x0e\n\x06\x61vatar\x18\x06 \x01(\t\x12&\n\x06status\x18\x07 \x01(\x0e\x32\r.PBUserStatus:\x07OFFLINE\x12\x14\n\x0cintroduction\x18\x08 \x01(\t\x12\x12\n\nbirth_date\x18\t \x01(\x05\x12\x0c\n\x04tags\x18\n \x03(\t\x12\x10\n\x08password\x18\x0b \x03(\t\x12\x1d\n\x08relation\x18\x14 \x01(\x0e\x32\x0b.PBRelation\x12\x11\n\tnote_name\x18\x15 \x01(\t\"\xcf\x01\n\x06PBUser\x12\x0b\n\x03uid\x18\x01 \x02(\t\x12 \n\nbasic_info\x18\x02 \x02(\x0b\x32\x0c.PBUserBasic\x12!\n\x08reg_info\x18\x03 \x01(\x0b\x32\x0f.PBRegistration\x12\x18\n\x08log_info\x18\x04 \x01(\x0b\x32\x06.PBLog\x12\x1e\n\x0b\x64\x65vice_info\x18\x05 \x01(\x0b\x32\t.PBDevice\x12\x18\n\x08sns_info\x18\x06 \x01(\x0b\x32\x06.PBSNS\x12\x1f\n\tstatistic\x18\x07 \x01(\x0b\x32\x0c.PBStatistic*E\n\nPBRelation\x12\x0b\n\x07STRANGE\x10\x00\x12\n\n\x06\x46OLLOW\x10\x01\x12\x07\n\x03\x46\x41N\x10\x02\x12\n\n\x06\x46RIEND\x10\x03\x12\t\n\x05\x42LACK\x10\x04*t\n\tPBRegType\x12\x08\n\x04NICK\x10\x00\x12\x0e\n\nSINA_WEIBO\x10\x01\x12\x0c\n\x08QQ_WEIBO\x10\x02\x12\n\n\x06RENREN\x10\x03\x12\x0c\n\x08QQ_SPACE\x10\x04\x12\n\n\x06KAIXIN\x10\x05\x12\x0c\n\x08\x46\x41\x43\x45\x42OOK\x10\x06\x12\x0b\n\x07TWITTER\x10\x07*9\n\nPBUserRole\x12\x08\n\x04USER\x10\x01\x12\t\n\x05\x41\x44MIN\x10\x02\x12\x07\n\x03VIP\x10\x03\x12\r\n\tFORBIDDEN\x10\x04*3\n\x0cPBUserStatus\x12\x0b\n\x07OFFLINE\x10\x01\x12\n\n\x06ONLINE\x10\x02\x12\n\n\x06HIDDEN\x10\x03')

_PBRELATION = descriptor.EnumDescriptor(
  name='PBRelation',
  full_name='PBRelation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STRANGE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FOLLOW', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FAN', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FRIEND', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BLACK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1185,
  serialized_end=1254,
)


_PBREGTYPE = descriptor.EnumDescriptor(
  name='PBRegType',
  full_name='PBRegType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NICK', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SINA_WEIBO', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='QQ_WEIBO', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RENREN', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='QQ_SPACE', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='KAIXIN', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FACEBOOK', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TWITTER', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1256,
  serialized_end=1372,
)


_PBUSERROLE = descriptor.EnumDescriptor(
  name='PBUserRole',
  full_name='PBUserRole',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='USER', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ADMIN', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='VIP', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FORBIDDEN', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1374,
  serialized_end=1431,
)


_PBUSERSTATUS = descriptor.EnumDescriptor(
  name='PBUserStatus',
  full_name='PBUserStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='OFFLINE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ONLINE', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='HIDDEN', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1433,
  serialized_end=1484,
)


STRANGE = 0
FOLLOW = 1
FAN = 2
FRIEND = 3
BLACK = 4
NICK = 0
SINA_WEIBO = 1
QQ_WEIBO = 2
RENREN = 3
QQ_SPACE = 4
KAIXIN = 5
FACEBOOK = 6
TWITTER = 7
USER = 1
ADMIN = 2
VIP = 3
FORBIDDEN = 4
OFFLINE = 1
ONLINE = 2
HIDDEN = 3



_PBSNS = descriptor.Descriptor(
  name='PBSNS',
  full_name='PBSNS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tel_number', full_name='PBSNS.tel_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='qq_number', full_name='PBSNS.qq_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='qq_weibo_id', full_name='PBSNS.qq_weibo_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='qq_weibo_nick', full_name='PBSNS.qq_weibo_nick', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sina_weibo_id', full_name='PBSNS.sina_weibo_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sina_weibo_nick', full_name='PBSNS.sina_weibo_nick', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='renren_id', full_name='PBSNS.renren_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='renren_nick', full_name='PBSNS.renren_nick', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=28,
  serialized_end=206,
)


_PBLOG = descriptor.Descriptor(
  name='PBLog',
  full_name='PBLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='last_log_date', full_name='PBLog.last_log_date', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_log_ip', full_name='PBLog.last_log_ip', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_log_latitude', full_name='PBLog.last_log_latitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_log_longitude', full_name='PBLog.last_log_longitude', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=208,
  serialized_end=314,
)


_PBREGISTRATION = descriptor.Descriptor(
  name='PBRegistration',
  full_name='PBRegistration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reg_date', full_name='PBRegistration.reg_date', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reg_type', full_name='PBRegistration.reg_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reg_ip', full_name='PBRegistration.reg_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=316,
  serialized_end=402,
)


_PBDEVICE = descriptor.Descriptor(
  name='PBDevice',
  full_name='PBDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='device_id', full_name='PBDevice.device_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device_os', full_name='PBDevice.device_os', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device_token', full_name='PBDevice.device_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device_name', full_name='PBDevice.device_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=404,
  serialized_end=495,
)


_PBSTATISTIC = descriptor.Descriptor(
  name='PBStatistic',
  full_name='PBStatistic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='fan_count', full_name='PBStatistic.fan_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='follow_count', full_name='PBStatistic.follow_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='my_activity', full_name='PBStatistic.my_activity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_fan_count', full_name='PBStatistic.new_fan_count', index=3,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_follow_count', full_name='PBStatistic.new_follow_count', index=4,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_message_count', full_name='PBStatistic.new_message_count', index=5,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_feed_count', full_name='PBStatistic.new_feed_count', index=6,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='new_notice_count', full_name='PBStatistic.new_notice_count', index=7,
      number=25, type=5, cpp_type=1, label=1,
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
  serialized_start=498,
  serialized_end=699,
)


_PBUSERBASIC = descriptor.Descriptor(
  name='PBUserBasic',
  full_name='PBUserBasic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uname', full_name='PBUserBasic.uname', index=0,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nick', full_name='PBUserBasic.nick', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role', full_name='PBUserBasic.role', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gender', full_name='PBUserBasic.gender', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avatar', full_name='PBUserBasic.avatar', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='PBUserBasic.status', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='introduction', full_name='PBUserBasic.introduction', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='birth_date', full_name='PBUserBasic.birth_date', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tags', full_name='PBUserBasic.tags', index=8,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='PBUserBasic.password', index=9,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='relation', full_name='PBUserBasic.relation', index=10,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='note_name', full_name='PBUserBasic.note_name', index=11,
      number=21, type=9, cpp_type=9, label=1,
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
  serialized_start=702,
  serialized_end=973,
)


_PBUSER = descriptor.Descriptor(
  name='PBUser',
  full_name='PBUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uid', full_name='PBUser.uid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='basic_info', full_name='PBUser.basic_info', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reg_info', full_name='PBUser.reg_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='log_info', full_name='PBUser.log_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device_info', full_name='PBUser.device_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sns_info', full_name='PBUser.sns_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='statistic', full_name='PBUser.statistic', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=976,
  serialized_end=1183,
)

_PBREGISTRATION.fields_by_name['reg_type'].enum_type = _PBREGTYPE
_PBUSERBASIC.fields_by_name['role'].enum_type = _PBUSERROLE
_PBUSERBASIC.fields_by_name['status'].enum_type = _PBUSERSTATUS
_PBUSERBASIC.fields_by_name['relation'].enum_type = _PBRELATION
_PBUSER.fields_by_name['basic_info'].message_type = _PBUSERBASIC
_PBUSER.fields_by_name['reg_info'].message_type = _PBREGISTRATION
_PBUSER.fields_by_name['log_info'].message_type = _PBLOG
_PBUSER.fields_by_name['device_info'].message_type = _PBDEVICE
_PBUSER.fields_by_name['sns_info'].message_type = _PBSNS
_PBUSER.fields_by_name['statistic'].message_type = _PBSTATISTIC
DESCRIPTOR.message_types_by_name['PBSNS'] = _PBSNS
DESCRIPTOR.message_types_by_name['PBLog'] = _PBLOG
DESCRIPTOR.message_types_by_name['PBRegistration'] = _PBREGISTRATION
DESCRIPTOR.message_types_by_name['PBDevice'] = _PBDEVICE
DESCRIPTOR.message_types_by_name['PBStatistic'] = _PBSTATISTIC
DESCRIPTOR.message_types_by_name['PBUserBasic'] = _PBUSERBASIC
DESCRIPTOR.message_types_by_name['PBUser'] = _PBUSER

class PBSNS(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSNS
  
  # @@protoc_insertion_point(class_scope:PBSNS)

class PBLog(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBLOG
  
  # @@protoc_insertion_point(class_scope:PBLog)

class PBRegistration(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBREGISTRATION
  
  # @@protoc_insertion_point(class_scope:PBRegistration)

class PBDevice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDEVICE
  
  # @@protoc_insertion_point(class_scope:PBDevice)

class PBStatistic(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSTATISTIC
  
  # @@protoc_insertion_point(class_scope:PBStatistic)

class PBUserBasic(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBUSERBASIC
  
  # @@protoc_insertion_point(class_scope:PBUserBasic)

class PBUser(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBUSER
  
  # @@protoc_insertion_point(class_scope:PBUser)

# @@protoc_insertion_point(module_scope)
