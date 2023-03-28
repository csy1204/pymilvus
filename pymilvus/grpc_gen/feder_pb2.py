# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feder.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x66\x65\x64\x65r.proto\x12\x12milvus.proto.feder\x1a\x0c\x63ommon.proto\"9\n\x10SegmentIndexData\x12\x11\n\tsegmentID\x18\x01 \x01(\x03\x12\x12\n\nindex_data\x18\x02 \x01(\t\"A\n\x18\x46\x65\x64\x65rSegmentSearchResult\x12\x11\n\tsegmentID\x18\x01 \x01(\x03\x12\x12\n\nvisit_info\x18\x02 \x01(\t\"t\n\x19ListIndexedSegmentRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x17\n\x0f\x63ollection_name\x18\x02 \x01(\t\x12\x12\n\nindex_name\x18\x03 \x01(\t\"]\n\x1aListIndexedSegmentResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x12\n\nsegmentIDs\x18\x02 \x03(\x03\"\x8f\x01\n\x1f\x44\x65scribeSegmentIndexDataRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x17\n\x0f\x63ollection_name\x18\x02 \x01(\t\x12\x12\n\nindex_name\x18\x03 \x01(\t\x12\x13\n\x0bsegmentsIDs\x18\x04 \x03(\x03\"\xb9\x02\n DescribeSegmentIndexDataResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12W\n\nindex_data\x18\x02 \x03(\x0b\x32\x43.milvus.proto.feder.DescribeSegmentIndexDataResponse.IndexDataEntry\x12\x37\n\x0cindex_params\x18\x03 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x1aV\n\x0eIndexDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.milvus.proto.feder.SegmentIndexData:\x02\x38\x01\x42\x32Z0github.com/milvus-io/milvus-proto/go-api/federpbb\x06proto3')



_SEGMENTINDEXDATA = DESCRIPTOR.message_types_by_name['SegmentIndexData']
_FEDERSEGMENTSEARCHRESULT = DESCRIPTOR.message_types_by_name['FederSegmentSearchResult']
_LISTINDEXEDSEGMENTREQUEST = DESCRIPTOR.message_types_by_name['ListIndexedSegmentRequest']
_LISTINDEXEDSEGMENTRESPONSE = DESCRIPTOR.message_types_by_name['ListIndexedSegmentResponse']
_DESCRIBESEGMENTINDEXDATAREQUEST = DESCRIPTOR.message_types_by_name['DescribeSegmentIndexDataRequest']
_DESCRIBESEGMENTINDEXDATARESPONSE = DESCRIPTOR.message_types_by_name['DescribeSegmentIndexDataResponse']
_DESCRIBESEGMENTINDEXDATARESPONSE_INDEXDATAENTRY = _DESCRIBESEGMENTINDEXDATARESPONSE.nested_types_by_name['IndexDataEntry']
SegmentIndexData = _reflection.GeneratedProtocolMessageType('SegmentIndexData', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTINDEXDATA,
  '__module__' : 'feder_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.feder.SegmentIndexData)
  })
_sym_db.RegisterMessage(SegmentIndexData)

FederSegmentSearchResult = _reflection.GeneratedProtocolMessageType('FederSegmentSearchResult', (_message.Message,), {
  'DESCRIPTOR' : _FEDERSEGMENTSEARCHRESULT,
  '__module__' : 'feder_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.feder.FederSegmentSearchResult)
  })
_sym_db.RegisterMessage(FederSegmentSearchResult)

ListIndexedSegmentRequest = _reflection.GeneratedProtocolMessageType('ListIndexedSegmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINDEXEDSEGMENTREQUEST,
  '__module__' : 'feder_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.feder.ListIndexedSegmentRequest)
  })
_sym_db.RegisterMessage(ListIndexedSegmentRequest)

ListIndexedSegmentResponse = _reflection.GeneratedProtocolMessageType('ListIndexedSegmentResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINDEXEDSEGMENTRESPONSE,
  '__module__' : 'feder_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.feder.ListIndexedSegmentResponse)
  })
_sym_db.RegisterMessage(ListIndexedSegmentResponse)

DescribeSegmentIndexDataRequest = _reflection.GeneratedProtocolMessageType('DescribeSegmentIndexDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBESEGMENTINDEXDATAREQUEST,
  '__module__' : 'feder_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.feder.DescribeSegmentIndexDataRequest)
  })
_sym_db.RegisterMessage(DescribeSegmentIndexDataRequest)

DescribeSegmentIndexDataResponse = _reflection.GeneratedProtocolMessageType('DescribeSegmentIndexDataResponse', (_message.Message,), {

  'IndexDataEntry' : _reflection.GeneratedProtocolMessageType('IndexDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DESCRIBESEGMENTINDEXDATARESPONSE_INDEXDATAENTRY,
    '__module__' : 'feder_pb2'
    # @@protoc_insertion_point(class_scope:milvus.proto.feder.DescribeSegmentIndexDataResponse.IndexDataEntry)
    })
  ,
  'DESCRIPTOR' : _DESCRIBESEGMENTINDEXDATARESPONSE,
  '__module__' : 'feder_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.feder.DescribeSegmentIndexDataResponse)
  })
_sym_db.RegisterMessage(DescribeSegmentIndexDataResponse)
_sym_db.RegisterMessage(DescribeSegmentIndexDataResponse.IndexDataEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/milvus-io/milvus-proto/go-api/federpb'
  _DESCRIBESEGMENTINDEXDATARESPONSE_INDEXDATAENTRY._options = None
  _DESCRIBESEGMENTINDEXDATARESPONSE_INDEXDATAENTRY._serialized_options = b'8\001'
  _SEGMENTINDEXDATA._serialized_start=49
  _SEGMENTINDEXDATA._serialized_end=106
  _FEDERSEGMENTSEARCHRESULT._serialized_start=108
  _FEDERSEGMENTSEARCHRESULT._serialized_end=173
  _LISTINDEXEDSEGMENTREQUEST._serialized_start=175
  _LISTINDEXEDSEGMENTREQUEST._serialized_end=291
  _LISTINDEXEDSEGMENTRESPONSE._serialized_start=293
  _LISTINDEXEDSEGMENTRESPONSE._serialized_end=386
  _DESCRIBESEGMENTINDEXDATAREQUEST._serialized_start=389
  _DESCRIBESEGMENTINDEXDATAREQUEST._serialized_end=532
  _DESCRIBESEGMENTINDEXDATARESPONSE._serialized_start=535
  _DESCRIBESEGMENTINDEXDATARESPONSE._serialized_end=848
  _DESCRIBESEGMENTINDEXDATARESPONSE_INDEXDATAENTRY._serialized_start=762
  _DESCRIBESEGMENTINDEXDATARESPONSE_INDEXDATAENTRY._serialized_end=848
# @@protoc_insertion_point(module_scope)
