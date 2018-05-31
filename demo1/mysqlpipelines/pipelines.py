from .sql import Sql
from demo1.items import Demo1Item

class Demo1Pipeline(object):

    def process_item(self,item,spider):
        if isinstance(item,Demo1Item):
            name_id = item['name_id']
            ret=Sql.select_name(name_id)
            if ret[0]==1:
                print("already exist")
                pass
            else:
                xs_name=item['name']
                xs_author=item['author']
                category=item['category']
                Sql.insert_dd_name(xs_name,xs_author,category,name_id)
                print("start save title")
