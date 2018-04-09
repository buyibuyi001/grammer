
def log(sql,args=())：
    logging.info('SQL: %s' % sql)

def create_pool()：
    logging.info()
    create __pool
def select(sql,args,size=None)：
    global __pool
     __pool.get().execute()
    logging.info()
def execute(sql,args,autocommit=True):
    logging.info()
    global __pool
    async with __pool.get() as conn
       if not autocommit:
            await conn.begin()
    conn.cursor.execute()
    affected = conn.cursor.rowcount
def create_args_string(num):
    return num ?

class Field(object):
    def __init__(self,name,column_type,primary_key,default):
        init
    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)
class StringField,BooleanField,IntegerField,FloatField,TextField():
    def __init__(): super().__init__()

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs)
    tableName= attrs.get('__table__',None) or name
    mappings, fields, primaryKey = dict(),[],None
