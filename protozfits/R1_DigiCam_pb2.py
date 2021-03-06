# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: R1_DigiCam.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import CoreMessages_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='R1_DigiCam.proto',
  package='DataModel',
  serialized_pb=_b('\n\x10R1_DigiCam.proto\x12\tDataModel\x1a\x12\x43oreMessages.proto\"\x0f\n\rDigiCamConfig\"\x0e\n\x0c\x44igiCamEvent')
  ,
  dependencies=[CoreMessages_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DIGICAMCONFIG = _descriptor.Descriptor(
  name='DigiCamConfig',
  full_name='DataModel.DigiCamConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=66,
)


_DIGICAMEVENT = _descriptor.Descriptor(
  name='DigiCamEvent',
  full_name='DataModel.DigiCamEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['DigiCamConfig'] = _DIGICAMCONFIG
DESCRIPTOR.message_types_by_name['DigiCamEvent'] = _DIGICAMEVENT

DigiCamConfig = _reflection.GeneratedProtocolMessageType('DigiCamConfig', (_message.Message,), dict(
  DESCRIPTOR = _DIGICAMCONFIG,
  __module__ = 'R1_DigiCam_pb2'
  # @@protoc_insertion_point(class_scope:DataModel.DigiCamConfig)
  ))
_sym_db.RegisterMessage(DigiCamConfig)

DigiCamEvent = _reflection.GeneratedProtocolMessageType('DigiCamEvent', (_message.Message,), dict(
  DESCRIPTOR = _DIGICAMEVENT,
  __module__ = 'R1_DigiCam_pb2'
  # @@protoc_insertion_point(class_scope:DataModel.DigiCamEvent)
  ))
_sym_db.RegisterMessage(DigiCamEvent)


# @@protoc_insertion_point(module_scope)
