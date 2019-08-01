#!/usr/bin/python3.6

import os
import xml.tree.ElementTree as et

class ONT(object, ):

	def __init__(self, ont_id, label, ont_type, fsan_serial, reg_id, ont_status,
					last_boot_timestamp, wan_mac_address, running_sw_version,
					current_ip, config_synced_with_server, custom_config, ):
		self.ont_id = ont_id 
		self.label = label
		self.ont_type = ont_type
		self.fsan_serial = fsan_serial
		self.reg_id = reg_id
		self.ont_status = ont_status
		self.last_boot_timestamp = last_boot_timestamp
		self.wan_mac_address = wan_mac_address
		self.running_sw_version = running_sw_version
		self.current_ip = current_ip
		self.config_synced_with_server = config_synced_with_server
		self.custom_config = custom_config

	def __str__(self,):
		print(f'{self.ont_id}, {self.label}, {self.ont_type}, \
			{self.fsan_serial}, {self.reg_id}, {self.ont_status},  \
			{self.last_boot_timestamp}, {self.wan_mac_address}, \
			{self.running_sw_version},{self.current_ip}, \
			{self.config_synced_with_server}, {self.custom_config},')

class Port(object, ):

	def __init__(self, port, port_id, port_name, port_type, is_configured,
				is_enabled, vlan, tag_mode, downstream_meter, upstream_meter,
				auto_negotiate, configured_eth_speed, configured_eth_duplex,
				operational_status, description, ):
		self.port = port
		self.port_id = port_id
		self.port_name = port_name
		self.port_type = port_type
		self.is_configured = is_configured
		self.is_enabled = is_enabled
		self.vlan = vlan
		self.tag_mode = tag_mode
		self.downstream_meter = downstream_meter
		self.upstream_meter = upstream_meter
		self.auto_negotiate = auto_negotiate
		self.configured_eth_speed = configured_eth_speed
		self.configured_eth_duplex = configured_eth_duplex
		self.operational_status = operational_status
		self.description = description


	def __str__(self,):
		print(
			f'{self.port}, {self.port_id}, {self.port_name}, {self.port_type},\
			{self.is_configured},{self.is_enabled}, {self.vlan}, \
			{self.tag_mode}, {self.downstream_meter}, {self.upstream_meter},\
			{self.auto_negotiate}, {self.configured_eth_speed}, \
			{self.configured_eth_duplex},{self.operational_status}, {self.description},')
