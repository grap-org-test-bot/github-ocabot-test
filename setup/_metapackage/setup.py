import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-grap-github-ocabot-test",
    description="Meta package for grap-github-ocabot-test Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-module_test',
        'odoo12-addon-module_test_2',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
