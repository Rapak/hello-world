

prod_config = {'dialect' : 'postgresql', 'host' : 'semantic.amazonaws-prod.com', 'port': 5432,
               'database name' : 'semantic', 'user name' : 'admin', 'password' : '12345'}

staging_config = {'dialect': 'postgresql', 'host': 'semantic.amazonaws-staging.com', 'port': 5432,
                  'database name': 'semantic', 'user name': 'admin', 'password': 'root'}

print  prod_config['dialect'],"://",prod_config['user name'],":",prod_config['password'],"@",prod_config['host'],":",prod_config['port'],"/",prod_config['database name']

print  staging_config['dialect'],"://",staging_config['user name'],":",staging_config['password'],"@",staging_config['host'],":",staging_config['port'],"/",staging_config['database name']
