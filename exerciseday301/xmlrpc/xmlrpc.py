import xmlrpc.client


url = "https://hkanthonyleung-bftraining-staging-6864362.dev.odoo.com/"
db = "hkanthonyleung-bftraining"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db,username,password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

print(models)
