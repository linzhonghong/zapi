__author__ = 'zhonghong'

'''
/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ZAPI` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `ZAPI`;

DROP TABLE IF EXISTS `t_test`;

CREATE TABLE `t_test` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `info` VARCHAR(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

'''

class TestModel(object):
    from zapi.core.db import DB
    db = DB('')
    def select(self):
        return self.db.exec_sql('select * from test')

    def chain_select(self):
        return self.db.select('*').from_('test').where({'id': 1}).limit(1).get()

    def insert(self):
        return self.db.insert('test', {'id': 1, 'info': "i am info"})

    def update(self):
        return self.db.update('test', {'info': "i am info too"}, {'id': 1})

    def delete(self):
        return self.db.delete('test', {'id': 1})

    def transaction(self):
        self.db.begin()
        try:
            self.db.update('test', {'info': "i am transaction info"}, {'id': 1})
        except:
            self.db.end('rollback')
        else:
            self.db.end()


    def just_sql(self):
        # just return the sql statement, not execute.
        return self.db.to_sql.select('*').from_('test').where({'id': 1}).limit(1).get()
