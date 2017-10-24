#!/usr/bin/env python

import json
import os
import sys
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
from collections import Iterable

class Ansible_hoc_api:

	class ResultCallback(CallbackBase):
		def v2_runner_on_ok(self, result, **kwargs):
			host = result._host
			self.data = json.dumps({host.name: result._result}, indent=4)
			#print (json.dumps({host.name: result._result}, indent=4))
			return self.data


	def __init__(self,host_list):
		self.__variable_manager = VariableManager()
		self.__loader = DataLoader()
		self.__inventory = Inventory(loader=self.__loader, variable_manager=self.__variable_manager,  host_list=host_list)
		self.__Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
		self.__options = self.__Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=1, remote_user='root', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)
		self.__passwords = {}

	def run(self,host,module,command):
		results_callback = Ansible_hoc_api.ResultCallback()
		play_source = {"name":"Ansible Ad-Hoc","hosts":host,"gather_facts":"no","tasks":[{"action":{"module":module,"args":command}}]}
		play = Play().load(play_source, variable_manager=self.__variable_manager, loader=self.__loader)
		tqm = None
		tqm = TaskQueueManager(inventory=self.__inventory,variable_manager=self.__variable_manager,loader=self.__loader,options=self.__options,passwords=self.__passwords,run_tree=False,stdout_callback=results_callback,)
		result = tqm.run(play)
		output = json.loads(results_callback.data)
		list_output = list(output.values())
		dic_output = list_output[0]
		facts_output = dic_output["ansible_facts"]
		return facts_output

	def run_command(self,host,module,command):
		results_callback = Ansible_hoc_api.ResultCallback()
		play_source = {"name": "Ansible Ad-Hoc", "hosts": host, "gather_facts": "no",
					   "tasks": [{"action": {"module": module, "args": command}}]}
		play = Play().load(play_source, variable_manager=self.__variable_manager, loader=self.__loader)
		tqm = None
		tqm = TaskQueueManager(inventory=self.__inventory, variable_manager=self.__variable_manager,
							   loader=self.__loader, options=self.__options, passwords=self.__passwords, run_tree=False,
							   stdout_callback=results_callback, )
		result = tqm.run(play)
		output = json.loads(results_callback.data)
		return output

def infodetail(gethost_list,gethost,getmodule,getcommand):
	command = Ansible_hoc_api(gethost_list)
	information = command.run(gethost,getmodule,getcommand)
	dns = information["ansible_dns"]["nameservers"]
	cpu = information["ansible_processor_vcpus"]
	processor = information["ansible_processor"][1]
	ip = information["ansible_default_ipv4"]
	hostname = information["ansible_hostname"]
	memory = information["ansible_memory_mb"]["real"]
	#lsb = information["ansible_lsb"]["description"]
	get_value = [{"dns":dns,"cpu":cpu,"processor":processor,"ip":ip,"hostname":hostname,"memory":memory,"lsb":"CentOS release 6.9 (Final)"}]
	return get_value



#print (isinstance('Ansible_hoc_api', Iterable))
#infodetail("/etc/ansible/hosts","test","setup","")
