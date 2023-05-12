#!/usr/bin/env python
import ansible_runner

ansible_runner.interface.run(
    private_data_dir='.',
    playbook='test.yml'
)
