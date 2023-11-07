Demo of using a multiple inventory hierarchy with `ansible-runner`.

# Setup

    python3.9 -m venv venv39
    . venv39/bin/activate
    pip install -U pip
    code requirements.txt
    pip install -r requirements.txt 


# Demo
This defines two inventories:
- `default_inventory`, defines:
    - group `mygroup` containing `localhost`
    - `myvar` on `all` group as `foo`
    - `myvar` for `mygroup` as `bar`
- `overrides`, defines:
    - `myvar` for `mygroup` as `baz`

In `env/envvars`, `ANSIBLE_INVENTORY` is defined as `default_inventory` first and `overrides` second. Note the paths here are resolved relative to the `projects/` directory.

Therefore running:

    $ . venv39/bin/activate
    (venv39) $ ansible-runner run . -p test.yml

should show `myvar` as `baz`.


It also provides `cli.py`, showing how the above test can be run from Python.

# Notes
Futher experimentation shows that:
- Empty `hosts` files are necessary in the inventory directories
- If a directory `inventory/` exists (in the private data directory), runner ignores the ANSIBLE_INVENTORY variable.
- Contrary to docs, using `ansible-runner run --inventory whatever` actually writes `whatever` to `inventory/hosts`, creating the file/directory if necessary!
